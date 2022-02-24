from django.urls import path

from . import views

urlpatterns = [
    path('', views.scanHistory.as_view(), name='scan_history'),
    path('rapport/<uuid:uuid>/', views.scanDetails.as_view(), name='scan_details'),
    path('add/<str:ip_address>', views.add_report, name='add-report'),
]