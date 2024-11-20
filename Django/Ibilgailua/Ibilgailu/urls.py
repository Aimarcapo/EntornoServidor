from django.urls import path 
from . import views 
urlpatterns = [
    path('Kotxe/', views.kotxe_list, name="kotxe-default"),
    path('Kotxe/new/', views.kotxe_new, name='kotxe-new'),
    path('Kotxe/delete/', views.kotxe_delete, name='kotxe-delete'),
    path('Kotxe/edit/<str:id>', views.edit_kotxe, name='kotxe-edit'),#c
    path('Pertsona/', views.pertsona_list, name="pertsona-default"),
    path('Pertsona/new/', views.pertsona_new, name="pertsona-new"),
    ]
