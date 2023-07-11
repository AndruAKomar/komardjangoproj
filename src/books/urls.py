from django.urls import path
from . import views

app_name='books'
urlpatterns = [
    path('books-list/', views.BooksListView.as_view(), name='BooksListView'),     #переход к просмотру всех товаров-книг 
    path('books-view/<int:pk>', views.BookView.as_view(), name='BookView'),   #переход к конкретному объекту/деталям BOOK по его РК       
    path('books-add/', views.BooksCreateView.as_view(), name='BooksCreateView'),        #переход к форме для добавления новой BOOK 
    path('books-upd/<int:pk>', views.BooksUpdateView.as_view(), name='BooksUpdateView'),        #переход к форме для редактирования BOOK по его РК 
    path('books-delete/<int:pk>', views.BooksDeleteView.as_view(), name='BooksDeleteView'),     #переход к форме для удаления Жанра по его РК
      
]
