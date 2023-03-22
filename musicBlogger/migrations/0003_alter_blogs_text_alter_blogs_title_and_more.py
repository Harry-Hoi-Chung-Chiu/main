# Generated by Django 4.1.7 on 2023-03-21 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('musicBlogger', '0002_alter_blogs_options_alter_comments_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogs',
            name='text',
            field=models.CharField(default='', max_length=4096),
        ),
        migrations.AlterField(
            model_name='blogs',
            name='title',
            field=models.CharField(default='', max_length=128),
        ),
        migrations.AlterField(
            model_name='comments',
            name='content',
            field=models.CharField(default='', max_length=1000),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='text',
            field=models.CharField(default='', max_length=1000),
        ),
    ]
