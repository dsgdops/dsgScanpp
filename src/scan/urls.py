from django.urls import path

from . import views

urlpatterns = [
    path('', views.scanHistory.as_view(), name='scan_history'),
    path('rapport/<uuid:uuid>/', views.scanDetails.as_view(), name='scan_details'),
    path('configuration/', views.configurationIndex.as_view(), name='configuration_index'),
    path('configuration/scan/', views.scanConfiguration.as_view(), name='scan_configuration'),
    path('configuration/categorie/', views.categorieConfiguration.as_view(), name='categorie_configuration'),
    path('configuration/categorie/settings/', views.categorieSettings.as_view(), name='categorie_settings'),
    path('configuration/categorie/settings/add-host/', views.categorieAddHost.as_view(), name='categorie_add-host'),
    path('configuration/success/', views.scanSuccess.as_view(), name='scan_success'),
]