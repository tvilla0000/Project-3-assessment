from django.db import models

# Create your models here.

class Widget(models.Model):
  description = models.CharField(max_length=20)
  quantity = models.IntegerField(blank=False)

  def __str__(self):
    return f"{self.id} - {self.name}, {self.element}"