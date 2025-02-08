# Django-To-Do-App

A simple To-Do List web application built with Django. This app allows users to add, edit, and delete tasks.

Features
Add new tasks

Edit existing tasks

Mark tasks as completed

Delete tasks

Installation
Clone the repository:

bash
git clone https://github.com/your_username/django-todo-app.git
cd django-todo-app
Create and activate a virtual environment:

bash
python -m venv venv
source venv/bin/activate   # On Windows use `venv\Scripts\activate`
Install the required packages:

bash
pip install -r requirements.txt
Run migrations:

bash
python manage.py makemigrations
python manage.py migrate
Create a superuser:

bash
python manage.py createsuperuser --username Tanjim --email admin@example.com
# When prompted, enter the password: 123
Start the development server:

bash
python manage.py runserver
Access the application: Open your web browser and go to http://127.0.0.1:8000/

Admin interface: http://127.0.0.1:8000/admin/

Username: Tanjim

Password: 123

Project Structure
todo_project/: Project settings and configuration.

tasks/: Contains the app for managing tasks.

models.py: Defines the Task model.

views.py: Handles the application logic for tasks.

forms.py: Defines the Task form.

admin.py: Registers the Task model with the admin site.

templates/tasks/: HTML templates for the app.

Usage
Adding a Task
Go to the main page.

Click on "Add Task".

Fill out the task form and click "Save".

Editing a Task
Go to the main page.

Click on the task you want to edit.

Update the task details and click "Save".

Marking a Task as Completed
Go to the main page.

Check the checkbox next to the task to mark it as completed.

Deleting a Task
Go to the main page.

Click on the task you want to delete.

Click the "Delete" button.
