from django.contrib import admin
from .models import Post


admin.site.register(Post)




# @admin.register(Category)
# class CategoryPage(admin.ModelAdmin):
#     list_display=('name',)
#     prepoplated_files={'slug':('name',)}


    
