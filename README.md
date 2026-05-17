# Django Class Project

User authentication app — register, login, logout, change password.

## Run

```bash
.\env\Scripts\activate    # Windows
source env/bin/activate   # Mac/Linux

python manage.py runserver
```

Open `http://127.0.0.1:8000`

## Pages

| URL | Access |
|-----|--------|
| `/` | Home (login required) |
| `/register/` | Register |
| `/login/` | Login |
| `/logout/` | Logout |
| `/about/` | About (login required) |
| `/change-password/` | Change password (login required) |
| `/admin/` | Admin panel |

## Create admin user

```bash
python manage.py createsuperuser
```
