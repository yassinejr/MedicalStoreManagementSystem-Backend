from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views


app_name = 'company_bank'

urlpatterns = [
    path('', views.CompanyBankList.as_view(), name="company-bank-list"),
    path('<int:pk>/', views.CompanyBankDetail.as_view(), name="company-bank-detail"),
]

urlpatterns = format_suffix_patterns(urlpatterns)