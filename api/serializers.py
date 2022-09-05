from rest_framework import serializers

from api.models import Portfolio, Image


class PortfolioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Portfolio


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        exclude = ('publication_date',)
