from django.db import models

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
        (1, 'Free Summer Program'), (2, 'Paid Summer Program'), 
        (3, 'Unpaid Internship'), (4, 'Paid Internship')
    ], null=True)
    grade = models.IntegerField(choices=[(i, str(i)) for i in range(1, 6)], null=True)
    location = models.IntegerField(choices=[(1, 'USA'), (2, 'Global')], null=True)
    offered_by = models.IntegerField(choices=[
        (1, 'Educational Institution'), 
        (2, 'Non-profit Organization'), 
        (3, 'Business Corporation')
    ], null=True)

    class Meta:
        abstract = True

class ExtracurricularReference(CommonFields):
    pass

class ScholarshipReference(CommonFields):
    pass

class AwardReference(CommonFields):
    pass