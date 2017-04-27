from django.shortcuts import render
from .models import Word

def index(request):
    return render(request, 'index.html')

def wordCloud(request):
    w_list = Word.objects.all()
    context = {'word_list':w_list}
    return render(request, 'wordCloud.html', context)
