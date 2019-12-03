from django.shortcuts import render, render_to_response, get_object_or_404

# Create your views here.
from django.http import Http404

from blog.forms import CommentForm
from blog.models import Blog, Comment


def get_blogs(request):
    try:
        blogs = Blog.objects.all().order_by('-created')
    except Blog.DoesNotExist:
        raise Http404('Blog does not exist')

    return render(request, 'blogs/index.html', {'blogs': blogs})


def get_details(request, blog_id):

    blog = get_object_or_404(Blog, id=blog_id)

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            cleaned_data['blog'] = blog
            Comment.objects.create(**cleaned_data)
    else:
        form = CommentForm()

    content = {
        'blog': blog,
        'comments': blog.comment_set.all().order_by('-created'),
        'form': form
    }
    return render(request, 'blogs/detail.html', content)
