# Generated by Django 2.1.1 on 2018-09-15 13:54

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
                ('gender', models.CharField(choices=[('f', 'female'), ('m', 'male')], max_length=2, null=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
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
                ('grade', models.FloatField(default=0)),
                ('gender', models.CharField(choices=[('f', 'female'), ('m', 'male')], max_length=2, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Platform',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Play',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('brief', models.CharField(max_length=2000, null=True)),
                ('durationMinutes', models.SmallIntegerField(default=0)),
                ('publishedDate', models.DateTimeField(null=True)),
                ('roleCount', models.SmallIntegerField(default=0)),
                ('isDetective', models.BooleanField(default=False)),
                ('isRepresentative', models.BooleanField(default=False)),
                ('reasoningGrade', models.FloatField(default=0)),
                ('storyGrade', models.FloatField(default=0)),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='Plays', to='reasoning.Author')),
                ('platforms', models.ManyToManyField(related_name='Plays', to='reasoning.Platform')),
            ],
        ),
        migrations.CreateModel(
            name='PlayComment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reasoningGrade', models.FloatField(default=0)),
                ('storyGrade', models.FloatField(default=0)),
                ('desc', models.TextField(null=True)),
                ('play', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='reasoning.Play')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reasoning.User')),
            ],
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('brief', models.CharField(max_length=100, null=True)),
                ('gender', models.CharField(choices=[('f', 'female'), ('m', 'male')], max_length=2, null=True)),
                ('play', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='roles', to='reasoning.Play')),
            ],
        ),
        migrations.CreateModel(
            name='Studio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('grade', models.FloatField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
                ('play', models.ManyToManyField(to='reasoning.Play')),
            ],
        ),
        migrations.AddField(
            model_name='play',
            name='publisher',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='publishedPlays', to='reasoning.Studio'),
        ),
        migrations.AddField(
            model_name='play',
            name='studio',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='Plays', to='reasoning.Studio'),
        ),
        migrations.AddField(
            model_name='author',
            name='studio',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='authors', to='reasoning.Studio'),
        ),
    ]
