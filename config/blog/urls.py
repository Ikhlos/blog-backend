from django.urls import path
from blog import views
urlpatterns = [
    path('', views.BlogsView.as_view(), name='home'),
    path('detail/<int:pk>/', views.BlogsDetailView.as_view(), name='detail'),
    path('posts-by/<slug:by>/<int:id>/', views.BlogsByView, name='posts-by'),
    path('post-create/', views.PostCreateView, name='post-create'),
    path('image-create/', views.ImageCreateView, name='image-create'),
]