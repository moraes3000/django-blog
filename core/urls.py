from django.urls import path
from . import views
from ckeditor_uploader.views import upload, browse

urlpatterns = [
    # path('upload',upload, name='ckeditor_upload'),
    # path('browse',browse, name='ckeditor_browse'),
    # path('', views.post_list, name='post_list'),
    # path('post/<int:pk>/', views.post_detail, name='post_detail'),
   
]