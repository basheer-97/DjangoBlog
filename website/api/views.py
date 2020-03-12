from django.shortcuts import render
from rest_framework import generics, permissions
from website1.models import Post
from . serializers import PostSerializer

# Create your views here.

class PostAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset=Post.objects.all()
    serializer_class=PostSerializer

class PostAPIDetailView(generics.ListCreateAPIView):
    queryset=Post.objects.all()
    serializer_class=PostSerializer