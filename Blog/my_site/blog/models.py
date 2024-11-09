from django.contrib.auth.models import User
from django.db import models
from django.db.models import Model
from django.urls import reverse
from django.utils import timezone
from taggit.managers import TaggableManager
from unidecode import unidecode


# Create your models here.
class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status=Post.Status.PUBLISHED)
class Post(models.Model):
    class Status(models.TextChoices):
        DRAFT = 'DF', 'Draft'
        PUBLISHED = 'PB', 'Published'

    objects = models.Manager()
    published = PublishedManager()
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique_for_date='publish')
    text = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=2, choices=Status.choices, default=Status.DRAFT)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    tags = TaggableManager()
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('blog:detail_post', args=[
            self.publish.year,
            self.publish.month,
            self.publish.day,
            self.slug
        ])
    class Meta:
        ordering = ['-publish']
        indexes = [
            models.Index(fields=['-publish']),
        ]

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments_auth')
    text = models.TextField(max_length=10000)
    create_data = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f'Комментарий от пользователя {self.author}: {self.text[:15]}'
    class Meta:
        ordering = ['-create_data']
        indexes = [
            models.Index(fields=['create_data']),
        ]
