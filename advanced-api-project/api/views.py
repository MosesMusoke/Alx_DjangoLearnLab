from rest_framework import generics
from django.http import HttpResponse
from .models import Book
from .serializers import BookSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated

# ListView: Retrieve all books
class ListView(generics.ListCreateAPIView):
    """
    View to list all books and create a new book.
    Only authenticated users can create a book.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        # Example of customizing creation behavior
        serializer.save()

# DetailView: Retrieve a single book by ID
class DetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    View to retrieve, update, or delete a single book by its ID.
    Only authenticated users can update or delete a book.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_update(self, serializer):
        # Example of customizing update behavior
        serializer.save()


# CreateView: Add a new book
class CreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]  # Only authenticated users can create

# UpdateView: Modify an existing book
class UpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]  # Only authenticated users can update


# DeleteView: Remove a book
class DeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]  # Only authenticated users can delete

def home(request):
    return HttpResponse("<h1>Welcome to the Advanced API Project</h1>")