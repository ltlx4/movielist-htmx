from django.http.response import HttpResponse
from django.shortcuts import render
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views.generic import FormView, TemplateView
from django.views.decorators.http import require_http_methods
from django.views.generic.list import ListView
from django.contrib.auth import get_user_model
from .models import Movie
from films.forms import RegisterForm

# Create your views here.
class IndexView(TemplateView):
    template_name = 'index.html'
    
class Login(LoginView):
    template_name = 'registration/login.html'

class RegisterView(FormView):
    form_class = RegisterForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        form.save()  # save the user
        return super().form_valid(form)


class MovieList(ListView):
    model = Movie
    template_name = 'movie.html'
    context_object_name = 'movies'

    def get_queryset(self):
        user = self.request.user
        return user.movies.all()

def check_username(request):
    username = request.POST.get('username')
    if get_user_model().objects.filter(username=username).exists():
        return HttpResponse("<div id='username-error' class='error'>This username already exists</div>")
    else:
        return HttpResponse("<div id='username-error' class='success'>This username is available</div>")

def add_movie(request):
    name = request.POST.get('moviename')
    movie = Movie.objects.create(name=name)
    
    request.user.movies.add(movie)

    movies = request.user.movies.all()

    return render(request, 'partials/movie_list.html', {'movies': movies})


@require_http_methods(['DELETE'])
def delete_movie(request, pk):
    request.user.movies.remove(pk)
    movies = request.user.movies.all()
    return render(request, 'partials/movie_list.html', {'movies': movies})

