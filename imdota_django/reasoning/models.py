from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser


class Studio(models.Model):
    name = models.CharField(max_length=30)
    score = models.FloatField(default=0)
    brief = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "工作室"
        verbose_name_plural = "工作室"


class Author(models.Model):
    studio = models.ForeignKey('Studio', on_delete=models.SET_NULL, null=True, blank=True, related_name='authors')
    name = models.CharField(max_length=30)
    brief = models.TextField(null=True, blank=True)
    score = models.FloatField(default=0)
    gender = models.CharField(
        max_length=2,
        choices=(
            ('f', 'female'),
            ('m', 'male'),
        ),
        null=True,
        blank=True
    )
    user = models.ForeignKey('User', on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "作者"
        verbose_name_plural = "作者"


class Play(models.Model):
    studio = models.ForeignKey('Studio',
                               on_delete=models.SET_NULL,
                               blank=True,
                               null=True,
                               related_name='Plays')

    author = models.ForeignKey('Author',
                               on_delete=models.SET_NULL,
                               blank=True,
                               null=True,
                               related_name='Plays')

    publisher = models.ForeignKey('Studio', on_delete=models.SET_NULL, blank=True, null=True, related_name='publishedPlays')

    name = models.CharField(max_length=50)
    brief = models.TextField(blank=True, null=True)
    durationMinutes = models.SmallIntegerField(default=0)
    wordCount = models.SmallIntegerField(default=0)
    publishedDate = models.DateTimeField(blank=True, null=True)
    characterCount = models.SmallIntegerField(default=0)
    isDetective = models.BooleanField(default=False)
    isRepresentative = models.BooleanField(default=False)
    isExclusive = models.BooleanField(default=False)
    logicScore = models.FloatField(default=0)
    storyScore = models.FloatField(default=0)
    platforms = models.ManyToManyField('Platform', blank=True, related_name='plays')
    tags = models.ManyToManyField('Tag', blank=True, related_name='plays')

    # contributors = models.ManyToManyField('User')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "剧本"
        verbose_name_plural = "剧本"


class Platform(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "游戏平台"
        verbose_name_plural = "游戏平台"


class Character(models.Model):
    play = models.ForeignKey('Play', on_delete=models.CASCADE, related_name='characters', blank=True, null=True)
    name = models.CharField(max_length=30)
    brief = models.TextField(blank=True, null=True)
    gender = models.CharField(
        max_length=2,
        choices=(
            ('f', 'female'),
            ('m', 'male'),
        ),
        null=True,
        blank=True,
    )

    def __str__(self):
        return "剧本: " + self.play.name + ", 角色: " + self.name

    class Meta:
        verbose_name = "角色"
        verbose_name_plural = "角色"


class Tag(models.Model):
    name = models.CharField(max_length=10)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "标签"
        verbose_name_plural = "标签"


class User(AbstractUser):
    gender = models.CharField(
        max_length=2,
        choices=(
            ('f', 'female'),
            ('m', 'male'),
        ),
        null=True,
        blank=True,
    )

    def __str__(self):
        return "用户 " + self.username

    class Meta:
        verbose_name = "用户"
        verbose_name_plural = "用户"


class PlayComment(models.Model):
    play = models.ForeignKey('Play', on_delete=models.CASCADE, blank=True, null=True)

    user = models.ForeignKey('User', on_delete=models.CASCADE)

    reasoningGrade = models.FloatField(default=0)
    storyGrade = models.FloatField(default=0)
    desc = models.TextField(blank=True, null=True)

    def __str__(self):
        return "用户 " + self.user.username + " 剧本 " + self.play.name + " 评论"

    class Meta:
        verbose_name = "剧本评论"
        verbose_name_plural = "剧本评论"
