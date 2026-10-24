# The main list of URLs for the whole project.
# Django checks the patterns from top to bottom and uses the first one that matches.
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),    # the admin back office
    path("", include("posts.urls")),    # every other URL: look in posts/urls.py
]
