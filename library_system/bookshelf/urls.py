from django.urls import path
from .views import BookshelfListCreateAPIView, BookshelfRetrieveUpdateDestroyAPIView, BookListCreateAPIView, BookRetrieveUpdateDestroyAPIView

urlpatterns = [
    path('', BookshelfListCreateAPIView.as_view(), name='bookshelf-list-create'),
    path('<int:pk>/', BookshelfRetrieveUpdateDestroyAPIView.as_view(), name='bookshelf-detail'),
    path('books/', BookListCreateAPIView.as_view(), name='book-list-create'),
    path('books/<int:pk>/', BookRetrieveUpdateDestroyAPIView.as_view(), name='book-detail'),
]
