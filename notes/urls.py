from django.urls import path
from .views import index, create, edit, delete

urlpatterns = [
    path('mypage/', index, name='base'),
    path('create/', create, name='create'),
    path('edit/<id>/', edit, name='edit'),
    path('delete/<id>/', delete, name='delete')
]