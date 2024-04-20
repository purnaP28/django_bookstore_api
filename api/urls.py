from django.urls import path, include
from .views import BookViewset, PriceView, random, AuthorViewSet, BookAuthorDetailsView, AuthorBookView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'book', BookViewset)
router.register(r'author', AuthorViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path("book/<int:id>/price/", PriceView.as_view()),
    path("book/<int:id>/author/", BookAuthorDetailsView.as_view()),
    path("author/<int:id>/books/", AuthorBookView.as_view()),

]
