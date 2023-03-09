

from books.views import BookListView
from django.urls import path

urlpatterns = [
    path('', BookListView.as_view(),name='home'),
    
]
