from django.db import models
from django.conf import settings  # استيراد settings

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)  # تحديث العلاقة
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title