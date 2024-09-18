from django.shortcuts import render
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from book.models import Book
from django.urls import reverse_lazy
# Create your views here.
class CreateBookview(CreateView):
    model = Book
    fields = ["author", "title", "year"]
    template_name = "createBook.html"
    
    def get_success_url(self) -> str:
        return reverse_lazy("books_detail", kwargs={"pk": self.object.pk})
        
class ListBookView(ListView):
    model = Book
    queryset = Book.objects.all()
    template_name = "Books.html"
    
# class BookDetailView(DetailView): 
#     model = Book
#     template_name = "book_detail.html"
    
class BookUpdateView(UpdateView):
    model = Book
    fields = ["author", "title", "year"]
    template_name = "updateBook.html"
    def get_success_url(self) -> str:
        return reverse_lazy("books_detail", kwargs={"pk": self.object.pk})
    
    
class BookDeleteView(DeleteView):
    model = Book
    template_name = "deleteBook.html"
    success_url = reverse_lazy('books_list')