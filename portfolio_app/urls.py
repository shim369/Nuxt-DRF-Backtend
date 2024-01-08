from django.urls import path

from . import views

urlpatterns = [
    path('', views.AllProjectsView.as_view()),
    path('skills/', views.SkillsView.as_view()),
    path('newest/', views.NewestProjectsView.as_view()),
    path('<int:pk>/', views.ProjectsDetailView.as_view()),
]