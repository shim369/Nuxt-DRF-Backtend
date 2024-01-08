from rest_framework import status, authentication, permissions
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Project, Skill
from .serializers import ProjectSerializer, ProjectDetailSerializer, SkillSerializer

class SkillsView(APIView):
    def get(self, request, format=None):
        skills = Skill.objects.all()
        serializer = SkillSerializer(skills, many=True)

        return Response(serializer.data)
    
class NewestProjectsView(APIView):
    def get(self, request, format=None):
        projects = Project.objects.all()[0:4]
        serializer = ProjectSerializer(projects, many=True)

        return Response(serializer.data)
    
class AllProjectsView(APIView):
    def get(self, request, format=None):
        projects = Project.objects.all()
        skills = request.GET.get('skills', '')
        query = request.GET.get('query', '')

        if query:
            projects = projects.filter(title__icontains=query)

        if skills:
            projects = projects.filter(skill_id__in=skills.split(','))

        serializer = ProjectSerializer(projects, many=True)

        return Response(serializer.data)

class ProjectsDetailView(APIView):
    def get(self, request, pk, format=None):
        project = Project.objects.get(pk=pk)
        serializer = ProjectDetailSerializer(project)

        return Response(serializer.data)