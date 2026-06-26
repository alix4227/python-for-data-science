from django.shortcuts import render, redirect
from django.views.generic import *
from .models import *
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.contrib.auth.views import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import *
from .forms import *
from django.contrib.auth.mixins import LoginRequiredMixin

class Display(ListView):
    model = Articles
    context_object_name = "articles_objects"
    template_name = "display.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["headers"] = [f.name for f in Articles._meta.fields if not f.name == 'content']
        return context

class ArticleCreateView(LoginRequiredMixin,CreateView):
    
    model = Articles
    fields = ['title', 'synopsis', 'content']
    template_name = 'article_creation.html'
    success_url = reverse_lazy('display')
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class UserCreationView(CreateView):
    model = User
    form_class = UserCreationForm
    template_name = 'user_creation.html'
    success_url = reverse_lazy('login')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form_register"] = UserCreationForm
        return context

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

class Detail(LoginRequiredMixin, DetailView):
    model = Articles
    context_object_name = "item"
    template_name = 'detail.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["headers"] = [f.name for f in Articles._meta.fields]
        return context
    

class Logout(TemplateView):
    def get(self, request, **kwargs):
        logout(self.request)
        return redirect('home')

class Favourites(ListView):
    model = UserFavouriteArticle
    context_object_name = "favourites"
    template_name = "favourites.html"
    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(user=self.request.user)

class FavouriteCreateView(LoginRequiredMixin, TemplateView):
    def get(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        return redirect('detail', pk=pk)
    def post(self, request, *args, **kwargs):
        article = Articles.objects.get(pk=request.POST.get('article'))
        UserFavouriteArticle.objects.get_or_create(user=request.user, article=article)
        return redirect('favourites')