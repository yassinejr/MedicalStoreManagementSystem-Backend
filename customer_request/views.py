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

from .models import CustomerRequest
from .serializers import CustomerRequestSerializer


class CustomerRequestList(APIView):
    """
    List all customers, or create a new one.
    """
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        customer_request = CustomerRequest.objects.all()
        serializer = CustomerRequestSerializer(customer_request, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = CustomerRequestSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CustomerRequestDetail(APIView):
    """
    Retrieve, update or delete a customer instance.
    """

    def get_object(self, pk):
        try:
            return CustomerRequest.objects.get(pk=pk)
        except CustomerRequest.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        customer_request = self.get_object(pk)
        serializer = CustomerRequestSerializer(customer_request)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        customer_request = self.get_object(pk)
        serializer = CustomerRequestSerializer(customer_request, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        customer_request = self.get_object(pk)
        customer_request.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
