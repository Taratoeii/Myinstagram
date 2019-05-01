from rest_framework.parsers import FileUploadParser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework import generics
from .serializers import PhotoSerializer,CommentSerializer,EmojiSerializer
from .models import Photo,Comment,Emoji

class PhotoUploadView(APIView):
    parser_class = (FileUploadParser,)

    def post(self, request, *args, **kwargs):

      photo_serializer = PhotoSerializer(data=request.data)

      if photo_serializer.is_valid():
          photo_serializer.save()
          return Response(photo_serializer.data, status=status.HTTP_201_CREATED)
      else:
          return Response(photo_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CommentUploadView(APIView):
    parser_class = (FileUploadParser,)

    def post(self, request, *args, **kwargs):

      comment_serializer = CommentSerializer(data=request.data)

      if comment_serializer.is_valid():
          comment_serializer.save()
          return Response(comment_serializer.data, status=status.HTTP_201_CREATED)
      else:
          return Response(comment_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class EmojiUploadView(APIView):
    parser_class = (FileUploadParser,)

    def post(self, request, *args, **kwargs):

      emoji_serializer = EmojiSerializer(data=request.data)

      if emoji_serializer.is_valid():
          emoji_serializer.save()
          return Response(emoji_serializer.data, status=status.HTTP_201_CREATED)
      else:
          return Response(emoji_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PhotoList(generics.ListAPIView):
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer

class CommentList(generics.ListAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

class EmojiList(generics.ListAPIView):
    queryset = Emoji.objects.all()
    serializer_class = EmojiSerializer