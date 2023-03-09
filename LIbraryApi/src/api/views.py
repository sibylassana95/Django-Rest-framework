from .serializers import BookSerializer
from books.models import Book
from rest_framework import generics


class BookAPIView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
