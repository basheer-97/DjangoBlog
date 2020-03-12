from django.urls import path
from .views import PostAPIView, PostAPIDetailView

urlpatterns=[
    path('',PostAPIDetailView.as_view(),name='api_detail'),
    path('<int:pk>',PostAPIView.as_view(),name='list')
]
