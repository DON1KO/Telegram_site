from django.urls import path
from . import views

urlpatterns = [
    path('send/', views.send_message),
    path('posts/', views.get_posts),
    path('about/', views.get_about),
    path('projects/', views.get_projects),
    path('consultation/', views.create_consultation),
    path('tools/', views.get_tools),
    path('reviews/', views.get_reviews),
    path('vacancy/', views.get_vacancy),
    path('vacancy/apply/', views.send_vacancy_application),
    path('contact/send/', views.send_contact),
    path('contact/info/', views.get_contact_info),
    path('design/', views.get_design),
    path('viewJob/', views.get_viewjob)
]