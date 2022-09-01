from django.shortcuts import get_object_or_404

from api.serializers import PortfolioSerializer
from api.models import Portfolio
from rest_framework import viewsets, status
from rest_framework.response import Response


class PortfolioView(viewsets.ViewSet):
    serializer_class = PortfolioSerializer

    def list(self, request):
        queryset = Portfolio.objects.all()
        serializer = PortfolioSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk):
        queryset = Portfolio.objects.all()
        recipe = get_object_or_404(queryset, pk=pk)
        serializer = PortfolioSerializer(recipe)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request):
        serializer = PortfolioSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        queryset = Portfolio.objects.all()
        portfolio = get_object_or_404(queryset, pk=pk)
        serializer = PortfolioSerializer(portfolio, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        queryset = Portfolio.objects.all()
        portfolio = get_object_or_404(queryset, pk=pk)
        portfolio.delete()
        return Response(f"Object id={pk} Deleted", status=status.HTTP_204_NO_CONTENT)
