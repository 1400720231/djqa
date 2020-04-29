from django.contrib import admin
from django.urls import path,include
from django.contrib import admin 
from apps.user.views import IndexView
import os
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/', include('apps.user.urls', namespace="user")),
    path('operation/', include('apps.operation.urls', namespace="operation")),
    path('book/', include('apps.book.urls', namespace="book")),
    path('', IndexView.as_view(), name='index'),
]


 