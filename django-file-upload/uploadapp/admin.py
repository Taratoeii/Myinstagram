from django.contrib import admin

from .models import Photo, Comment, Emoji

admin.site.register(Photo)
admin.site.register(Comment)
admin.site.register(Emoji)
# Register your models here.
