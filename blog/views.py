from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

posts = [{'author': 'Jeisa Raja',  'datePosted' : 'June 30', 'content' : 'ini buat jobdesc nya barangkali lupa', 'title': 'Reminder'},
         {'author' : 'Azriel', 'datePosted' : 'June 25', 'content' : 'dikit lgi guys abis itu kelar kok gak bakal gw panggil panggilin lagi', 'title': 'semangat!'}]
# Create your views here.
# context = {'posts': posts}
context = {'posts': Post.objects.all()}
def home(request):
    #return HttpResponse('<h1>Project_0 Blog</h1>')

    return render(request,'blog/home.html',context)

def about(request):
    #return HttpResponse('<h1>This is About Our Blog</h1>')
    return render(request, 'blog/about.html')
