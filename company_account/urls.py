from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views


app_name = 'company_account'

urlpatterns = [
    path('', views.CompanyAccountList.as_view(), name="company-account-list"),
    path('<int:pk>/', views.CompanyAccountDetail.as_view(), name="company-account-detail"),
]

urlpatterns = format_suffix_patterns(urlpatterns)