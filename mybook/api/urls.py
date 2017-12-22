from django.urls import path
from api import views

urlpatterns = [
    # 書籍
    path('v1/books/', views.book_list, name='book_list'),  # 一覧
]