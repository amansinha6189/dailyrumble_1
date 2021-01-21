# Generated by Django 3.1.2 on 2021-01-21 07:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('author_image', models.ImageField(default='', upload_to='blog/images')),
                ('bio', models.CharField(max_length=150)),
                ('para1', models.TextField()),
                ('para2', models.TextField()),
                ('para3', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100)),
                ('image', models.ImageField(default='', upload_to='blog/images')),
                ('content', models.TextField()),
                ('slug', models.CharField(max_length=150)),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('author', models.CharField(max_length=100)),
                ('meta_description', models.CharField(max_length=160, null=True)),
                ('meta_keywords', models.CharField(max_length=500, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=250)),
                ('email', models.EmailField(max_length=254)),
                ('content', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='FrontPage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('para1', models.TextField()),
                ('para2', models.TextField(null=True)),
                ('para3', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='SocialContact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('facebook', models.TextField(null=True)),
                ('instagram', models.TextField(null=True)),
                ('twitter', models.TextField(null=True)),
                ('linkedin', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('task', models.CharField(max_length=150)),
                ('description', models.TextField()),
                ('priority', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='BlogComment',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('comment', models.TextField()),
                ('timestamp', models.DateTimeField(default=django.utils.timezone.now)),
                ('blog', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.blog')),
                ('parent', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='blog.blogcomment')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='blog',
            name='tags',
            field=models.ManyToManyField(to='blog.Tag'),
        ),
    ]
