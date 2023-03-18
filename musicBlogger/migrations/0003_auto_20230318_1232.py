# Generated by Django 2.2.28 on 2023-03-18 12:32

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('musicBlogger', '0002_auto_20230309_1630'),
    ]

    operations = [
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('artistName', models.CharField(max_length=128)),
            ],
        ),
        migrations.RenameField(
            model_name='blogs',
            old_name='title',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='songs',
            old_name='coverArt',
            new_name='image',
        ),
        migrations.RenameField(
            model_name='userprofile',
            old_name='picture',
            new_name='image',
        ),
        migrations.RenameField(
            model_name='userprofile',
            old_name='user',
            new_name='name',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='artsIndustry',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='review',
        ),
        migrations.AddField(
            model_name='songs',
            name='text',
            field=models.CharField(default=django.utils.timezone.now, max_length=1000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userprofile',
            name='text',
            field=models.CharField(default=django.utils.timezone.now, max_length=1000),
            preserve_default=False,
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='artist',
        ),
        migrations.AddField(
            model_name='songs',
            name='madeBy',
            field=models.ForeignKey(default=django.utils.timezone.now, on_delete=django.db.models.deletion.CASCADE, to='musicBlogger.Artist'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userprofile',
            name='artist',
            field=models.ManyToManyField(to='musicBlogger.Artist'),
        ),
    ]
