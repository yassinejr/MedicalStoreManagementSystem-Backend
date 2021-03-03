from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

app_name = 'customer_request'

urlpatterns = [
    path('', views.CustomerRequestList.as_view(), name="customer-request-list"),
    path('<int:pk>/', views.CustomerRequestDetail.as_view(), name="customer-request-detail"),
]

urlpatterns = format_suffix_patterns(urlpatterns)