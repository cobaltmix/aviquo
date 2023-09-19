from django.db import models
from django.contrib.auth.models import User


build_fields = lambda fields: {field['name']: getattr(models, field['type'] + 'Field')(**field['args']) for field in fields}

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
fields = [
        {'name': 'name', 'type': 'Char', 'args': {'max_length' : 255}},
        {'name': 'description', 'type': 'Text', 'args': {}},
        {'name': 'website', 'type': 'URL', 'args': {'blank' : True}},
        {'name': 'field', 'type': 'Integer', 'args': {'choices' : models.IntegerChoices('fields', 'STEM Liberal_Art').choices, 'default' : None, 'null' : True}},
        {'name': 'type', 'type': 'Integer', 'args': {'choices' : models.IntegerChoices('types', 'ChoiceA ChoiceB ChoiceC').choices, 'default' : None, 'null' : True}},

        #rest of code follows for the rest of fields
]

gen_fields = build_fields(fields)
gen_fields['__module__'] = __name__

ExtracurricularReference = type('Extracurricular', (models.Model,), gen_fields)

#old code is below

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