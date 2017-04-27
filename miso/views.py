from django.shortcuts import render, redirect
from django.utils import timezone
from .models import Word
from .forms import WordForm

def index(request):
    return render(request, 'index.html')

def wordCloud(request):
    w_list = Word.objects.all()
    context = {'word_list':w_list}
    return render(request, 'wordCloud.html', context)

def wordForm(request):
    if request.method == "POST":
        form = WordForm(request.POST)
        if form.is_valid():
            newWord = form.save(commit=False)
            newWord.date = timezone.now()
            newWord.save()
            return redirect('wordCloud')
    else:
        form = WordForm()
        context = {'form':form}

    return render(request, 'wordForm.html', context)
