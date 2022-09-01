from django.shortcuts import render

from api.serializers import PortfolioSerializer
from api.models import Portfolio
from rest_framework import viewsets, status
from rest_framework.response import Response


class PortfolioView(viewsets.ViewSet):
    def list(self, request):
        return Response(status=status.HTTP_200_OK)

    def retrieve(self, request, pk):
        return Response(status=status.HTTP_200_OK)

    def create(self, request):
        return Response(status=status.HTTP_200_OK)

    def update(self, request, pk):
        return Response(status=status.HTTP_200_OK)

    def delete(self, request, pk):
        return Response(status=status.HTTP_200_OK)
