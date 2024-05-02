from django.contrib import admin
from .models import BlogPost, BlogImage

# Register your models here.


class BlogImageInline(admin.StackedInline):
    model = BlogImage
    extra = 2


class BlogPostAdmin(admin.ModelAdmin):
    inlines = [BlogImageInline]


admin.site.register(BlogPost, BlogPostAdmin)
