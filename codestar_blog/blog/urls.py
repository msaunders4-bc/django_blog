from . import views
from django.urls import path

urlpatterns = [
    path("", views.PostList.as_view(), name='home'),
    path('<slug:slug>/', views.post_detail, name='post_detail'),  # Changed from PostDetail.as_view()
    path('<slug:slug>/edit_comment/<int:comment_id>', views.comment_edit, name='comment_edit'),
]