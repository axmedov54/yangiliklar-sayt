from django.urls import path 
from .views import *

urlpatterns=[
    path('',HomePage,name='home'),
    path('post/',PostDatail,name='postd'),
    # path('<int:year>/<int:month>/<int:day>/<slug:slug>/',PostDatail,name='post_detali'),
    # path('signup/',SignupPage,name='signup'),
    # path('logout/',LogoutUser,name="logout"),
    # path('login/',loginPage,name='login'),
    # path('contact/',ContactPage,name='contact'),
    # path('about/',AboutPage,name='about'),
    # path('category/<slug:slug>/',category_post,name='category_post')
    
]
