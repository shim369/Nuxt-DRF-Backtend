from django.contrib import admin

from .models import Project, Skill

from django_summernote.admin import SummernoteModelAdmin


class ArticleAdmin(SummernoteModelAdmin):
    summernote_fields = '__all__'

admin.site.register(Skill)
admin.site.register(Project, ArticleAdmin)