from django.shortcuts import render
from relationship_app.models import Book

def list_all_books(request):
  books = Book.objects.all()
  context = {'books': books}
  return render(request, 'list_books.html', context)

from django.views.generic import DetailView
from relationship_app.models import Library

class LibraryDetailView(DetailView):
  model = Library
  template_name = 'library_detail.html'

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    return context