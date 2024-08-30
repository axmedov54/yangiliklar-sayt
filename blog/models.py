from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=200)
    slug= models.SlugField(max_length=200,unique=True)
    
    
    def __str__(self) -> str:
        return self.name

    def get_absolute_url(self):
        return reverse('category_post', args=[self.slug])   
    
class Publishmeneger(models.Manager):
    def get_queryset(self) -> models.QuerySet:
        return super(Publishmeneger,self).get_queryset().filter(status='published')







# class Post(models.Model):
#     STATUS_CHOICES=(
#         ('draft','Draft'),
#         ('published','Published'),
#     )
#     title=models.CharField(max_length=200)
#     slug= models.SlugField(max_length=200,unique_for_date='publish',null=True)
#     category=models.ForeignKey(to = Category,on_delete=models.CASCADE,null=True)
#     author =models.ForeignKey(to=User,on_delete=models.CASCADE,name=True)
#     body=models.TextField()
#     publish=models.DateTimeField(default=timezone.now)
#     created=models.DateField(auto_now=True)
#     update=models.DateTimeField(auto_now=True)
#     status = models.CharField(max_length=10,choices=STATUS_CHOICES,default='draft')
#     objects=models.Manager()
#     published=Publishmeneger()

#     class Meta:
#         ordering=('-publish',)

#     def __str__(self):
#         return self.title
    
    
    
class Post(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published')
    )
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=250, unique_for_date='publish')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    photo = models.ImageField(upload_to='photo/post', null=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="blog_posts")
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')
    objects = models.Manager()  # defoult manager
    published = Publishmeneger() # published manajer yangiliklarni qayataradi

    class Meta:
        ordering = ('-publish',)


    def get_absolute_url(self):
        return reverse('post_detali', args=[self.publish.year, self.publish.month, self.publish.day, self.slug])    


class CommentPost(models.Model):
    author = models.CharField(max_length=50)
    post= models.CharField(max_length=50)
    comment=models.TextField()
    crated= models.DateField(auto_now_add=True)
    
    
    
    def __str__(self) -> str:
        return f'{self.author} -> {self.crated}'
    
    
class Contact(models.Model):
    username = models.CharField(max_length=50)
    email= models.EmailField(max_length=50)
    phone_numer = models.CharField(max_length=15)
    message = models.TextField()
    
    
    def __str__(self) -> str:
        return  self.username    