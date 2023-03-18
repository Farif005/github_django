from django.shortcuts import render, redirect
from .models import *
from .form import *

genres = Genre.objects.all()

def index(request):
    news = News.objects.all()
    context = {'news': news, 'genres': genres}
    return render(request, 'gitapp/index.html', context)

def genredef(request, genre_id):
    news = News.objects.filter(genre=genre_id)
    current_genre = Genre.objects.get(pk=genre_id)
    context = {'news': news, 'current_genre': current_genre, 'genres': genres}
    return render(request, 'gitapp/genre.html', context)

def newsform(request):

    if request.method == 'POST':
        form = NewsForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('succes')
    else:
        form = NewsForm()
    
    context = {'form': form, 'genres': genres}
    return render(request, 'gitapp/form.html', context)

def succes(request):
    return render(request, 'gitapp/succes.html')