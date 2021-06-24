from django.contrib import admin
from .models import Post,Comment,Category

# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id','title']

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['id','author']

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id','name']
