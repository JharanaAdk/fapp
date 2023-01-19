from django.db import models

# Create your models here.
class demo(models.Model):
    name = models.CharField(max_length=150)
    age = models.IntegerField()
    time = models.TimeField(auto_now_add=True)
    date = models.DateField(auto_created=True)
    description = models.TextField(max_length=500)
    slug = models.SlugField()
    number = models.PositiveIntegerField()
    number2 = models.IntegerField()

    def __str__(self):
        return self.slug
# user decription model
#books