from django.urls import path
from films import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('login/', views.Login.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path("register/", views.RegisterView.as_view(), name="register"),
    path("movies/", views.MovieList.as_view(), name="movie-list"),
]

htmx_urlpatterns = [
    path('check_username/', views.check_username, name='check-username'),
    path('add_movie/', views.add_movie, name='add-movie'),
    path('delete_movie/<int:pk>/', views.delete_movie, name='delete-movie'),
]

urlpatterns += htmx_urlpatterns