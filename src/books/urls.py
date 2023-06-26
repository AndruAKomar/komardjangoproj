from django.urls import path
from . import views

app_name='books'
urlpatterns = [
    path('books-list/', views.BooksListView.as_view(), name='BooksListView'),     #переход к просмотру всех товаров-книг
    
    path('books-view/<int:pk>', views.BookView.as_view(), name='BookView'),   #переход к конкретному объекту/деталям BOOK по его РК
    # path('author/<int:pk>', views.AuthorView.as_view(), name='AuthorView'),     #переход к просмотру всех объектов Авторов
    # path('series/<int:pk>', views.SeriesView.as_view(), name='SeriesView'),     #переход к просмотру всех объектов Серии
    # path('publish/<int:pk>', views.PublishView.as_view(), name='PublishView'),     #переход к просмотру всех объектов Издательст
        
    path('books-add/', views.BooksCreateView.as_view(), name='BooksCreateView'),        #переход к форме для добавления новой BOOK
    # path('author-add/', views.AuthorCreateView.as_view(), name='AuthorCreateView'),        #переход к форме для добавления Авторов 
    # path('series-add/', views.SeriesCreateView.as_view(), name='SeriesCreateView'),        #переход к форме для добавления Серии 
    # path('publish-add/', views.PublishCreateView.as_view(), name='PublishCreateView'),        #переход к форме для добавления Издательства 
    
    path('books-upd/<int:pk>', views.BooksUpdateView.as_view(), name='BooksUpdateView'),        #переход к форме для редактирования BOOK по его РК
    # path('author-upd/<int:pk>', views.AuthorUpdateView.as_view(), name='AuthorUpdateView'),        #переход к форме для редактирования Авторов по его РК
    # path('series-upd/<int:pk>', views.SeriesUpdateView.as_view(), name='SeriesUpdateView'),        #переход к форме для редактирования Серии по его РК
    # path('publish-upd/<int:pk>', views.PublishUpdateView.as_view(), name='PublishUpdateView'),        #переход к форме для редактирования Издательст по его РК
    
    path('books-delete/<int:pk>', views.BooksDeleteView.as_view(), name='BooksDeleteView'),     #переход к форме для удаления Жанра по его РК
    # path('author-delete/<int:pk>', views.AuthorDeleteView.as_view(), name='AuthorDeleteView'),     #переход к форме для удаления Автора по его РК
    # path('series-delete/<int:pk>', views.SeriesDeleteView.as_view(), name='SeriesDeleteView'),     #переход к форме для удаления Серии по его РК
    # path('publish-delete/<int:pk>', views.PublishDeleteView.as_view(), name='PublishDeleteView'),     #переход к форме для удаления Издательсвт по его РК
    
]
