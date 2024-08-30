from django.urls import path 
from .views import HomePage,PostDatail,SinupPage

urlpatterns=[
    path('',HomePage,name='home'),
    path('post/<int:id>/',PostDatail,name='post_detali'),
    path('signup/',SinupPage,name='signup')
]
