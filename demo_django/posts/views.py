from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

from .models import Post

# A view is a Python function. Django gives it the request,
# and the view gives back a response.


# 1. The simplest view: no database, no template. Just text.
def hello(request):
    return HttpResponse("Hello from Django!")


# 2. A page: get the posts from the database and put them into a template.
def post_list(request):
    posts = Post.objects.order_by("-created_at")    # newest first: ORDER BY created_at DESC
    return render(request, "posts/post_list.html", {"posts": posts})


# 3. An API: the same posts as JSON, for other programs.
#    React (Session 4) and n8n (Session 6) will read this.
def api_posts(request):
    data = []
    for post in Post.objects.order_by("-created_at"):
        data.append({
            "id": post.id,
            "topic": post.topic.name,
            "text": post.text,
            "created_at": post.created_at.isoformat(),
        })
    return JsonResponse({"posts": data})
