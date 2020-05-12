from django.db import models
from django.utils import timezone

class Author(models.Model):
    name = models.CharField(max_length=255)
    def __str__(self):
        return self.name

class Category(models.Model):
    category = models.CharField(max_length=255)
    def __str__(self):
        return self.category


class Article(models.Model):
    title = models.CharField(max_length=255)
    status = models.CharField(max_length=10, choices=[('D', 'draft'), ('P', 'published')])
    content = models.TextField()
    publication_date = models.DateTimeField(default=timezone.now)
    category = models.ForeignKey(Category, null=True, default=None, on_delete=models.CASCADE)
    author = models.ForeignKey(Author, null=True, default=None, on_delete=models.CASCADE, related_name='articles')

    def __str__(self):
        return self.title




