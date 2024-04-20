from rest_framework import serializers
from .models import Book, Author


class BookSerializer(serializers.ModelSerializer):
    author_name = serializers.SerializerMethodField(source='get_author_name')  #

    class Meta:
        model = Book
        fields = ['id', 'author_id', 'name', 'price', 'author_name']

    def get_author_name(self, obj):
        return obj.author.name if obj.author else None


class PriceInfoOfBookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['price', 'name']


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = "__all__"
