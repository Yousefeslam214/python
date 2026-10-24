from django.contrib import admin

from .models import Post, Topic


# The columns the admin shows in the list of posts.
class PostAdmin(admin.ModelAdmin):
    list_display = ["text", "topic", "created_at"]


admin.site.register(Topic)
admin.site.register(Post, PostAdmin)
