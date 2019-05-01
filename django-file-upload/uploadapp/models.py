from django.db import models

class Photo(models.Model):
    photo = models.ImageField(blank=False, null=False)
    caption = models.TextField(null=True)

    def __str__(self):
        return self.photo.name

class Comment(models.Model): 
    comment = models.CharField(max_length=200,default='')
    photoID = models.IntegerField(default=0)
    
    def __str__(self):
        return self.comment

class Emoji(models.Model):
    emoji = models.CharField(max_length=200,default='')
    photoID = models.IntegerField(default=0)

    def __str__(self):
        return self.emoji
