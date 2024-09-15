from django.urls import path
from .views import ListView, DetailView, BookCreateView, BookUpdateView, BookDeleteView

urlpatterns = [
    path('books/', ListView.as_view(), name='book-list'),
    path('books/<int:pk>/', DetailView.as_view(), name='book-detail'),
    path('books/<int:pk>/', DetailView.as_view(), name='book-detail'), # Retrieve a book by ID
    path('books/<int:pk>/update/', UpdateView.as_view(), name='book-update'), # Update a book
    path('books/<int:pk>/delete/', DeleteView.as_view(), name='book-delete'), # Delete a book
]
