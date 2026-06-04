from django.shortcuts import render

def gradient(request):
    title = 'Gradient'
    return render(request, 'ex03/gradient.html', {"title": title, "range": range(50), "rgb": "rgb(0,0,0)"})
