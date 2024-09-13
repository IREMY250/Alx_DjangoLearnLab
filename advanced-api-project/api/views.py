
from django_filters import rest_framework
from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated

from .models import Book
from .serializers import BookSerializer

class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookDetailView(generics.Serializer
    lookup_field = 'pk'  # Use primary key for lookup

class BookCreateView(generics.CreateAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]Serializer

class BookUpdateView(generics.UpdateAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]  # Set permission later
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    lookup_field = 'pk'

class BookDeleteView(generics.DestroyAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]  # Set permission later
    queryset = Book.objects.all()
    lookup_field = 'pk'