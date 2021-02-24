"""MSMS_Django_Backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


from company import views
from company_bank import views
# from company_account.views import *
# from customer.views import *
# from customer_request.views import *
# from employee.views import *
# from employee_bank.views import *
# from employee_salary.views import *
# from invoice.views import *
# from invoice_detail.views import *
# from medicine.views import *
# from medical_detail.views import *


# router = DefaultRouter()
# router.register(r'company', views.CompanyViewset, basename='company')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/gettoken/', TokenObtainPairView.as_view(), name='gettoken'),
    path('api/refresh_token/', TokenRefreshView.as_view(), name='refresh_token'),
    path('api/companies/', include('company.urls')),
    path('api/company_bank/', include('company_bank.urls')),
    # path('api/', include(router.urls)),
    # path('company_account/', include(company_account.urls)),
    # path('api/customer/', include(customer.urls)),
    # path('api/customer_request/', include(customer_request.urls)),
    # path('api/employee/', include(employee.urls)),
    # path('api/employee_bank/', include(employee_bank.urls)),
    # path('api/employee_salary/', include(employee_salary.urls)),
    # path('api/invoice/', include(invoice.urls)),
    # path('api/invoice_detail/', include(invoice_detail.urls)),
    # path('api/medicine/', include(medicine.urls)),
    # path('api/medical_detail/', include(medical_detail.urls)),
]
