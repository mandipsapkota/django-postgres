# django-postgres

## Django Setup
1. Setup a venv
2. Install required dependencies
3. `django-admin startproject --name-- `

## Django file structure

project_name
|__ __init.py
|__ settings.py
|__ urls.py
|__ wsgi.py -> How our python web app and web server communicates

manage.py

## Some basics
We can run our server with this command:
` python3 manage.py runserver`

main/admin returns a admin url

## Adding a app 

A blog section is a app. Astore section is a app. It just seperates different section of our project, even making it usable for other projects.

Query to start an app:
```bash
django-admin startapp blog
```

New folder structure:
``` bash
├── blog
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   └── views.py
├── blogapp
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── db.sqlite3
└── manage.py
```

## Creating a view

Go to `blog/views.py`

Add a code 
```python
from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse("<h1>Welcome to blog Homepage<h1>")
```

## Adding urls
Create `urls.py` in `../blog`

Add this to create paths:

```py
from django.urls import path
from . import views 

urlpatterns = [
    # This is how we create a path. We specify route, view that handles the logic behind the url, and a app-specific name to avoid further issues.
    path('' , views.home, name = "blog-home")
]
```
This wont work yet. We need to point this app from our project, from a whole project level.

We need to append this in urlpatterns of project-level urls.py in order to run it. But, now djngos default url wont be shown.
```py
## Specifying a app path
    path('blog/', include('blog.urls'))
```

