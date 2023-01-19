from django.contrib import admin

# Register your models here.
from .models import Post, Comment

class CommentInLine(admin.StackedInline):
    model = Comment 

class PostAdmin(admin.ModelAdmin):
    inlines = [
        CommentInLine,
    ]

admin.site.register(Post, PostAdmin)
admin.site.register(Comment)