from django.urls import path
from . import views

app_name = 'drugs'

urlpatterns = [
    path('', views.home, name='home'),
    path('search/', views.search_interactions, name='search'),
    path('drug/<str:drug_id>/', views.drug_detail, name='drug_detail'),
    path('interaction/<int:interaction_id>/', views.interaction_detail, name='interaction_detail'),
] 