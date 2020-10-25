from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'index.html')

def eventIntro(request):
    return render(request, 'eventIntro.html')

def event1(request):
    return render(request, 'event1.html')

def event2(request):
    return render(request, 'event2.html') 
