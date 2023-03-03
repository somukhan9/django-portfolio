from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name="home"),
    path('resume/', views.ResumeView.as_view(), name="resume"),
    path('projects/', views.ProjectView.as_view(), name="projects"),
    path('contact/', views.ContactView.as_view(), name="contact"),
]
