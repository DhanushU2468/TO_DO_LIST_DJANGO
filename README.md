# TO_DO_LIST_DJANGO
# ToDo List (Django)

## Overview / Architecture
This project is a simple Django To-Do List app.

### Project layout
- **todo_list/** (Django project)
  - `settings.py` - configuration (installed apps, database, templates, static files)
  - `urls.py` - project-level URL routing
  - `wsgi.py` / `asgi.py` - deployment entrypoints
- **app/** (Django app)
  - `models.py` - database models (Task, CompleteTask, Trash)
  - `views.py` - request handlers (home/add/update/complete/trash/about)
  - `urls.py` - app-level URL routing
  - `templates/` - app templates (home/add/trash/completed/update/about)
- **templates/** (project-level templates)
  - `main.html` - base layout (includes nav + static CSS)
  - `nav.html` - navigation bar included on all pages
- **static/** - static files (CSS)
- **db.sqlite3** - SQLite database file (already present in the repo)

### Request/Response + Data flow
1. **URL routing**
   - `todo_list/urls.py` includes `app.urls`
   - `app/urls.py` maps paths to view functions:
     - `/` → `home`
     - `/add/` → `add`
     - `/update/<pk>/` → `update`
     - `/completed/<pk>/` → `completed` (move to completed list)
     - `/complete/` → `complete` (list completed items)
     - `/hdelete/<pk>/` → `hdelete` (move to trash list)
     - `/trash/` → `trash` (list trashed items)
     - `/about/` → `about`
2. **Views**
   - `home` loads `Task.objects.all()` and renders `home.html`
   - `add` (POST) reads `title` and `description` and creates a `Task`
   - `update` loads a `Task` by `id=pk`, updates it on POST, then redirects to `home`
   - `completed` loads a `Task` by `id=pk`, creates a `CompleteTask`, deletes the original `Task`, then redirects to `complete`
   - `hdelete` loads a `Task` by `id=pk`, creates a `Trash`, deletes the original `Task`, then redirects to `trash`
   - `complete` loads `CompleteTask.objects.all()` and renders `completed.html`
   - `trash` loads `Trash.objects.all()` and renders `trash.html`
3. **Templates**
   - `templates/main.html` is the base layout (`{% include 'nav.html' %}` and `{% block content %}`)
   - `app/templates/home.html` displays current tasks with action links to update/complete/trash

## Database / Models
Defined in `app/models.py`:
- `Task`
  - `title`: CharField(max_length=30)
  - `desc`: CharField(max_length=30)
- `CompleteTask`
  - `title`, `desc`
- `Trash`
  - `title`, `desc`

When you “Complete” or “Delete (Trash)” a task:
- the original `Task` is removed
- a new row is inserted into `CompleteTask` or `Trash`

## Prerequisites
- **Python 3.x**
- **Django** (repo uses Django 5.2.x)
- **SQLite** (included with Python; project uses `db.sqlite3`)

## Setup & Run Commands

### 1) Create a virtual environment (recommended)
```bash
python -m venv venv
```

Activate it:

**Windows (cmd):**
```bash
venv\Scripts\activate
```

### 2) Install dependencies
If you don’t have Django installed yet:
```bash
pip install django
```

### 3) Apply migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### 4) Run the development server
```bash
python manage.py runserver
```

### 5) Open the app in your browser
- `http://127.0.0.1:8000/` (Home)
- `http://127.0.0.1:8000/add/`
- `http://127.0.0.1:8000/complete/`
- `http://127.0.0.1:8000/trash/`
- `http://127.0.0.1:8000/about/`
- `http://127.0.0.1:8000/admin/`

## Notes
- `DEBUG = True` in `todo_list/settings.py` (development mode).
- `title` / `desc` are limited to **30 characters** in the model fields.
