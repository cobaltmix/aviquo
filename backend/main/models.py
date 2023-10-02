from django.contrib.auth.models import AbstractUser
from django.db import models


# class CustomUser(AbstractUser):
class User(AbstractUser):
    bio = models.TextField(verbose_name="Bio", max_length=4000, blank=True, null=True)
    date_registered = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return str(self.id)


class Tag(models.Model):
    """Global list of tags/keywords applicable to opportunities.

    Examples: scholarship, extracurricular activity, etc.
    """

    name = models.TextField(
        unique=True, max_length=50, verbose_name="Tag", help_text="scholarship, extracurricular activity, etc."
    )

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["name"]


class Category(models.Model):
    name = models.CharField(max_length=255)


# parent model
class Forum(models.Model):
    username = models.CharField(max_length=200, default="anonymous")
    topic = models.CharField(max_length=300)
    description = models.CharField(max_length=1000, blank=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    parent_post = models.ForeignKey("self", null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id)


class Opportunity(models.Model):
    name = models.TextField(max_length=200, verbose_name="Opportunity", help_text="Opportunity name/title")
    description = models.TextField(
        max_length=4000, verbose_name="Description", help_text="Detailed description of the opportunity"
    )
    tags = models.ManyToManyField(Tag, blank=True)

    def __str__(self):
        return self.name


class Waitlist(models.Model):
    email = models.EmailField(max_length=70, blank=True, unique=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return str(self.email)
