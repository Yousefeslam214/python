from django.db import models


# A model is a table. Each attribute below is a column.
# In the database the tables are called posts_topic and posts_post.


class Topic(models.Model):
    name = models.CharField(max_length=50)    # short text, at most 50 characters

    # How a topic shows up in the admin and in the shell.
    def __str__(self):
        return self.name


class Post(models.Model):
    # A foreign key: each post belongs to one topic,
    # like orders.customer_id in Session 2.
    # on_delete=models.CASCADE: delete a topic and its posts are deleted too.
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()                                # long text
    created_at = models.DateTimeField(auto_now_add=True)     # filled in automatically

    def __str__(self):
        return self.text[:40]    # the first 40 characters
