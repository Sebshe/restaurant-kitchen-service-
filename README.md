# Piter's restaurant

This is a Django project that aims to manage the interaction between cooks and the creation of dishes in a restaurant.

## Check it out!
[Piter's restaurant project deployed to Heroku](past_link)

## Installing / Getting started

Clone the repository:
```shell
git clone https://github.com/Sebshe/restaurant-kitchen-service-.git
```

Create a virtual environment:
```shell
python -m venv env
```

Activate the virtual environment:

* For Windows:
```shell
env\Scripts\activate
```
* For macOS/Linux:
```shell
source env/bin/activate
```

Install the required dependencies:
```shell
pip install -r requirements.txt
```

Set up the database:
```shell
python manage.py migrate
```
Create a superuser:
```shell
python manage.py createsuperuser
```
Start the development server:
```shell
python manage.py runserver
```

## Features

* User Registration and Authentication: Users can register for an account and authenticate themselves to access the system.
* Account Management: Users have the ability to manage their personal account information, including updating their profile.
* Dish Creation via Web Interface: Chefs can create new dishes using the web interface, providing details such as dish name, description, ingredients, and cooking instructions.
* Admin Panel Management: Administrators have access to the Django admin panel, which allows them to manage various aspects of the application, including user accounts, dish data.
