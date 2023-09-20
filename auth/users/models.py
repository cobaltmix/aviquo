from django.db import models

build_fields = lambda fields: {field['name']: getattr(models, field['type'] + 'Field')(**field['args']) for field in
                               fields}


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
    {'name': 'name', 'type': 'Char', 'args': {'max_length': 255}},
    {'name': 'description', 'type': 'Text', 'args': {}},
    {'name': 'website', 'type': 'URL', 'args': {'blank': True}},
    {'name': 'field', 'type': 'Integer', 'args': {'choices': models.IntegerChoices('fields', 'Computer_Science '
                                                                                             'Engineering '
                                                                                             'Mathematics '
                                                                                             'Science Medicine '
                                                                                             'Business Law '
                                                                                             'Politics History '
                                                                                             'Arts Writing '
                                                                                             'Psychology '
                                                                                             'Environment '
                                                                                             'Architecture').choices,
                                                  'default': None, 'null': True}},
    {'name': 'type', 'type': 'Integer',
     'args': {'choices': models.IntegerChoices('types', 'Internship Research Program').choices, 'default': None,
              'null': True}},
    {'name': 'mode', 'type': 'Integer',
     'args': {'choices': models.IntegerChoices('types', 'Remote In-person Hybrid').choices, 'default': None,
              'null': True}},
    {'name': 'season', 'type': 'Integer',
     'args': {'choices': models.IntegerChoices('types', 'Summer School_Year').choices, 'default': None,
              'null': True}},
    {'name': 'selectivity', 'type': 'Integer',
     'args': {'choices': models.IntegerChoices('types', 'Less_Selective Medium_Selective Very_Selective').choices, 'default': None,
              'null': True}},
    {'name': 'cost', 'type': 'Integer',
     'args': {'choices': models.IntegerChoices('types', 'Free_Summer_Program Paid_Summer_Program Unpaid_Internship Paid_Internship').choices, 'default': None,
              'null': True}},
    {'name': 'Grade', 'type': 'Integer',
     'args': {'choices': models.IntegerChoices('types', '9 10 11 12 All_grades').choices, 'default': None,
              'null': True}},
    {'name': 'Location', 'type': 'Integer',
     'args': {'choices': models.IntegerChoices('types', 'USA Global').choices, 'default': None,
              'null': True}},
    {'name': 'Offered By', 'type': 'Integer',
     'args': {'choices': models.IntegerChoices('types', 'Educational_Insitution Nonprofit_Organization Business_Corporation').choices, 'default': None,
              'null': True}},
    {'name': 'Organization', 'type': 'Integer',
     'args': {'choices': models.IntegerChoices('types', 'Club Program').choices, 'default': None,
              'null': True}},




    # rest of code follows for the rest of fields
]

gen_fields = build_fields(fields)
gen_fields['__module__'] = __name__

ExtracurricularReference = type('Extracurricular', (models.Model,), gen_fields)


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
