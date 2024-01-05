from django.urls import path

from . import views

urlpatterns = [
    path('', views.AllProjectsView.as_view()),
    path('skills/', views.SkillsView.as_view()),
    path('admin/', views.AdminView.as_view()),
    path('create/', views.CreateProjectView.as_view()),
    path('newest/', views.NewestProjectsView.as_view()),
    path('<int:pk>/', views.ProjectsDetailView.as_view()),
    path('<int:pk>/delete/', views.CreateProjectView.as_view()),
    path('<int:pk>/edit/', views.CreateProjectView.as_view()),
]