# Django Authentication Project

A simple Django authentication system featuring user registration, login/logout, password change, and role-based access control using Django’s built-in auth system.

## Features
- User registration system
- Login and logout functionality
- Password change functionality
- Protected views using @login_required
- Staff-only content restriction
- Django messages framework for feedback
- next= redirect after login
- Responsive navigation bar
- Django admin panel integration

## Tech Stack
- Python
- Django
- HTML5
- CSS3

## Setup

python -m venv env

.\env\Scripts\activate

pip install django

python manage.py runserver

## Usage
http://127.0.0.1:8000

/ → Home (login required)
/register/ → Register
/login/ → Login
/logout/ → Logout
/admin/ → Admin panel

## Notes
Uses Django built-in authentication system with protected routes and staff-only access.
