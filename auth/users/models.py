
"""
@params
name - the name of the variable
type - prefix of models.Field
args - any arguments you'd pass into the standard function

examples -

{'name': 'name', 'type': 'Char', 'args': {'max_length' : 255}}
translates to
name = models.CharField(max_length=255)
"""
# Define the custom function to generate fields
from django.db import models

# Define your fields list
fields = [
    {'name': 'name', 'type': 'Char', 'args': {'max_length': 255}},
    {'name': 'description', 'type': 'Text', 'args': {}},
    {'name': 'website', 'type': 'URL', 'args': {'blank': True}},
    {'name': 'field', 'type': 'Integer', 'args': {'choices': models.IntegerChoices(
        'fields',
        'Computer_Science Engineering Mathematics Science Medicine Business Law Politics History Arts Writing Psychology Environment Architecture'
    ).choices, 'default': None, 'null': True}},
    {'name': 'type', 'type': 'Integer', 'args': {'choices': models.IntegerChoices(
        'types',
        'Internship Research Program'
    ).choices, 'default': None, 'null': True}},
    {'name': 'mode', 'type': 'Integer', 'args': {'choices': models.IntegerChoices(
        'types',
        'Remote In-person Hybrid'
    ).choices, 'default': None, 'null': True}},
    {'name': 'season', 'type': 'Integer', 'args': {'choices': models.IntegerChoices(
        'types',
        'Summer School_Year'
    ).choices, 'default': None, 'null': True}},
    {'name': 'selectivity', 'type': 'Integer', 'args': {'choices': models.IntegerChoices(
        'types',
        'Less_Selective Medium_Selective Very_Selective'
    ).choices, 'default': None, 'null': True}},
    {'name': 'cost', 'type': 'Integer', 'args': {'choices': models.IntegerChoices(
        'types',
        'Free_Summer_Program Paid_Summer_Program Unpaid_Internship Paid_Internship'
    ).choices, 'default': None, 'null': True}},
    {'name': 'Grade', 'type': 'Integer', 'args': {'choices': models.IntegerChoices(
        'types',
        '9 10 11 12 All_grades'
    ).choices, 'default': None, 'null': True}},
    {'name': 'Location', 'type': 'Integer', 'args': {'choices': models.IntegerChoices(
        'types',
        'USA Global'
    ).choices, 'default': None, 'null': True}},
    {'name': 'Offered By', 'type': 'Integer', 'args': {'choices': models.IntegerChoices(
        'types',
        'Educational_Insitution Nonprofit_Organization Business_Corporation'
    ).choices, 'default': None, 'null': True}},
    {'name': 'Organization', 'type': 'Integer', 'args': {'choices': models.IntegerChoices(
        'types',
        'Club Program'
    ).choices, 'default': None, 'null': True}},
]

