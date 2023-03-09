from books.models import Book
from django.shortcuts import render
from django.views.generic import ListView

class BookListView(ListView):
	model = Book
	template_name = 'books/book_list.html'
