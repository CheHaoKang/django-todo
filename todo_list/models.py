from django.db import models

class List(models.Model):
    item = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)
    document = models.FileField(upload_to='documents/', null=True, blank=True)

    def __str__(self):
        return self.item
