from django.shortcuts import render
# from django.contrib.auth.models import User
# from django.contrib.auth import login,logout,authenticate 
from .models import Post



def HomePage(request):
   Posts = Post.objects.all()
   return render (request,'index.html',{'posts':Posts})

#
# def ContactPage(request):
#     contact= Contact()
#     if request.method =="POST":
#         contact.username =request.POST.get('fullName')
#         contact.email =request.POST.get('email')
#         contact.phone_numer =request.POST.get('phone')
#         contact.message =request.POST.get('message')
#         return redirect('home')
    
#     return render(request,'contact.html')

def PostDatail(request):
    Posts = Post.objects.all()
    return render(request,'post_detaol.html',{"post":Posts})



# def SignupPage(request):

#     if request.method == 'POST':
#       user=User()
#       username = request.POST.get('name')
#       useremail = request.POST.get('email')
#       if request.POST.get('parol') == request.POST.get('parol2'):
#           password = request.POST.get('parol2')
#           user=User.objects.create_user(username=username,email=useremail,password=password)

#           login(request,user)
#           return redirect('home')
      
#     return render (request,'signup.html')

# def loginPage(request):
#     if request.method =='POST':
#         username = request.POST.get('name')
#         password = request.POST.get(' password')
#         user= authenticate(request,username=username,password=password)

#         if user is not None:
#             login(request,user)
#             return redirect('home')

#     return render(request,'login.html')


# def LogoutUser(request):
#     logout(request)
#     return redirect('home')

# def AboutPage(request):

#  return render(request,'about.html')


# def category_post(request, slug):
#     object_list = Post.objects.filter(category__slug = slug)
#     cat = Category.objects.get(slug=slug)
  
#     return render(request, "post_list.html", {'posts':object_list,'cat':cat})


