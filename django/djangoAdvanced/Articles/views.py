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
from django.utils import timezone, translation
from django.utils.translation import gettext as _
from django.http import *


# def handler404(request, exception):
#    return render(request, '404handler.html')

class Display(ListView):
    model = Articles
    context_object_name = "articles_objects"
    template_name = "display.html"
    ordering = ['-created']
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        now = timezone.now()
        for article in context["articles_objects"]:
            delta = now - article.created
            article.when = str(delta).split('.')[0]
        context["headers"] = [_("ID"),_("titre"), _("auteur"), _("créé le"), _("synopsis"), _("Cree il y a")]
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
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            raise Http404
        return super().dispatch(request, *args, **kwargs)

class Login(FormView):
    model = User
    form_class = CustomAuthenticationForm
    template_name = 'login.html'
    success_url = reverse_lazy('home')
    def form_valid(self, form):
        login(self.request, form.get_user())
        return super().form_valid(form)
    

class Home(RedirectView):
    pattern_name = 'display'

class Publications(LoginRequiredMixin, ListView):
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

class Favourites(LoginRequiredMixin, ListView):
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
        already_favourite = UserFavouriteArticle.objects.filter(user=request.user, article=article).exists()
        if already_favourite: 
            return render(request, "favourite_already_exists.html", status=400)
        UserFavouriteArticle.objects.create(user=request.user, article=article)
        return redirect('favourites')