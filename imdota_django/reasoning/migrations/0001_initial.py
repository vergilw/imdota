# Generated by Django 2.1.1 on 2018-09-27 03:33

import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0009_alter_user_last_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('gender', models.CharField(blank=True, choices=[('f', 'female'), ('m', 'male')], max_length=2, null=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': '用户',
                'verbose_name_plural': '用户',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('brief', models.TextField(blank=True, null=True)),
                ('grade', models.FloatField(default=0)),
                ('gender', models.CharField(blank=True, choices=[('f', 'female'), ('m', 'male')], max_length=2, null=True)),
            ],
            options={
                'verbose_name': '作者',
                'verbose_name_plural': '作者',
            },
        ),
        migrations.CreateModel(
            name='Character',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('brief', models.TextField(blank=True, null=True)),
                ('gender', models.CharField(blank=True, choices=[('f', 'female'), ('m', 'male')], max_length=2, null=True)),
            ],
            options={
                'verbose_name': '角色',
                'verbose_name_plural': '角色',
            },
        ),
        migrations.CreateModel(
            name='Platform',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
            options={
                'verbose_name': '游戏平台',
                'verbose_name_plural': '游戏平台',
            },
        ),
        migrations.CreateModel(
            name='Play',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('brief', models.TextField(blank=True, null=True)),
                ('durationMinutes', models.SmallIntegerField(default=0)),
                ('wordCount', models.SmallIntegerField(default=0)),
                ('publishedDate', models.DateTimeField(blank=True, null=True)),
                ('characterCount', models.SmallIntegerField(default=0)),
                ('isDetective', models.BooleanField(default=False)),
                ('isRepresentative', models.BooleanField(default=False)),
                ('logicScore', models.FloatField(default=0)),
                ('storyScore', models.FloatField(default=0)),
                ('author', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='Plays', to='reasoning.Author')),
                ('platforms', models.ManyToManyField(blank=True, related_name='plays', to='reasoning.Platform')),
            ],
            options={
                'verbose_name': '剧本',
                'verbose_name_plural': '剧本',
            },
        ),
        migrations.CreateModel(
            name='PlayComment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reasoningGrade', models.FloatField(default=0)),
                ('storyGrade', models.FloatField(default=0)),
                ('desc', models.TextField(blank=True, null=True)),
                ('play', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='reasoning.Play')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reasoning.User')),
            ],
            options={
                'verbose_name': '剧本评论',
                'verbose_name_plural': '剧本评论',
            },
        ),
        migrations.CreateModel(
            name='Studio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('grade', models.FloatField(default=0)),
                ('brief', models.TextField(blank=True, null=True)),
            ],
            options={
                'verbose_name': '工作室',
                'verbose_name_plural': '工作室',
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
                ('play', models.ManyToManyField(blank=True, to='reasoning.Play')),
            ],
            options={
                'verbose_name': '标签',
                'verbose_name_plural': '标签',
            },
        ),
        migrations.AddField(
            model_name='play',
            name='publisher',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='publishedPlays', to='reasoning.Studio'),
        ),
        migrations.AddField(
            model_name='play',
            name='studio',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='Plays', to='reasoning.Studio'),
        ),
        migrations.AddField(
            model_name='character',
            name='play',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='characters', to='reasoning.Play'),
        ),
        migrations.AddField(
            model_name='author',
            name='studio',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='authors', to='reasoning.Studio'),
        ),
    ]
