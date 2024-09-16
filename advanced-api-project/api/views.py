from rest_framework import generics
from django.http import HttpResponse
from rest_framework import filters.SearchFilter, filters.OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from django_filters import rest_framework
from .models import Book
from .serializers import BookSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated

# List and Create books
class ListView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['title', 'author__name', 'publication_year']  # Filtering on title, author's name, and publication year
    search_fields = ['title', 'author__name']  # Searching by title and author's name
    ordering_fields = ['title', 'publication_year']  # Ordering by title and publication year
    ordering = ['title']  # Default ordering

# Retrieve, Update, and Delete books
class DetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    Handles retrieving, updating, or deleting a book.
    Only authenticated users can update or delete books.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

# Create a new book (authenticated users only)
class CreateView(generics.CreateAPIView):
    """
    Allows authenticated users to create a new book.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

# Update a book (authenticated users only)
class UpdateView(generics.UpdateAPIView):
    """
    Allows authenticated users to update an existing book.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

# Delete a book (authenticated users only)
class DeleteView(generics.DestroyAPIView):
    """
    Allows authenticated users to delete a book.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

def home(request):
    return HttpResponse("<h1>Welcome to the Advanced API Project</h1>")