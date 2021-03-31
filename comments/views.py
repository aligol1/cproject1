from django.shortcuts import render
from .models import Post
from .utils import create_comments_tree


def base_view(request):
    comments = Post.objects.first().comments.all()
    result = create_comments_tree(comments)
    print(result)
    for res in result:
        print(res)
    return render(request, 'base.html', {'comments': comments})

