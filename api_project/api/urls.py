from django.urls import path
from . import views

urlpatterns = [
    # List and Detail views (already existing)
    path('books/', views.CustomBookListView.as_view(), name='book-list'),
    path('books/<int:pk>/', views.CustomBookDetailView.as_view(), name='book-detail'),

    # Create, Update, and Delete views
    path('books/create/', views.CustomBookCreateView.as_view(), name='book-create'),
    path('books/update/', views.CustomBookUpdateView.as_view(), name='book-update'),
    path('books/delete/', views.CustomBookDeleteView.as_view(), name='book-delete'),
]