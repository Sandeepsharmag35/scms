from django.shortcuts import render, get_object_or_404
from .models import BlogPost, BlogImage
from app.models import Info, Course

# Create your views here.


def blog(request):
    blogs = BlogPost.objects.all().order_by("-created_at")

    info = Info.objects.first()
    courses = Course.objects.all()

    context = {
        "blogs": blogs,
        "info": info,
        "courses": courses,
    }
    return render(request, "blog.html", context)


def blogDetails(request, blog_slug):
    single_blog = get_object_or_404(BlogPost, slug=blog_slug)
    blog_images = BlogImage.objects.filter(blog=single_blog)

    info = Info.objects.first()
    courses = Course.objects.all()

    context = {
        "blog": single_blog,
        "blog_images": blog_images,
        "info": info,
        "courses": courses,
    }
    return render(request, "blog-details.html", context)
