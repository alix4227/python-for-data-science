from django.shortcuts import render
from django.views.generic import *
from .models import Articles
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.contrib.auth.views import *
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import *
from .forms import *


class Display(ListView):
    model = Articles
    context_object_name = "articles_objects"
    template_name = "display.html"
    # def get_queryset(self):
    #     return Articles.objects.filter("author"='CRUSOE')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["headers"] = [f.name for f in Articles._meta.fields if not f.name == 'content']
        return context


class ArticleCreateView(CreateView):
    model = Articles
    fields = ['title', 'author', 'synopsis', 'content']
    template_name = 'article_creation.html'
    success_url = reverse_lazy('display')


class UserCreationView(CreateView):
    model = User
    form_class = UserCreationForm
    template_name = 'user_creation.html'
    success_url = reverse_lazy('login')

class Login(FormView):
    model = User
    form_class = AuthenticationForm
    template_name = 'login.html'
    success_url = reverse_lazy('home')
    def form_valid(self, form):
        login(self.request, form.get_user())
        return super().form_valid(form)

class Home(RedirectView):
    pattern_name = 'display'

class Publications(ListView):
    model = Articles
    context_object_name = "articles_objects"
    template_name = "publications.html"
    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(author=self.request.user)
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["headers"] = [f.name for f in Articles._meta.fields if f.name not in ('content', 'id', 'author')]
        return context

class Detail(DetailView):
    model = Articles
    context_object_name = "item"
    template_name = 'detail.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["headers"] = [f.name for f in Articles._meta.fields]
        return context