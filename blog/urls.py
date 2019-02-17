from django.urls import path
from . import views

urlpatterns = [
	path('', views.index, name="homepage"),
	path('categories', views.category_page, name='category_page'),
	path('profile', views.profile_page, name="profile_page") ,
	path('post/<int:pk>/', views.content_box, name="post_detail"),
	path('post/new', views.post_new, name="post_new"),
	path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
]
