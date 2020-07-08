from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


class Post(models.Model):
    # This will render in the 'category' post form field.
    POST_CATEGORIES = [
        ('none', 'None'),
        ('racial equality', 'Racial Equality'),
        ('police reform', 'Police Reform'),
        ('gender equality', 'Gender Equality'),
        ('relogion', 'Religion')
    ]

    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.CharField(max_length=100, choices=POST_CATEGORIES, default='None')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author = models.CharField(max_length=80)
    body = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)
    approved_comments = models.BooleanField(default=False)

    def approve(self):
        self.approved_comments = True
        self.save()

    def __str__(self):
        return 'Comment {} by {}'.format(self.body, self.name)
