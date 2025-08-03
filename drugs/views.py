from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.db.models import Q, Count
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from .models import Drug, DrugInteraction
from .serializers import DrugSerializer, DrugInteractionSerializer, DrugSearchSerializer


def home(request):
    """Home page with search functionality and dynamic statistics"""
    # Get dynamic statistics from database
    total_drugs = Drug.objects.count()
    total_interactions = DrugInteraction.objects.count()
    
    # Get severity breakdown
    severity_stats = DrugInteraction.objects.values('severity').annotate(
        count=Count('severity')
    ).order_by('severity')
    
    # Convert to dictionary for easy template access
    severity_breakdown = {}
    for stat in severity_stats:
        severity_breakdown[stat['severity']] = stat['count']
    
    context = {
        'total_drugs': total_drugs,
        'total_interactions': total_interactions,
        'severity_breakdown': severity_breakdown,
    }
    return render(request, 'drugs/home.html', context)


def search_interactions(request):
    """Search for drug interactions"""
    query = request.GET.get('q', '')
    severity = request.GET.get('severity', '')
    
    interactions = DrugInteraction.objects.all()
    
    if query:
        # Search in drug names and active ingredients
        interactions = interactions.filter(
            Q(drug1__ten_thuoc__icontains=query) |
            Q(drug2__ten_thuoc__icontains=query) |
            Q(drug1__hoat_chat__icontains=query) |
            Q(drug2__hoat_chat__icontains=query) |
            Q(mechanism__icontains=query) |
            Q(consequence__icontains=query)
        )
    
    if severity:
        interactions = interactions.filter(severity=severity)
    
    context = {
        'interactions': interactions[:50],  # Limit to 50 results
        'query': query,
        'severity': severity,
        'severity_choices': DrugInteraction.SEVERITY_CHOICES,
    }
    
    return render(request, 'drugs/search.html', context)


def drug_detail(request, drug_id):
    """Show drug details and its interactions"""
    drug = get_object_or_404(Drug, id=drug_id)
    interactions = DrugInteraction.objects.filter(
        Q(drug1=drug) | Q(drug2=drug)
    )
    
    context = {
        'drug': drug,
        'interactions': interactions,
    }
    
    return render(request, 'drugs/drug_detail.html', context)


def interaction_detail(request, interaction_id):
    """Show detailed interaction information"""
    interaction = get_object_or_404(DrugInteraction, id=interaction_id)
    
    context = {
        'interaction': interaction,
    }
    
    return render(request, 'drugs/interaction_detail.html', context)


def api_stats(request):
    """API endpoint for getting application statistics"""
    total_drugs = Drug.objects.count()
    total_interactions = DrugInteraction.objects.count()
    
    # Get severity breakdown
    severity_stats = DrugInteraction.objects.values('severity').annotate(
        count=Count('severity')
    ).order_by('severity')
    
    # Convert to list for JSON response
    severity_breakdown = []
    for stat in severity_stats:
        severity_breakdown.append({
            'severity': stat['severity'],
            'count': stat['count'],
            'label': dict(DrugInteraction.SEVERITY_CHOICES)[stat['severity']]
        })
    
    stats = {
        'total_drugs': total_drugs,
        'total_interactions': total_interactions,
        'severity_breakdown': severity_breakdown,
        'last_updated': DrugInteraction.objects.aggregate(
            last_updated=Count('updated_at')
        )['last_updated']
    }
    
    return JsonResponse(stats)


class DrugViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint cho danh sách thuốc
    
    list:
        Trả về danh sách tất cả thuốc
    retrieve:
        Trả về thông tin chi tiết của một thuốc
    """
    queryset = Drug.objects.all()
    serializer_class = DrugSerializer
    lookup_field = 'id'
    
    def get_queryset(self):
        """Filter drugs by search query"""
        queryset = Drug.objects.all()
        query = self.request.query_params.get('q', None)
        if query:
            queryset = queryset.filter(
                Q(ten_thuoc__icontains=query) |
                Q(hoat_chat__icontains=query) |
                Q(nhom_thuoc__icontains=query)
            )
        return queryset


class DrugInteractionViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint cho danh sách tương tác thuốc
    
    list:
        Trả về danh sách tất cả tương tác thuốc
    retrieve:
        Trả về thông tin chi tiết của một tương tác
    search:
        Tìm kiếm tương tác theo từ khóa
    """
    queryset = DrugInteraction.objects.all()
    serializer_class = DrugInteractionSerializer
    
    def get_queryset(self):
        """Filter interactions by search query and severity"""
        queryset = DrugInteraction.objects.all()
        query = self.request.query_params.get('q', None)
        severity = self.request.query_params.get('severity', None)
        
        if query:
            queryset = queryset.filter(
                Q(drug1__ten_thuoc__icontains=query) |
                Q(drug2__ten_thuoc__icontains=query) |
                Q(drug1__hoat_chat__icontains=query) |
                Q(drug2__hoat_chat__icontains=query) |
                Q(mechanism__icontains=query) |
                Q(consequence__icontains=query)
            )
        
        if severity:
            queryset = queryset.filter(severity=severity)
        
        return queryset
    
    @swagger_auto_schema(
        operation_description="Tìm kiếm tương tác thuốc theo từ khóa",
        manual_parameters=[
            openapi.Parameter(
                'q',
                openapi.IN_QUERY,
                description="Từ khóa tìm kiếm (tên thuốc, hoạt chất, cơ chế, hậu quả)",
                type=openapi.TYPE_STRING,
                required=False
            ),
            openapi.Parameter(
                'severity',
                openapi.IN_QUERY,
                description="Mức độ tương tác (contraindicated, major, moderate, minor)",
                type=openapi.TYPE_STRING,
                required=False,
                enum=['contraindicated', 'major', 'moderate', 'minor']
            )
        ],
        responses={
            200: DrugInteractionSerializer(many=True),
            400: "Bad Request"
        }
    )
    @action(detail=False, methods=['get'])
    def search(self, request):
        """Search for drug interactions"""
        serializer = DrugSearchSerializer(data=request.query_params)
        if serializer.is_valid():
            query = serializer.validated_data.get('q', '')
            severity = serializer.validated_data.get('severity', '')
            
            queryset = self.get_queryset()
            
            if query:
                queryset = queryset.filter(
                    Q(drug1__ten_thuoc__icontains=query) |
                    Q(drug2__ten_thuoc__icontains=query) |
                    Q(drug1__hoat_chat__icontains=query) |
                    Q(drug2__hoat_chat__icontains=query) |
                    Q(mechanism__icontains=query) |
                    Q(consequence__icontains=query)
                )
            
            if severity:
                queryset = queryset.filter(severity=severity)
            
            page = self.paginate_queryset(queryset)
            if page is not None:
                serializer = self.get_serializer(page, many=True)
                return self.get_paginated_response(serializer.data)
            
            serializer = self.get_serializer(queryset, many=True)
            return Response(serializer.data)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 