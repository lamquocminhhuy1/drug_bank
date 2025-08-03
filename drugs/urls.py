from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'drugs', views.DrugViewSet)
router.register(r'interactions', views.DrugInteractionViewSet)

app_name = 'drugs'

# Web routes
web_urlpatterns = [
    path('', views.home, name='home'),
    path('search/', views.search_interactions, name='search'),
    path('drug/<str:drug_id>/', views.drug_detail, name='drug_detail'),
    path('interaction/<int:interaction_id>/', views.interaction_detail, name='interaction_detail'),
]

# API routes
api_urlpatterns = [
    path('', include(router.urls)),
    path('stats/', views.api_stats, name='api_stats'),
]

# Combined for backward compatibility
urlpatterns = web_urlpatterns + api_urlpatterns 