# Create the Extracurriculars model
class ExtracurricularReference(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    website = models.URLField(blank=True)
    field = models.IntegerField(choices=models.IntegerChoices(
        'fields',
        'Computer_Science Engineering Mathematics Science Medicine Business Law Politics History Arts Writing Psychology Environment Architecture'
    ).choices, default=None, null=True)
    type = models.IntegerField(choices=models.IntegerChoices(
        'types',
        'Internship Research Program'
    ).choices, default=None, null=True)
    mode = models.IntegerField(choices=models.IntegerChoices(
        'types',
        'Remote In-person Hybrid'
    ).choices, default=None, null=True)
    season = models.IntegerField(choices=models.IntegerChoices(
        'types',
        'Summer School_Year'
    ).choices, default=None, null=True)
    selectivity = models.IntegerField(choices=models.IntegerChoices(
        'types',
        'Less_Selective Medium_Selective Very_Selective'
    ).choices, default=None, null=True)
    cost = models.IntegerField(choices=models.IntegerChoices(
        'types',
        'Free_Summer_Program Paid_Summer_Program Unpaid_Internship Paid_Internship'
    ).choices, default=None, null=True)
    Grade = models.IntegerField(choices=models.IntegerChoices(
        'types',
        '9 10 11 12 All_grades'
    ).choices, default=None, null=True)
    Location = models.IntegerField(choices=models.IntegerChoices(
        'types',
        'USA Global'
    ).choices, default=None, null=True)
    Offered_By = models.IntegerField(choices=models.IntegerChoices(
        'types',
        'Educational_Insitution Nonprofit_Organization Business_Corporation'
    ).choices, default=None, null=True)
    Organization = models.IntegerField(choices=models.IntegerChoices(
        'types',
        'Club Program'
    ).choices, default=None, null=True)

# Create the Awards model (with similar fields as Extracurriculars)
class AwardReference(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    website = models.URLField(blank=True)
    field = models.IntegerField(choices=models.IntegerChoices(
        'fields',
        'Computer_Science Engineering Mathematics Science Medicine Business Law Politics History Arts Writing Psychology Environment Architecture'
    ).choices, default=None, null=True)
    type = models.IntegerField(choices=models.IntegerChoices(
        'types',
        'Internship Research Program'
    ).choices, default=None, null=True)
    mode = models.IntegerField(choices=models.IntegerChoices(
        'types',
        'Remote In-person Hybrid'
    ).choices, default=None, null=True)
    season = models.IntegerField(choices=models.IntegerChoices(
        'types',
        'Summer School_Year'
    ).choices, default=None, null=True)
    selectivity = models.IntegerField(choices=models.IntegerChoices(
        'types',
        'Less_Selective Medium_Selective Very_Selective'
    ).choices, default=None, null=True)
    cost = models.IntegerField(choices=models.IntegerChoices(
        'types',
        'Free_Summer_Program Paid_Summer_Program Unpaid_Internship Paid_Internship'
    ).choices, default=None, null=True)
    Grade = models.IntegerField(choices=models.IntegerChoices(
        'types',
        '9 10 11 12 All_grades'
    ).choices, default=None, null=True)
    Location = models.IntegerField(choices=models.IntegerChoices(
        'types',
        'USA Global'
    ).choices, default=None, null=True)
    Offered_By = models.IntegerField(choices=models.IntegerChoices(
        'types',
        'Educational_Insitution Nonprofit_Organization Business_Corporation'
    ).choices, default=None, null=True)
    Organization = models.IntegerField(choices=models.IntegerChoices(
        'types',
        'Club Program'
    ).choices, default=None, null=True)

# Create the Scholarships model (with similar fields as Extracurriculars)
class ScholarshipReference(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    website = models.URLField(blank=True)
    field = models.IntegerField(choices=models.IntegerChoices(
        'fields',
        'Computer_Science Engineering Mathematics Science Medicine Business Law Politics History Arts Writing Psychology Environment Architecture'
    ).choices, default=None, null=True)
    type = models.IntegerField(choices=models.IntegerChoices(
        'types',
        'Internship Research Program'
    ).choices, default=None, null=True)
    mode = models.IntegerField(choices=models.IntegerChoices(
        'types',
        'Remote In-person Hybrid'
    ).choices, default=None, null=True)
    season = models.IntegerField(choices=models.IntegerChoices(
        'types',
        'Summer School_Year'
    ).choices, default=None, null=True)
    selectivity = models.IntegerField(choices=models.IntegerChoices(
        'types',
        'Less_Selective Medium_Selective Very_Selective'
    ).choices, default=None, null=True)
    cost = models.IntegerField(choices=models.IntegerChoices(
        'types',
        'Free_Summer_Program Paid_Summer_Program Unpaid_Internship Paid_Internship'
    ).choices, default=None, null=True)
    Grade = models.IntegerField(choices=models.IntegerChoices(
        'types',
        '9 10 11 12 All_grades'
    ).choices, default=None, null=True)
    Location = models.IntegerField(choices=models.IntegerChoices(
        'types',
        'USA Global'
    ).choices, default=None, null=True)
    Offered_By = models.IntegerField(choices=models.IntegerChoices(
        'types',
        'Educational_Insitution Nonprofit_Organization Business_Corporation'
    ).choices, default=None, null=True)
    Organization = models.IntegerField(choices=models.IntegerChoices(
        'types',
        'Club Program'
    ).choices, default=None, null=True)

# old code is below

class OldExtracurricular(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    website = models.URLField(blank=True)

    # Integer Fields
    field = models.IntegerField(null=True)
    type = models.IntegerField(null=True)
    mode = models.IntegerField(null=True)
    season = models.IntegerField(null=True)
    selectivity = models.IntegerField(null=True)
    cost = models.IntegerField(null=True)

    def __str__(self):
        return self.name
