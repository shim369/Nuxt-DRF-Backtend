from rest_framework import status, authentication, permissions
from rest_framework.views import APIView
from rest_framework.response import Response

from .forms import ProjectForm
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
    
class AdminView(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, format=None):
        projects = Project.objects.filter(created_by=request.user)
        serializer = ProjectSerializer(projects, many=True)

        return Response(serializer.data)

class CreateProjectView(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        form = ProjectForm(request.data)

        if form.is_valid():
            project = form.save(commit=False)
            project.created_by = request.user
            project.save()

            return Response({'status': 'created'})
        else:
            return Response({'status': 'errors', 'errors': form.errors})
    
    def put(self, request, pk):
        project = Project.objects.get(pk=pk, created_by=request.user)
        form = ProjectForm(request.data, instance=project)
        if form.is_valid():
            form.save()
            return Response({'status': 'updated'})
        else:
            return Response({'status': 'errors', 'errors': form.errors}, status=400)

    def delete(self, request, pk):
        project = Project.objects.get(pk=pk, created_by=request.user)
        project.delete()

        return Response({'status': 'deleted'})

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