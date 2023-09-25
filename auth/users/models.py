from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    bio = models.TextField(blank=True)

    def __str__(self):
        return str(self.id)
    
class Category(models.Model):
    name = models.CharField(max_length=255)


    
class CommonFields(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    website = models.URLField(blank=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    field = models.IntegerField(choices=[
        (i, field) for i, field in enumerate([
            'Computer Science', 'Engineering', 'Mathematics', 'Medicine', 
            'Business', 'Law', 'Politics', 'History', 'Arts', 'Writing', 
            'Psychology', 'Environment', 'Architecture'
        ], start=1)
    ], null=True)
    type = models.IntegerField(choices=[(1, 'Internship'), (2, 'Research')], null=True)
    mode = models.IntegerField(choices=[(1, 'Remote'), (2, 'In-person'), (3, 'Hybrid')], null=True)
    season = models.IntegerField(choices=[(1, 'Summer'), (2, 'School Year')], null=True)
    selectivity = models.IntegerField(choices=[(1, 'Less Selective'), (2, 'Medium Selective'), (3, 'Very Selective')], null=True)

    cost = models.IntegerField(choices=[
        (1, 'Free Summer Program'),
        (2, 'Paid Summer Program'),
        (3, 'Unpaid Internship'),
        (4, 'Paid Internship'),

    ], null=True)
    grade = models.IntegerField(choices=[
        (1, '9'),
        (2, '10'),
        (3, '11'),
        (4, '12'),
        (5, 'All'),

    ], null=True)
    location = models.IntegerField(choices=[
        (1, 'USA'),
        (2, 'Global'),

    ], null=True)
    offered_by = models.IntegerField(choices=[
        (1, 'Educational_Institution'),
        (2, 'Non-profit_Organization'),
        (3, 'Business_Corporation'),

    ], null=True)
    class Meta:
        abstract = True

class ExtracurricularReference(CommonFields):
    pass
   

class AwardReference(CommonFields):
    pass

class ScholarshipReference(CommonFields):
    pass
    

#parent model
class Forum(models.Model):
    username=models.CharField(max_length=200,default="anonymous")
    topic= models.CharField(max_length=300)
    description = models.CharField(max_length=1000,blank=True)
    date_created=models.DateTimeField(auto_now_add=True,null=True)
    parent_post = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE)
    def __str__(self):
        return str(self.id)
 
