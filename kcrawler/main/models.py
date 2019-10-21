from django.db import models
from django.utils import timezone

# Create your models here.
class EntryItem(models.Model):
    id = models.AutoField(primary_key=True)
    keyword = models.CharField(max_length=40)
    date = models.DateTimeField(default = timezone.now)

    def __str__(self):
        return str(self.id) + ' ' + self.keyword

class ArticleItem(models.Model):
    entry = models.ForeignKey(EntryItem, on_delete=models.CASCADE, related_name="enteredBy")
    url = models.CharField(max_length=200)
    headline = models.CharField(max_length=100)

    def __str__(self):
        return str(self.entry) + ' ' + self.headline

