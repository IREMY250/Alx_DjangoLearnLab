from django.urls import path
from . import views

urlpatterns = [
    # List and Detail views (already existing)
    path('books/', views.BookListView.as_view(), name='book-list'),
    path('books/<int:pk>/', views.BookDetailView.as_view(), name='book-detail'),

    # Create, Update, and Delete views
    path('books/create/', views.BookCreateView.as_view(), name='book-create'),
    
    # Update and Delete paths should include <int:pk>
    path('books/update/<int:pk>/', views.BookUpdateView.as_view(), name='book-update'),
    path('books/delete/<int:pk>/', views.BookDeleteView.as_view(), name='book-delete'),
]
