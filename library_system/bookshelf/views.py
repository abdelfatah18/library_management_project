from rest_framework import generics
from .models import Bookshelf, Book
from .serializers import BookshelfSerializer, BookSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

class BookshelfListCreateAPIView(generics.ListCreateAPIView):
    
    queryset = Bookshelf.objects.all()
    serializer_class = BookshelfSerializer

class BookshelfRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):

    queryset = Bookshelf.objects.all()
    serializer_class = BookshelfSerializer

class BookListCreateAPIView(generics.ListCreateAPIView):

    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):

    queryset = Book.objects.all()
    serializer_class = BookSerializer

