from django.urls import path

from . import views

urlpatterns = [
    path('', views.scanHistory.as_view(), name='scan_history'),
    path('rapport/<uuid:uuid>/', views.scanDetails.as_view(), name='scan_details'),
    path('configuration/', views.scanConfiguration.as_view(), name='scan_configuration'),
    path('configuration/categorie/', views.categorieConfiguration.as_view(), name='categorie_configuration'),
    path('configuration/success/', views.scanSuccess.as_view(), name='scan_success'),
]