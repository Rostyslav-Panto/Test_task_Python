from django.shortcuts import get_object_or_404

from api.serializers import PortfolioSerializer, ImageSerializer, CommentSerializer
from api.models import Portfolio, Image, Comment
from rest_framework import viewsets, status
from rest_framework.response import Response


class PortfolioView(viewsets.ViewSet):
    serializer_class = PortfolioSerializer

    @staticmethod
    def list(request):
        queryset = Portfolio.objects.all()
        serializer = PortfolioSerializer(queryset, many=True)
        return Response(serializer.data)

    @staticmethod
    def retrieve(request, pk):
        queryset = Portfolio.objects.all()
        recipe = get_object_or_404(queryset, pk=pk)
        serializer = PortfolioSerializer(recipe)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @staticmethod
    def create(request):
        serializer = PortfolioSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @staticmethod
    def update(request, pk=None):
        queryset = Portfolio.objects.all()
        portfolio = get_object_or_404(queryset, pk=pk)
        serializer = PortfolioSerializer(portfolio, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @staticmethod
    def destroy(request, pk=None):
        queryset = Portfolio.objects.all()
        portfolio = get_object_or_404(queryset, pk=pk)
        portfolio.delete()
        return Response(f"Object id={pk} Deleted", status=status.HTTP_204_NO_CONTENT)


class ImageView(viewsets.ViewSet):
    serializer_class = ImageSerializer

    @staticmethod
    def list(request):
        queryset = Image.objects.all().order_by('publication_date')
        serializer = ImageSerializer(queryset, many=True)
        return Response(serializer.data)

    @staticmethod
    def retrieve(request, pk):
        queryset = Image.objects.all()
        recipe = get_object_or_404(queryset, pk=pk)
        serializer = ImageSerializer(recipe)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @staticmethod
    def create(request):
        serializer = ImageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @staticmethod
    def update(request, pk):
        queryset = Image.objects.all()
        portfolio = get_object_or_404(queryset, pk=pk)
        serializer = ImageSerializer(portfolio, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @staticmethod
    def destroy(request, pk):
        queryset = Image.objects.all()
        portfolio = get_object_or_404(queryset, pk=pk)
        portfolio.delete()
        return Response(f"Object id={pk} Deleted", status=status.HTTP_204_NO_CONTENT)


class CommentView(viewsets.ViewSet):
    serializer_class = CommentSerializer

    @staticmethod
    def list(request):
        queryset = Comment.objects.all()
        serializer = CommentSerializer(queryset, many=True)
        return Response(serializer.data)

    @staticmethod
    def retrieve(request, pk):
        queryset = Comment.objects.all()
        recipe = get_object_or_404(queryset, pk=pk)
        serializer = CommentSerializer(recipe)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @staticmethod
    def create(request):
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @staticmethod
    def destroy(request, pk):
        queryset = Comment.objects.all()
        portfolio = get_object_or_404(queryset, pk=pk)
        portfolio.delete()
        return Response(f"Object id={pk} Deleted", status=status.HTTP_204_NO_CONTENT)
