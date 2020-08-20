from django.urls import path

from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>',views.detail,name='detail'),
    path('post/new',views.new_post,name='new_post'),
    path('post/<int:pk>/edit',views.edit_post,name='edit_post'),
    path('post/drafts',views.post_draft_list,name='post_draft_list'),
    path('post/<int:pk>/publish',views.post_publish,name="post_publish")
]
