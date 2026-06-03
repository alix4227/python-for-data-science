from django.shortcuts import render

def django(request):
    title = 'Presentation Django'
    return render(request, 'ex01/django.html', {"title": title})

def affichage(request):
    title = 'Processus d\'affichage d\'une page statique'
    return render(request, 'ex01/affichage.html', {"title": title})

def templates(request):
    title = 'Processus d\'affichage'
    return render(request, 'ex01/templates.html', {"title": title})