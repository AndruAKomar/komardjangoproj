from django.urls import path
from . import views

app_name='reference'
urlpatterns = [
    path('genre/<int:pk>', views.GenreView.as_view(), name='GenreView'),   #переход к конкретному объекту/деталям Жанра по его РК
    path('genre-list/', views.GenreListView.as_view(), name='GenreListView'),     #переход к просмотру всех объектов Жанра
    path('genre-add/', views.GenreCreateView.as_view(), name='GenreCreateView'),        #переход к форме для добавления нового Жанра
    path('genre-upd/<int:pk>', views.GenreUpdateView.as_view(), name='GenreUpdateView'),        #переход к форме для редактирования Жанра по его РК
    path('genre-delete/<int:pk>', views.GenreDeleteView.as_view(), name='GenreDeleteView'),     #переход к форме для удаления Жанра по его РК
    # path('author/<int:pk>', views.AuthorView.as_view(), name='AuthorView'),     #переход к просмотру всех объектов Авторов
]
