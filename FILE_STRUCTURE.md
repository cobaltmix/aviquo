# Auth

Manage.py:

* Main program that is used to manage the program

## Auth/Api

\_\_init\_\_.py

* Empty

admin.py

* Empty

apps.py

* Configures API as an app
* name = "api"
* Default field is an auto-incrementing big integer

models.py

* Empty

serializers.py

* Base serializer *BaseSerializer*. All fields are used.
* User (from django ([values](https://docs.djangoproject.com/en/4.2/ref/contrib/auth/))
* Extracurricular
* Award
* Scholarship

tests.py

* Empty

urls.py

* Urls:
  * REST API Auto-routing:
    * ViewSets from views.py
    * /users/ - UserViewSet
    * /ECS/ - ECSViewSet (extracurriculars)
    * /AWS/ - AWSViewSet (awards)
    * /SC/ - SCCViewSet (scholarships)
  * Generated from the router

views.py

* Base View:
  * Userview
    * Show all data
  * Extracurricular
    * Show all data
  * Award
    * Show all data
  * Scholarship
    * Show all data

### Auth/Api/Migrations

\_\_init\_\_.py:

* Empty

## Auth/Auth

\_\_init\_\_.py

* Empty

asgi.py

* Import settings
* Set application to application

settings.py

* Root is \.\.\/\.\. (aviquo/)
* Secret Key
* Debug mode = on
* Allowed hosts
* Installed apps
* Middleware
* Main url config = auth.urls.py
* Wsgi app is auth.wsgi.application
* Password validators
* Language
* Time zone
* Static url: "static/"
* Primary auto field: Big auto increment
* Whitelist: localhost:3000

urls.py

* "/admin" - Default django admin
* "/accounts" - Default django accounts
* "/accounts" - users.urls
* "/home" - users.urls
* "/api" - api.urls

wsgi.py

* Import settings
* application = application

## Users

\_\_init\_\_.py

* Empty

admin.py

*

└── users
    ├── __init__.py
    ├── admin.py
    ├── apps.py
    ├── email_sender.py
    ├── migrations
    │   ├── 0001_initial.py
    │   ├── 0002_oldextracurricular_alter_extracurricular_cost_and_more.py
    │   ├── 0003_extracurricular_grade_extracurricular_location_and_more.py
    │   ├── 0004_awardreference_category_extracurricularreference_and_more.py
    │   ├── 0004_awardreference_extracurricularreference_and_more.py
    │   ├── 0005_remove_category_grade_remove_category_location_and_more.py
    │   ├── 0006_awardreference_grade_awardreference_location_and_more.py
    │   ├── __init__.py
    ├── models.py
    ├── serializers.py
    ├── templates
    │   ├── accounts
    │   │   └── custom_reset_email.html
    │   ├── registration
    │   │   ├── login.html
    │   │   └── signup.html
    │   └── users
    │       ├── base.html
    │       ├── home.html
    │       └── profile.html
    ├── tests.py
    ├── urls.py
    └── views.py
