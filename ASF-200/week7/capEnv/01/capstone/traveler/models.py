from django.db import models

# Create your models here.
class Location(models.Model):
    text = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    via = models.URLField(blank=True)

    def total_likes(self):
        return self.like_set.count()

    def __str__(self):
        return self.text[:25]

class Like(models.Model):
    location= models.ForeignKey(Location, on_delete = models.CASCADE)


