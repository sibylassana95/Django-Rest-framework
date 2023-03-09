
from django.contrib import admin
from django.urls import include
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('books.urls')),
    path('api/',include('api.urls'))
]
