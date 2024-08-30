from django.contrib import admin
from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'created', 'status')  
    list_filter = ('status',) 
    search_fields = ('title', 'body') 
