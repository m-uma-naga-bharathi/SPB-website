from multiprocessing import context
from urllib import request
from urllib import request
from django.shortcuts import render
from .models import FeedBack, Song, Year
from django.contrib import messages
from django.db.models import Q

def home(request):
    return render(request, 'menu.html')

def trail1(request):
    return render(request, 'trail1.html')

def trail2(request):
    return render(request, 'trail2.html')

def trail3(request):
    return render(request, 'trail3.html')

def trail4(request):
    return render(request, 'trail4.html')

def trail6(request):
    return render(request, 'trail6.html')

def trail7(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    songs = Song.objects.filter(
        Q(name__icontains=q) |
        Q(year__year__icontains=q)
        )
    years = Year.objects.all()
    print(years)
    context = {'songs':songs, 'years':years}
    return render(request, 'trail7.html',context)

def trail5(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        feed = request.POST.get('feed')

        new_feed = FeedBack.objects.create(name=name,email=email,phone=phone,feed=feed)
        new_feed.save()
        messages.success(request, 'Feedback Successfully Submitted')

    return render(request, 'trail5.html')



