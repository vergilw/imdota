from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser


class Studio(models.Model):
    name = models.CharField(max_length=30)
    grade = models.FloatField(default=0)


class Author(models.Model):
    studio = models.ForeignKey('Studio', on_delete=models.SET_NULL, null=True, related_name='authors')
    name = models.CharField(max_length=30)
    grade = models.FloatField(default=0)
    gender = models.CharField(
        max_length=2,
        choices=(
            ('f', 'female'),
            ('m', 'male'),
        ),
        null=True
    )

    # ROLE_CHOICES = (
    #     (FRESHMAN, 'Writer'),
    #     (SOPHOMORE, 'Designer'),
    #     (JUNIOR, 'Junior'),
    #     (SENIOR, 'Senior'),
    # )
    # role = models.CharField(
    #     max_length=2,
    #     choices=ROLE_CHOICES,
    #     default=FRESHMAN,
    # )


class Play(models.Model):
    studio = models.ForeignKey('Studio',
                               on_delete=models.SET_NULL,
                               null=True,
                               related_name='Plays')

    author = models.ForeignKey('Author',
                               on_delete=models.SET_NULL,
                               null=True,
                               related_name='Plays')

    publisher = models.ForeignKey('Studio', on_delete=models.SET_NULL, null=True, related_name='publishedPlays')

    name = models.CharField(max_length=50)
    brief = models.CharField(max_length=2000, null=True)
    durationMinutes = models.SmallIntegerField(default=0)
    publishedDate = models.DateTimeField(null=True)
    roleCount = models.SmallIntegerField(default=0)
    isDetective = models.BooleanField(default=False)
    isRepresentative = models.BooleanField(default=False)
    reasoningGrade = models.FloatField(default=0)
    storyGrade = models.FloatField(default=0)
    platforms = models.ManyToManyField('Platform', related_name='Plays')

    # contributor


class Platform(models.Model):
    name = models.CharField(max_length=30)


class Role(models.Model):
    play = models.ForeignKey('Play', on_delete=models.CASCADE, related_name='roles', null=True)
    name = models.CharField(max_length=30)
    brief = models.CharField(max_length=100, null=True)
    gender = models.CharField(
        max_length=2,
        choices=(
            ('f', 'female'),
            ('m', 'male'),
        ),
        null=True
    )


class Tag(models.Model):
    name = models.CharField(max_length=10)
    play = models.ManyToManyField('Play')


class User(AbstractUser):
    gender = models.CharField(
        max_length=2,
        choices=(
            ('f', 'female'),
            ('m', 'male'),
        ),
        null=True
    )


class PlayComment(models.Model):
    play = models.ForeignKey('Play', on_delete=models.CASCADE, null=True)

    user = models.ForeignKey('User', on_delete=models.CASCADE)

    reasoningGrade = models.FloatField(default=0)
    storyGrade = models.FloatField(default=0)
    desc = models.TextField(null=True)
