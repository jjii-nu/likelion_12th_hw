from django.urls import path
from main import views

app_name = "main"
urlpatterns = [
    path('', views.mainpage, name="mainpage"),
    path('second', views.secondpage, name="secondpage"),
    path('new-post', views.new_post, name="new-post"),
    path('create', views.create, name="create"),
    path('<int:id>', views.detail, name="detail"),
    path('edit/<int:id>', views.edit, name="edit"),
    path('update/<int:id>', views.update, name="update"),    
    path('delete/<int:id>', views.delete, name="delete"),
]