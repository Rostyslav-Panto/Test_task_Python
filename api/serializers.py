from rest_framework import serializers

from api.models import Portfolio, Image, Comment


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = (
            'description',
            'publication_date',
            'author_id'
        )
        read_only_fields = ('publication_date',)


class ImageSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Image
        fields = (
            'image',
            'name',
            'description',
            'portfolio_id',
            'comments',)


class PortfolioSerializer(serializers.ModelSerializer):
    images = ImageSerializer(many=True, read_only=True)

    class Meta:
        model = Portfolio
        fields = (
            'name',
            'description',
            'images',)
