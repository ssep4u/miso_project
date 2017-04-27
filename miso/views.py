from django.shortcuts import render, redirect
from django.utils import timezone
from django.db.models import Count
from .models import Word
from .forms import WordForm
import datetime

def index(request):
    return render(request, 'index.html')

def wordCloud(request):
    w_list = Word.objects.all()
    w_count = Word.objects.values('word').annotate(weight=Count('word'))
    context = {'word_list':w_list, 'word_count':w_count}
    return render(request, 'wordCloud.html', context)

def wordForm(request):
    if request.method == "POST":
        form = WordForm(request.POST)
        if form.is_valid():
            newWord = Word()
            newWord.word = form.cleaned_data['word']
            newWord.date = timezone.localtime(timezone.now())
            newWord.save()
            return redirect('wordCloud')
    else:
        form = WordForm()
        context = {'form':form}

    return render(request, 'wordForm.html', context)
