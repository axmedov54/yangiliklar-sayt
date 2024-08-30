from django.db import models
from django.utils import timezone

class Post(models.Model):
    STATUS_CHOICE=(
        ('draft','draft'),
        ('published','Published'),
    )
    title=models.CharField(max_length=200)
    image=models.ImageField(upload_to='image/post')
    body=models.TextField()
    publish=models.DateTimeField(default=timezone.now)
    created=models.DateField(auto_now_add=True)
    update=models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=10,choices=STATUS_CHOICE,default='draft')

    class Meta:
        ordering=('-publish',)


    def __str__(self):
        return self.title
