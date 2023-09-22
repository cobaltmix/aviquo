# aviquo

Before setting up the git, create a .venv environement for your program:

	python -m venv

To use our program, simply copy and paste into your terminal:

	git clone https://github.com/cobaltmix/aviquo.git

Next, you need to install all the dependencies:

	cd aviquo/auth
	pip install -r requirements.txt

Now, we need to set up the database. Paste into your terminal:

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

You are all done! Now you can add values to your databases!


