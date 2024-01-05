from django.contrib.auth.models import User
from django.db import models
from django.template import defaultfilters

class Skill(models.Model):
    title = models.CharField('スキル', max_length=255)

    class Meta:
        ordering = ('title',)

    def __str__(self):
        return self.title

class Project(models.Model):
    skill = models.ForeignKey(Skill, related_name="projects", on_delete=models.CASCADE)
    title = models.CharField('タイトル', max_length=255)
    description = models.CharField('説明', max_length=500)
    image_url = models.URLField('サムネイルリンク', max_length=200)
    demo_link = models.URLField('リンク', max_length=200)
    github_repo = models.URLField('GitHub', max_length=200)
    content = models.TextField('テキスト')
    created_at = models.DateTimeField('作成日', auto_now_add=True)
    created_by = models.ForeignKey(User, verbose_name='作者', related_name="projects", on_delete=models.CASCADE)

    class Meta:
        ordering = ('-created_at',)

    def __str__(self):
        return self.title

    def created_at_formatted(self):
        return defaultfilters.date(self.created_at, 'M d, Y')