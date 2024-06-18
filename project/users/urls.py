from django.urls import path
from django.contrib import admin
from .views import *

app_name = "users"
urlpatterns = [
    path('admin/', admin.site.urls),
    path('mypage/<int:id>', mypage, name="mypage"),
    path('follow/<int:id>', follow, name="follow"),
]