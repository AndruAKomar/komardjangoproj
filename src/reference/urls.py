from django.urls import path
from . import views

app_name='reference'
urlpatterns = [
    path('reference-list/', views.ReferenceListView.as_view(), name='ReferenceListView'),     #переход к просмотру всех справочников
    
    path('genre/<int:pk>', views.GenreView.as_view(), name='GenreView'),   #переход к конкретному объекту/деталям Жанра по его РК
    path('author/<int:pk>', views.AuthorView.as_view(), name='AuthorView'),     #переход к просмотру всех объектов Авторов
    path('series/<int:pk>', views.SeriesView.as_view(), name='SeriesView'),     #переход к просмотру всех объектов Серии
    path('publish/<int:pk>', views.PublishView.as_view(), name='PublishView'),     #переход к просмотру всех объектов Издательст
    path('status/<int:pk>', views.StatusView.as_view(), name='StatusView'),     
        
    path('genre-add/', views.GenreCreateView.as_view(), name='GenreCreateView'),        #переход к форме для добавления нового Жанра
    path('author-add/', views.AuthorCreateView.as_view(), name='AuthorCreateView'),        #переход к форме для добавления Авторов 
    path('series-add/', views.SeriesCreateView.as_view(), name='SeriesCreateView'),        #переход к форме для добавления Серии 
    path('publish-add/', views.PublishCreateView.as_view(), name='PublishCreateView'),        #переход к форме для добавления Издательства 
    path('status-add/', views.StatusCreateView.as_view(), name='StatusCreateView'),       
    
    path('genre-upd/<int:pk>', views.GenreUpdateView.as_view(), name='GenreUpdateView'),        #переход к форме для редактирования Жанра по его РК
    path('author-upd/<int:pk>', views.AuthorUpdateView.as_view(), name='AuthorUpdateView'),        #переход к форме для редактирования Авторов по его РК
    path('series-upd/<int:pk>', views.SeriesUpdateView.as_view(), name='SeriesUpdateView'),        #переход к форме для редактирования Серии по его РК
    path('publish-upd/<int:pk>', views.PublishUpdateView.as_view(), name='PublishUpdateView'),        #переход к форме для редактирования Издательст по его РК
    path('status-upd/<int:pk>', views.StatusUpdateView.as_view(), name='StatusUpdateView'),       
    
    path('genre-delete/<int:pk>', views.GenreDeleteView.as_view(), name='GenreDeleteView'),     #переход к форме для удаления Жанра по его РК
    path('author-delete/<int:pk>', views.AuthorDeleteView.as_view(), name='AuthorDeleteView'),     #переход к форме для удаления Автора по его РК
    path('series-delete/<int:pk>', views.SeriesDeleteView.as_view(), name='SeriesDeleteView'),     #переход к форме для удаления Серии по его РК
    path('publish-delete/<int:pk>', views.PublishDeleteView.as_view(), name='PublishDeleteView'),     #переход к форме для удаления Издательсвт по его РК
    path('status-delete/<int:pk>', views.StatusDeleteView.as_view(), name='StatusDeleteView'),     
    
]
