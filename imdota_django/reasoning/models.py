from django.db import models

# Create your models here.


class Studio(models.Model):
    name = models.CharField(max_length=30)
    grade = models.FloatField(default=0)


class Author(models.Model):
    studio = models.ForeignKey('Studio', on_delete=models.SET_NULL, null=True, related_name='authors')
    name = models.CharField(max_length=30)
    grade = models.FloatField(default=0)

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

    studioRepresentative = models.ForeignKey('Author',
                                             on_delete=models.SET_NULL,
                                             null=True,
                                             related_name='representativePlays')

    author = models.ForeignKey('Author',
                               on_delete=models.SET_NULL,
                               null=True,
                               related_name='Plays')

    authorRepresentative = models.ForeignKey('Studio',
                                             on_delete=models.SET_NULL,
                                             null=True,
                                             related_name='representativePlays')

    name = models.CharField(max_length=50)
    brief = models.CharField(max_length=2000, null=True)
    duration = models.DurationField(null=True)
    publishedDate = models.DateTimeField(null=True)
    roleCount = models.SmallIntegerField(default=0)
    isDetective = models.BooleanField(default=False)
    reasoningGrade = models.FloatField(default=0)
    storyGrade = models.FloatField(default=0)
    platforms = models.ManyToManyField('Platform', related_name='Plays')


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