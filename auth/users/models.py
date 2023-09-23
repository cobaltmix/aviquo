from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=255)

class ExtracurricularReference(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    website = models.URLField(blank=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    field = models.IntegerField(choices=[
        (1, 'Computer Science'),
        (2, 'Engineering'),
        (3, 'Mathematics'),
        (4, 'Medicine'),
        (5, 'Business'),
        (6, 'Law'),
        (7, 'Politics'),
        (8, 'History'),
        (9, 'Arts'),
        (10, 'Writing'),
        (11, 'Psychology'),
        (12, 'Environment'),
        (13, 'Architecture'),

    ], null=True)
    type = models.IntegerField(choices=[
        (1, 'Internship'),
        (2, 'Research'),

    ], null=True)
    mode = models.IntegerField(choices=[
        (1, 'Remote'),
        (2, 'In-person'),
        (3, 'Hybrid'),

    ], null=True)
    season = models.IntegerField(choices=[
        (1, 'Summer'),
        (2, 'School Year'),

    ], null=True)
    selectivity = models.IntegerField(choices=[
        (1, 'Less Selective'),
        (2, 'Medium Selective'),
        (3, 'Very Selective'),

    ], null=True)
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

class ScholarshipReference(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    website = models.URLField(blank=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    field = models.IntegerField(choices=[
        (1, 'Computer Science'),
        (2, 'Engineering'),
        (3, 'Mathematics'),
        (4, 'Medicine'),
        (5, 'Business'),
        (6, 'Law'),
        (7, 'Politics'),
        (8, 'History'),
        (9, 'Arts'),
        (10, 'Writing'),
        (11, 'Psychology'),
        (12, 'Environment'),
        (13, 'Architecture'),

    ], null=True)
    type = models.IntegerField(choices=[
        (1, 'Internship'),
        (2, 'Research'),

    ], null=True)
    mode = models.IntegerField(choices=[
        (1, 'Remote'),
        (2, 'In-person'),
        (3, 'Hybrid'),

    ], null=True)
    season = models.IntegerField(choices=[
        (1, 'Summer'),
        (2, 'School Year'),

    ], null=True)
    selectivity = models.IntegerField(choices=[
        (1, 'Less Selective'),
        (2, 'Medium Selective'),
        (3, 'Very Selective'),

    ], null=True)
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

class AwardReference(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    website = models.URLField(blank=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    field = models.IntegerField(choices=[
        (1, 'Computer Science'),
        (2, 'Engineering'),
        (3, 'Mathematics'),
        (4, 'Medicine'),
        (5, 'Business'),
        (6, 'Law'),
        (7, 'Politics'),
        (8, 'History'),
        (9, 'Arts'),
        (10, 'Writing'),
        (11, 'Psychology'),
        (12, 'Environment'),
        (13, 'Architecture'),

    ], null=True)
    type = models.IntegerField(choices=[
        (1, 'Internship'),
        (2, 'Research'),

    ], null=True)
    mode = models.IntegerField(choices=[
        (1, 'Remote'),
        (2, 'In-person'),
        (3, 'Hybrid'),

    ], null=True)
    season = models.IntegerField(choices=[
        (1, 'Summer'),
        (2, 'School Year'),

    ], null=True)
    selectivity = models.IntegerField(choices=[
        (1, 'Less Selective'),
        (2, 'Medium Selective'),
        (3, 'Very Selective'),

    ], null=True)
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