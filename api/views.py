from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from .serializers import BookSerializer, PriceInfoOfBookSerializer, AuthorSerializer
from .models import Book, Author
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.views import APIView


# @api_view(['GET'])
# def allbooks(rq):
#     books = Book.objects.all()
#     bookser = BookSerializer(books, many=True)
#     return Response(bookser.data, status=200)

class BookViewset(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class PriceView(APIView):
    def get(self, request, id):
        book = Book.objects.get(id=id)
        priceser = PriceInfoOfBookSerializer(book)
        return Response(priceser.data, status=200)


class BookAuthorDetailsView(APIView):
    def get(self, rq, id):
        book = Book.objects.get(id=id)
        author = book.author
        author_ser = AuthorSerializer(author)

        return Response(author_ser.data, status=200)


class AuthorBookView(APIView):
    def get(self, rq, id):
        author = Author.objects.get(id=id)
        books = author.book_set.all()
        bookser = BookSerializer(books, many=True)
        return Response(bookser.data, status=200)


def random(rq, id):
    return HttpResponse("Random")
