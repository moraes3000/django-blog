from django.urls import path
from . import views

urlpatterns = [
    path('', views.PostListView.as_view(), name='PostListView'),
    path('novo/',views.PostCreateView.as_view(), name='PostCreateView'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('delete/<int:pk>', views.PostDeleteView.as_view(), name='delete-post'),
]