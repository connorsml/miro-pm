from django.db import models
from django.contrib.auth.models import User
from uuidfield import UUIDField
from positions import PositionField


def project_types():
    return [
        ('New Development', 'New Development'),
        ('Support & Maintenance', 'Support & Maintenance')
    ]


def task_types():
    return [
        ('Bug', 'Bug'),
        ('User Story', 'User Story'),
        ('Investigation', 'Investigation'),
        ('Technical Task', 'Technical Task')
    ]


def task_states():
    return [
        ('Queued', 'Queued'),
        ('In Progress', 'In Progress'),
        ('Complete', 'Complete'),
        ('Abandoned', 'Abandoned')
    ]

# Create your models here.
class Organisation(models.Model):
    organisation_identifier = UUIDField(auto=True)
    name = models.CharField(null=False, blank=False, max_length=256)
    owner = models.ForeignKey(User, null=False, blank=False)
    allowed_users = models.IntegerField(null=False, default=5)

    class Meta:
        verbose_name_plural = "Organisations"

    def __str__(self):
        return self.name


class Project(models.Model):
    project_identifier = UUIDField(auto=True)
    name = models.CharField(null=False, blank=False, max_length=256)
    organisation = models.ForeignKey(Organisation, null=False, blank=False)
    type = models.CharField(
        null=False,
        blank=False,
        max_length=256,
        choices=project_types()
    )


class Sprint(models.Model):
    sprint_identifier = UUIDField(auto=True)
    name = models.CharField(null=False, blank=False, max_length=256)
    project = models.ForeignKey(Project, null=False, blank=False)
    start_date = models.DateTimeField(null=False)
    due_date = models.DateTimeField(null=False)
    released = models.BooleanField(null=False, default=False)


class Task(models.Model):
    task_identifier = UUIDField(auto=True)
    type = models.CharField(
        null=False,
        blank=False,max_length=256,
        choices=task_types()
    )
    name = models.CharField(null=False, blank=False, max_length=256)
    description = models.TextField(null=True, blank=True)
    status = models.CharField(
        null=False,
        blank=False,
        max_length=256,
        choices=task_states()
    )
    user = models.ForeignKey(User, null=True, blank=True)
    project = models.ForeignKey(Project, null=False, blank=False)
    sprint = models.ForeignKey(Sprint, null=True, blank=True)
    size = models.IntegerField(null=True)
    position = PositionField(collection='sprint')