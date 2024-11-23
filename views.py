from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def education(request):
    return render(request, 'education.html')

def work(request):
    return render(request, 'work.html')

def profile(request):
    return render(request, 'profile.html')