from django.urls import path

from . import views

# Which view runs for which URL.
urlpatterns = [
    path("", views.post_list),              # http://127.0.0.1:8000/
    path("hello/", views.hello),            # http://127.0.0.1:8000/hello/
    path("api/posts/", views.api_posts),    # http://127.0.0.1:8000/api/posts/
]
