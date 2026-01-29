from django.contrib import admin
from django.urls import path
from expenses.views import index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
]
