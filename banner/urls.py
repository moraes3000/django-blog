from django.urls import path
from . import views

urlpatterns = [
    path('novo', views.BannerCreateView.as_view(), name='BannerCreateView'),
    path('lista', views.BannerListView.as_view(), name='BannerListView'),
    path('delete/<int:pk>', views.BannerDeleteView.as_view(), name='BannerDeleteView'),
    path('update/<int:pk>', views.BannerUpdate.as_view(), name='BannerUpdate')
    
    # #admin
    # path('admin-post', views.AdminPostView.as_view(), name='admin-post'),
    # path('novo/', views.PostCreateView.as_view(), name='PostCreateView'),
    # path('delete/<int:pk>', views.PostDeleteView.as_view(), name='delete-post'),
    # path('admin-post/<int:pk>', views.AdminPostUpdate.as_view(), name='AdminPostUpdate'),


]