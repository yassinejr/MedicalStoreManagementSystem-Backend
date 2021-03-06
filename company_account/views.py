from django.http import Http404
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.authentication import JWTAuthentication

from .models import CompanyAccount
from .serializers import CompanyAccountSerializer


# Create your views here.
class CompanyAccountList(APIView):
    """
    List all company accounts, or create a new one.
    """
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        company_bank = CompanyAccount.objects.all()
        serializer = CompanyAccountSerializer(company_bank, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = CompanyAccountSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CompanyAccountDetail(APIView):
    """
    Retrieve, update or delete a company account instance.
    """

    def get_object(self, pk):
        try:
            return CompanyAccount.objects.get(pk=pk)
        except CompanyAccount.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        company_account = self.get_object(pk)
        serializer = CompanyAccountSerializer(company_account)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        company_account = self.get_object(pk)
        serializer = CompanyAccountSerializer(company_account, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        company_account = self.get_object(pk)
        company_account.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
