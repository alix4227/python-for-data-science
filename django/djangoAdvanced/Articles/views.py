from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView

class articlesView(ListView):
    model = Articles
    context_object_name = "articles_objects"
    template_name = "Articles/index.html"
    
    # def get_queryset(self):
    #     return Articles.objects.filter("author"='CRUSOE')