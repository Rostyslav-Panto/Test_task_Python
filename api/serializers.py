from rest_framework import serializers

from api.models import Portfolio, Image


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        exclude = ('publication_date',)


class PortfolioSerializer(serializers.ModelSerializer):
    images = ImageSerializer(many=True, read_only=True)

    class Meta:
        model = Portfolio
        fields = (
            'name',
            'description',
            'images',)
