from rest_framework.test import APITestCase, APIClient
from django.urls import reverse
from rest_framework import status
from .models import Book
from django.contrib.auth.models import User

class BookAPITestCase(APITestCase):

    def setUp(self):
        """
        Create initial data and setup test client.
        """
        self.client = APIClient()
        self.user = User.objects.create_user(username="testuser", password="testpass")
        self.client.login(username="testuser", password="testpass")

        # Creating a sample book instance
        self.book = Book.objects.create(title="Test Book", author="Test Author", publication_year=2023)

    def test_create_book(self):
        """
        Test creating a book with authenticated user.
        """
        data = {"title": "New Book", "author": "New Author", "publication_year": 2021}
        response = self.client.post(reverse('book-list'), data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 2)
        self.assertEqual(Book.objects.get(id=2).title, "New Book")

    def test_list_books(self):
        """
        Test retrieving the list of books.
        """
        response = self.client.get(reverse('book-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_book_detail(self):
        """
        Test retrieving a single book by ID.
        """
        response = self.client.get(reverse('book-detail', args=[self.book.id]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], "Test Book")

    def test_update_book(self):
        """
        Test updating an existing book.
        """
        data = {"title": "Updated Book", "author": "Updated Author", "publication_year": 2022}
        response = self.client.put(reverse('book-detail', args=[self.book.id]), data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book.refresh_from_db()
        self.assertEqual(self.book.title, "Updated Book")

    def test_delete_book(self):
        """
        Test deleting a book.
        """
        response = self.client.delete(reverse('book-detail', args=[self.book.id]))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 0)

    def test_filter_books(self):
        """
        Test filtering books by title.
        """
        response = self.client.get(reverse('book-list'), {'title': 'Test Book'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], 'Test Book')

    def test_search_books(self):
        """
        Test searching books by title.
        """
        response = self.client.get(reverse('book-list'), {'search': 'Test'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_order_books(self):
        """
        Test ordering books by publication year.
        """
        Book.objects.create(title="Older Book", author="Another Author", publication_year=2019)
        response = self.client.get(reverse('book-list'), {'ordering': 'publication_year'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]['title'], "Older Book")

