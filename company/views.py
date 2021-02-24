from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.generics import get_object_or_404
from django.http import Http404
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.authentication import JWTAuthentication

from .models import Company
from .serializers import CompanySerializer


# Create your views here.
# class CompanyViewset(viewsets.ViewSet):
# queryset = Company.objects.all()
# serializer_class = CompanySerializer
#     def list(self, request):
#         company = Company.objects.all()
#         serializer = CompanySerializer(company, many=True, context={'request': request})
#         response_dict = {"error": False, "message": "All company list data", "data": serializer.data}
#         return Response(response_dict)
#
#     def create(self, request):
#         try:
#             serializer = CompanySerializer(data=request.data, context={"request": request})
#             serializer.is_valid()
#             serializer.save()
#             dict_response = {"error": False, "message": "Company data saved successfully"}
#         except:
#             dict_response = {"error": True, "message": "Company data not saved"}
#         return Response(dict_response)
#
#     def upadte(self, request, pk=None):
#         try:
#             queryset = Company.objects.all()
#             company = get_object_or_404(queryset, pk=pk)
#             serializer = CompanySerializer(company, data=request.data, context={"request": request})
#             serializer.is_valid()
#             serializer.save()
#             dict_response = {"error": False, "message": "Company data updated successfully"}
#         except:
#             dict_response = {"error": True, "message": "Error while updating"}
#         return Response(dict_response)
#
#
# company_list = CompanyViewSet.as_view({"get": "list"})
# company_create = CompanyViewSet.as_view({"post": "create"})
# company_update = CompanyViewSet.as_view({"put": "update"})


# class CompanyViewset(viewsets.ModelViewSet):
#     """
#     API endpoint that allows companies to be viewed or edited.
#     """
#     queryset = Company.objects.all()
#     serializer_class = CompanySerializer
#     permission_classes = [permissions.IsAuthenticated]


class CompanyList(APIView):
    """
    List all companies, or create a new one.
    """
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self, request, format=None):
        companies = Company.objects.all()
        serializer = CompanySerializer(companies, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = CompanySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CompanyDetail(APIView):
    """
    Retrieve, update or delete a company instance.
    """

    def get_object(self, pk):
        try:
            return Company.objects.get(pk=pk)
        except Company.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        company = self.get_object(pk)
        serializer = CompanySerializer(company)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        company = self.get_object(pk)
        serializer = CompanySerializer(company, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        company = self.get_object(pk)
        company.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
