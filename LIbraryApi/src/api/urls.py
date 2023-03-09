from api.views import BookAPIView
from django.urls import path


urlpatterns = [
path("", BookAPIView.as_view(), name="book_list"),
]