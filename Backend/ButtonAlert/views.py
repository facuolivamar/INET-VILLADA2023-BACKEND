from django.shortcuts import render

# Create your views here.
# chat/views.py


def index(request):
    return render(request, "index.html")
