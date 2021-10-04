from django.db import models


class Women(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/")
    time_create = models.DateTimeField(auto_now_add=True)  # Один раз ставиться і не міняється
    time_update = models.DateTimeField(auto_now=True)  # Міняється кожен раз
    is_published = models.BooleanField(default=True)

    def __str__(self):
        return self.title