from django.urls import path

from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='home-scan'),
    path('add/<str:ip_address>', views.add_report, name='add-report'),
]