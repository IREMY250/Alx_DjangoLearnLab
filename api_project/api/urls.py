#api/urls.py
from django.urls import path
from . import views
urlpatterns =[
    #list and detail views (already existing)
    path('books/', views.BooklistView.as_view(), name='book-list'),
    path('books/<int:pk>/', views.BookDetailView.as_view(), name='book-detail'),

     #create, update ,detele views

    path('books/create/', views.BookCreateView.as_view(), name='book-create'),
    path('books/update/', views.BookUpdateView.as_view(), name='book-update'),
    path('books/delete', views.BookDeleteView.as_view(), name='book-delete'),
]