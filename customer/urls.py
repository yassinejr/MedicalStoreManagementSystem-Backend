from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

app_name = 'customer'

urlpatterns = [
    path('', views.CustomerList.as_view(), name="customer-list"),
    path('<int:pk>/', views.CustomerDetail.as_view(), name="customer-detail"),
]

urlpatterns = format_suffix_patterns(urlpatterns)