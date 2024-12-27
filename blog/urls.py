from django.contrib import admin
from django.urls import path
from blog.views import home, create_post, detail_post, delete_post

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),  # Головна сторінка
    path('create_post/', create_post, name='create_post'),
    path('post/<int:post_id>/', detail_post, name='detail_post'),
    path('delete_post/<int:post_id>/', delete_post, name='delete_post'),
]
