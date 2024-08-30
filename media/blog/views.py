from django.shortcuts import render,redirect
from django.contrib.auth.models import User 
from .models import Post


def HomePage(request):
    Posts = Post.objects.all()
    return render (request,'index.html',{'posts':Posts})



def PostDatail(request,id=id):
    Posts = Post.objects.get(id=id)
    return render(request,'post_detali.html',{"post":Posts})



def SinupPage(request):
    user = User()
    if request.method == 'POST':
      user.first_name  = request.POST.get('name')
      user.email = request.POST.get('email')
      if request.POST.get('parol') ==request.POST.get('parol2'):
          user.password = request.POST.get('parol')
          user.save()
          return redirect('home')
      
    return render (request,'signup.html')