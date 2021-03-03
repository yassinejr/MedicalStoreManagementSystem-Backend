from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

app_name = 'company'

urlpatterns = [
    path('', views.CompanyList.as_view(), name="company-list"),
    path('<int:pk>/', views.CompanyDetail.as_view(), name="company-detail"),
]

urlpatterns = format_suffix_patterns(urlpatterns)