# Generated by Django 5.0 on 2024-01-02 06:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio_app', '0002_remove_project_updated_at_project_created_by'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='image_url',
            field=models.URLField(default='', verbose_name='サムネイルリンク'),
            preserve_default=False,
        ),
    ]
