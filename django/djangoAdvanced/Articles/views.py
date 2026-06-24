from django.shortcuts import render
from django.views.generic import *
from .models import Articles
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .forms import *


class ArticlesView(ListView):
    model = Articles
    context_object_name = "articles_objects"
    template_name = "display.html"
    # def get_queryset(self):
    #     return Articles.objects.filter("author"='CRUSOE')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["headers"] = [f.name for f in Articles._meta.fields]
        return context


class ArticleCreateView(CreateView):
    model = Articles
    fields = ['title', 'author', 'synopsis', 'content']
    template_name = 'index.html'
    success_url = reverse_lazy('display')


class UserCreationView(CreateView):
    model = User
    form_class = UserCreationForm
    template_name = 'index.html'
    success_url = reverse_lazy('index')

class Login(FormView):
    model = User
    form_class = AuthenticationForm
    template_name = 'index.html'
    success_url = reverse_lazy('display')