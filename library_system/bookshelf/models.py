from django.db import models

class Bookshelf(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)  # حقل الوصف

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    bookshelf = models.ForeignKey(Bookshelf, related_name='books', on_delete=models.CASCADE)

    def __str__(self):
        return self.title