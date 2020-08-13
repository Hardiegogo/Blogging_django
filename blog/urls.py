from django.urls import path

from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>',views.detail,name='detail'),
    path('post/new',views.new_post,name='new_post')
]
