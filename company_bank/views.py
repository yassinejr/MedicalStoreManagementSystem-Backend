from django.http import Http404
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.authentication import JWTAuthentication

from .models import CompanyBank
from .serializers import CompanyBankSerializer


# Create your views here.
class CompanyBankList(APIView):
    """
    List all company banks, or create a new one.
    """
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        company_bank = CompanyBank.objects.all()
        serializer = CompanyBankSerializer(company_bank, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = CompanyBankSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CompanyBankDetail(APIView):
    """
    Retrieve, update or delete a company instance.
    """

    def get_object(self, pk):
        try:
            return CompanyBank.objects.get(pk=pk)
        except CompanyBank.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        company_bank = self.get_object(pk)
        serializer = CompanyBankSerializer(company_bank)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        company_bank = self.get_object(pk)
        serializer = CompanyBankSerializer(company_bank, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        company_bank = self.get_object(pk)
        company_bank.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
