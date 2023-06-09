from django.contrib import admin
from django.urls import path, include # new
from .views import DishListView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app.urls')), # new
    path('', DishListView.as_view(), name='home')
]
