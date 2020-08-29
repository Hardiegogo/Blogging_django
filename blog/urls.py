from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>',views.detail,name='detail'),
    path('post/new',views.new_post,name='new_post'),
    path('post/<int:pk>/edit',views.edit_post,name='edit_post'),
    path('post/drafts',views.post_draft_list,name='post_draft_list'),
    path('post/<int:pk>/publish',views.post_publish,name="post_publish"),
    path('post/<int:pk>/delete',views.post_delete,name='post_delete'),
    path('accounts/login/',auth_views.LoginView.as_view(),name="login"),
    path('accounts/logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),
    path('post/<int:pk>/addComment',views.add_comment,name='add_comment'),
    path('comment/<int:pk>/approve/', views.comment_approve, name='comment_approve'),
    path('comment/<int:pk>/remove/', views.comment_remove, name='comment_remove'),

]
