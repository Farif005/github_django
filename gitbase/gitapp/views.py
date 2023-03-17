from django.shortcuts import render, redirect
from .models import *
from .form import *


def index(request):
    news = News.objects.all()
    context = {'news': news}
    return render(request, 'gitapp/index.html', context)

def newsform(request):

    if request.method == 'POST':
        form = NewsForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('succes')
    else:
        form = NewsForm()
    return render(request, 'gitapp/form.html', {'form': form})

def succes(request):
    return render(request, 'gitapp/succes.html')