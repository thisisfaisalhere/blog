from django.urls import path
from .views import BlogDetail, BlogList, CommentApi, EditBlogApi

app_name = 'blog_api'

urlpatterns = [
    # route for user edit 
    path('edit/', EditBlogApi.as_view(), name='edit'),
    path('edit/<str:pk>/', EditBlogApi.as_view(), name='edit'),
    # read only blog details route
    path('<str:slug>/', BlogDetail.as_view(), name='detail'),
    # get list of blogs
    path('', BlogList.as_view(), name='list'),

    # comment routes
    path('c/comment/', CommentApi.as_view(), name='comment'),
    path('c/comment/<str:pk>/', CommentApi.as_view(), name='comment'),
]