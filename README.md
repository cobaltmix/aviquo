# aviquo

Before setting up the git, create a .venv environement for your program:

	python -m venv

To use our program, simply copy and paste into your terminal:

	git clone https://github.com/cobaltmix/aviquo.git

Next, you need to install all the dependencies:

	cd aviquo
	pip install -r requirements.txt

Now, we need to set up the database. Paste into your terminal:
	
	cd auth
	python manage.py makemigrations
	python manage.py migrate

Now you can create a superuser, paste:

	python manage.py createsuperuser

	Name: [YOUR NAME]
	Email address: [YOUR EMAIL ADDRESS]
	Password: [YOUR PASSWORD]
	Retype Password: [YOUR PASSWORD]

Now run:

	python manage.py runserver

Now that your superuser is set up, you can navigate to:

	http://127.0.0.1:8000/admin

Here, you will type in your super user name and password.

To access the front-end portion of the app, navigate to the frontend folder with:

	 cd ..
	 cd frontend
 
To setup and run development server:

	 npm install
	 npm start
 
Navigate to localhost:3000. This is where changes to the database must be reflected

A guide to the backend APIs:
/api/users is the endpoint for users
/api/ECS is the endpoint for extracurriculars
/api/AWS is the endpoint for awards
/api/SC is the endpoint for scholarships
all CRUD functions have been set-up, along with middle-ware dependencies, so backend APIs can be accesed seemlessly

You are all done! Now you can add values to your databases, and create the front-end using api endpoints!

