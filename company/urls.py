from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('', views.CompanyList.as_view()),
    path('<int:pk>/', views.CompanyDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)