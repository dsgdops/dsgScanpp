from django.urls import path

from . import views

urlpatterns = [
    path('', views.scanHistory.as_view(), name='scan_history'),
    path('rapport/<uuid:uuid>/', views.scanDetails.as_view(), name='scan_details'),
    path('delete/<uuid:pk>/', views.scanDelete.as_view(), name='scan_delete'),
    path('configuration/', views.configurationIndex.as_view(), name='configuration_index'),
    path('configuration/scan/', views.scanConfiguration.as_view(), name='scan_configuration'),
    path('configuration/categorie/', views.categorieConfiguration.as_view(), name='categorie_configuration'),
    path('configuration/categorie/list-host', views.listHost.as_view(), name='list_host'),
    path('configuration/categorie/list-categorie', views.listCategorie.as_view(), name='list_categorie'),
    path('configuration/categorie/delete-host/<int:pk>/', views.hostDelete.as_view(), name='host_delete'),
    path('configuration/categorie/settings/', views.categorieSettings.as_view(), name='categorie_settings'),
    path('configuration/categorie/delete-categorie/<int:pk>', views.categorieDelete.as_view(), name='categorie_delete'),
    path('configuration/categorie/settings/add-host/', views.categorieAddHost.as_view(), name='categorie_add-host'),
    #path('fdp'),
]