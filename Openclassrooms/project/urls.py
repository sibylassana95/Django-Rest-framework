from django.contrib import admin
from django.urls import include
from django.urls import path
from shop.views import CategoryAPIView,ProductView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/category/', CategoryAPIView.as_view()),
    path('api/product/', ProductView.as_view()),
]
