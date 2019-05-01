from django.urls import path
from . import views

urlpatterns = [
    path('addPhoto/', views.PhotoUploadView.as_view()),
    path('getPhoto/', views.PhotoList.as_view()),
    path('addComment/', views.CommentUploadView.as_view()),
    path('getComment/', views.CommentList.as_view()),
    path('addEmoji/', views.EmojiUploadView.as_view()),
    path('getEmoji/', views.EmojiList.as_view()),
]