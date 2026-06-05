from django.shortcuts import render

def gradient(request):
    title = 'Gradient'
    table = []
    j = 255
    b = 0

    for i in range(50):
        table.append([f"rgb({b}, {b}, {b})", f"rgb({j}, 0, 0)", f"rgb({b}, 0, {j})", f"rgb(0, {j}, {b})"])
        j -= 4
        b += 4
    return render(request, 'ex03/gradient.html', {"title": title, "table": table})
