from django.urls import path
from . import views

urlpatterns = [
    path('send/', views.send_message,),
    path('posts/', views.get_posts,),
    path('about/', views.get_about),
    path('projects/', views.get_projects),
    path('consultation/', views.create_consultation),
    path('tools/', views.get_tools),
    path('reviews/', views.get_reviews, name='reviews'),
]