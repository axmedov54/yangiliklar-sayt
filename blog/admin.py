from django.contrib import admin
from .models import Post,Contact,Category,CommentPost


admin.site.register(Category)
admin.site.register(Contact)
admin.site.register(CommentPost)



@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'created', 'status')  
    list_filter = ('status',) 
    search_fields = ('title', 'body') 
    prepoplated_files={'slug':('title',)}


# @admin.register(Category)
# class CategoryPage(admin.ModelAdmin):
#     list_display=('name',)
#     prepoplated_files={'slug':('name',)}


    
