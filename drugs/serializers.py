from rest_framework import serializers
from .models import Drug, DrugInteraction


class DrugSerializer(serializers.ModelSerializer):
    class Meta:
        model = Drug
        fields = '__all__'


class DrugInteractionSerializer(serializers.ModelSerializer):
    drug1_name = serializers.CharField(source='drug1.ten_thuoc', read_only=True)
    drug2_name = serializers.CharField(source='drug2.ten_thuoc', read_only=True)
    severity_display = serializers.CharField(source='get_severity_display', read_only=True)
    severity_color = serializers.CharField(source='get_severity_color', read_only=True)

    class Meta:
        model = DrugInteraction
        fields = '__all__'


class DrugSearchSerializer(serializers.Serializer):
    query = serializers.CharField(max_length=255, help_text="Tên thuốc hoặc hoạt chất để tìm kiếm")
    severity = serializers.ChoiceField(choices=DrugInteraction.SEVERITY_CHOICES, required=False, help_text="Lọc theo mức độ tương tác") 