from django.urls import path
from .views import  CreateBookview, ListBookView, BookDeleteView, BookUpdateView

urlpatterns = [
    path("create_book", CreateBookview.as_view(), name='create_book'),  
    path("all/",ListBookView.as_view(), name='books_list'), 
    path("details/<int:pk>",BookDeleteView.as_view(), name='books_detail'),  
    path("edit/<int:pk>", BookUpdateView.as_view(), name='edit_book'),  
]
