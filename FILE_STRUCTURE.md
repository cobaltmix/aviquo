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
* Forum

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
    * /Forum/ - ForumViewSet
  * Generated from the router
  * /register/ - Register View
  * /login/ - Login View

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
  * User Registration
    * Validate form and create user
  * User Login
    * Check form
    * Login
    * Return token
  * Forum
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
* Custom user
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
* "/" - users.urls
* "/api" - api.urls

wsgi.py

* Import settings
* application = application

## Users

\_\_init\_\_.py

* Empty

admin.py

* Admin models for
  * Extracurriculars
  * Scholarships
  * Awards
  * Category (only name)
  * Forum

apps.py

* User app config:
  * One big auto-increment

email_sender.py

* Uses SMTP
* Email class:
  * Init:
    * Context
    * Password
    * Sender = pythondiscordbot88@gmail.com
    * Reciever
  * Create Headers:
    * Subject
    * From
    * To
  * Create body:
    * Creates the body html
  * Send message:
    * Sends the message
* Email reset:
  * Send mail:
   * Subject
   * Email template
   * Context
   * From
   * To
* Password reset view:
  * "accounts/custom_reset_email.html"

models.py

* Custom User
  * User
  * Bio
* Category
  * Name - max length 255
* Common fields
  * Name - max length 255
  * Description - text
  * Website - url
  * Category - Choice
  * Field - Choice
  * Type - Choice
  * Mode - Choice
  * Season - Choice
  * Selectivity - Choice
  * Cost - Choice
  * Grade - Choice
  * Location - Choice
  * Offered by - Choice
  * Everything except name and description is optional (Can be null)
* Extracurricular, Scholarship, and Award are all commented out (common fields is better I think)
* Forum
  * Username Char(200)
  * Topic Char(300)
  * Description Char(1000)
  * Date Created
  * Parent Post

serializers.py

* ECS, Award, SC, User, Forum
  * All fields, matching model.

tests.py

* Empty

urls.py

* Urls:
  * / - Home
  * /signup/ - signup
  * /ec/create/ - Create EC
  * /ec/list/ - List ECs
  * /aws/create/ - Create AW
  * /aws/list/ - List AWs
  * /sc/create/ - Create SC
  * /sc/list/ - List SCs
  * /profile/ - Profile
  * /password_reset/ - Pass reset
  * /forum/ - Forum

views.py

* Custom User Creation Form
  * Default Fields
  * Email
* Edit Profile Form
  * Use user model
  * Username, email, first and last name
* Profile page
  * Login needed
  * Post - edit profile and redirect to /profile/
  * Get - get form and show profile
* Sign up
  * Render sign up form
* EC/AW/SC Create/List - Rest framework query add/list
* Forum View
  * All values

## Migrations

* Auto generated Django stuff

## Templates

### Accounts

custom\_reset\_email.html
* Reset email template

### Registration

login.html
* Login template

signup.html
* Signup template

### Users

base.html
* Base html, content that is pink

home.html
* Home page

profile.html
* Profile info and editing

# **Add more stuff as you please**
