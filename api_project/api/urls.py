from django.urls import path
from .views import CustomBookCreateView, CustomBookListView, CustomBookDetailView, CustomBookUpdateView, CustomBookDeleteView

urlpatterns = [
    #list and detail views (already existing)
    path('books/', CustomBookListView.as_view(), name='list'),
    path('books/<int:pk>', CustomBookDetailView.as_view(), name='detail'),

    #create, update, and delete views
    path('books/update/<int:pk>', CustomBookUpdateView.as_view(), name='update'),
    path('books/delete/<int:pk>', CustomBookDeleteView.as_view(), name='delete'),
    path('books/create', CustomBookCreateView.as_view(), name='create'),
]