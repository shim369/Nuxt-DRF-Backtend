from rest_framework import serializers

from .models import Project, Skill


class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = ['id', 'title']

class ProjectSerializer(serializers.ModelSerializer):
    skill_title = serializers.CharField(source='skill.title', read_only=True)

    class Meta:
        model = Project
        fields = (
            'id', 'title', 'description', 'small_image', 'demo_link',
            'github_repo', 'skill_title'
        )


class ProjectDetailSerializer(serializers.ModelSerializer):
    skill_title = serializers.CharField(source='skill.title', read_only=True)

    class Meta:
        model = Project
        fields = (
            'id', 'title', 'description', 'big_image', 'demo_link',
            'github_repo', 'frontend', 'backend', 'content', 'created_at_formatted', 'skill_title', 'created_by'
        )