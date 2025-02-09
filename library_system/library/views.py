from rest_framework import viewsets
from .models import Book, Transaction
from .serializers import BookSerializer, TransactionSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

class BookViewSet(viewsets.ModelViewSet):

    queryset = Book.objects.all()
    serializer_class = BookSerializer

class TransactionViewSet(viewsets.ModelViewSet):

    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
