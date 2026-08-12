from urllib import request
from django.shortcuts import render

from django.shortcuts import render

def home(request):
    return render(request, 'base.html')

def verses(request):
    return render(request, 'verses.html')

def mawlid(request):
    return render(request, 'mawlid.html')

def seerah(request):
    return render(request, 'seerah.html')

def sahaba(request):
    return render(request, 'sahaba.html')

def ahlalbayt(request):
    return render(request, 'ahlalbayt.html')

def hadith(request):
    return render(request, 'hadith.html')

def videos(request):
    return render(request, 'videos.html')  
