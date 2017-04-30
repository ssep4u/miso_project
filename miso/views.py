from django.shortcuts import render, redirect
from django.utils import timezone
from django.db.models import Count
from .models import Word
from .forms import WordForm
import datetime

def index(request):
    return render(request, 'index.html')


def wordForm(request):
    if request.method == "POST":
        form = WordForm(request.POST)
        if form.is_valid() and isValid(form.cleaned_data['word']):
            newWord = Word()
            newWord.word = form.cleaned_data['word']
            newWord.date = timezone.localtime(timezone.now())
            newWord.save()
            return redirect('wordCloud')
    else:
        form = WordForm()
        context = {'form':form}

    return render(request, 'wordForm.html', context)

def wordCloud(request):
    special_word = '미소'

    w_count = Word.objects.values('word').annotate(weight=Count('word'))
    context = {'word_count':w_count, 'special_word':special_word}
    return render(request, 'wordCloud.html', context)

def isValid(word):
    quiz = 'ㅁㅅ'

    if len(word) != len(quiz):
        return False

    i=0
    correct=0
    for letter in word:
        if isJaeumToLetter(quiz[i], letter):
            correct+=1
        i+=1

    if correct==len(quiz):
        return True
    else:
        return False

    def isJaeumToLetter(jaeum, letter):
        if jaeum=='ㄱ' and ('가' <= letter and letter <= '깋'):
            return True
        elif jaeum=='ㄴ' and ('나' <= letter and letter <= '닣'):
            return True
        elif jaeum=='ㄷ' and ('다' <= letter and letter <= '딯'):
            return True
        elif jaeum=='ㄹ' and ('라' <= letter and letter <= '맇'):
            return True
        elif jaeum=='ㅁ' and ('마' <= letter and letter <= '밓'):
            return True
        elif jaeum=='ㅂ' and ('바' <= letter and letter <= '빟'):
            return True
        elif jaeum=='ㅅ' and ('사' <= letter and letter <= '싷'):
            return True
        elif jaeum=='ㅇ' and ('아' <= letter and letter <= '잏'):
            return True
        elif jaeum=='ㅈ' and ('자' <= letter and letter <= '짛'):
            return True
        elif jaeum=='ㅊ' and ('차' <= letter and letter <= '칳'):
            return True
        elif jaeum=='ㅋ' and ('카' <= letter and letter <= '킿'):
            return True
        elif jaeum=='ㅌ' and ('타' <= letter and letter <= '팋'):
            return True
        elif jaeum=='ㅍ' and ('파' <= letter and letter <= '핗'):
            return True
        elif jaeum=='ㅎ' and ('하' <= letter and letter <= '힣'):
            return True
        else:
            return False
