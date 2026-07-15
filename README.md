# 📝 Django To-Do List

A clean and beginner-friendly **To-Do List web application** built with **Django**. The application allows users to create, update, complete, and delete (move to trash) tasks through a simple and responsive interface.

---

## 📸 Features

* ➕ Add new tasks
* ✏️ Update existing tasks
* ✅ Mark tasks as completed
* 🗑️ Move tasks to Trash
* 📂 View Completed Tasks
* ♻️ View Deleted (Trash) Tasks
* 🎨 Modern and responsive user interface
* 💾 SQLite database integration

---

# 🏗️ Project Architecture

```
todo_list/
│
├── todo_list/                 # Django Project
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── app/                       # Django Application
│   ├── migrations/
│   ├── templates/
│   │   ├── home.html
│   │   ├── add.html
│   │   ├── update.html
│   │   ├── completed.html
│   │   ├── trash.html
│   │   └── about.html
│   ├── admin.py
│   ├── models.py
│   ├── views.py
│   └── urls.py
│
├── templates/
│   ├── main.html
│   └── nav.html
│
├── static/
│   └── css/
│       └── style.css
│
├── db.sqlite3
├── manage.py
└── README.md
```

---

# ⚙️ Technologies Used

| Technology | Version                 |
| ---------- | ----------------------- |
| Python     | 3.x                     |
| Django     | 5.2.x                   |
| HTML5      | Latest                  |
| CSS3       | Latest                  |
| SQLite     | Default Django Database |

---

# 🚀 Application Workflow

### Step 1 — Home Page

The application displays all active tasks stored in the **Task** table.

```
Task.objects.all()
```

---

### Step 2 — Add Task

The user enters

* Task Title
* Task Description

The task is stored in the database.

```
Task
```

---

### Step 3 — Update Task

The selected task is fetched using its primary key.

```
Task.objects.get(id=pk)
```

The task information is updated.

---

### Step 4 — Complete Task

When a task is completed,

* Data is copied to **CompleteTask**
* Original task is deleted

```
Task
      ↓
CompleteTask
```

---

### Step 5 — Delete Task

When Delete is clicked,

* Data is copied into **Trash**
* Original task is removed

```
Task
      ↓
Trash
```

---

# 🌐 URL Routing

| URL                | Description            |
| ------------------ | ---------------------- |
| `/`                | Home Page              |
| `/add/`            | Add New Task           |
| `/update/<pk>/`    | Update Existing Task   |
| `/completed/<pk>/` | Move Task to Completed |
| `/complete/`       | View Completed Tasks   |
| `/hdelete/<pk>/`   | Move Task to Trash     |
| `/trash/`          | View Deleted Tasks     |
| `/about/`          | About Page             |
| `/admin/`          | Django Admin           |

---

# 🗄️ Database Models

## Task

| Field | Type          |
| ----- | ------------- |
| title | CharField(30) |
| desc  | CharField(30) |

---

## CompleteTask

| Field | Type          |
| ----- | ------------- |
| title | CharField(30) |
| desc  | CharField(30) |

---

## Trash

| Field | Type          |
| ----- | ------------- |
| title | CharField(30) |
| desc  | CharField(30) |

---

# 📊 Data Flow

```
             User
               │
               ▼
        Django URL Routing
               │
               ▼
            View Function
               │
               ▼
        Database (SQLite)
               │
               ▼
          HTML Template
               │
               ▼
            Browser
```

---

# 🛠️ Installation

## 1. Clone the Repository

```bash
git clone https://github.com/your-username/todo-list.git
```

```bash
cd todo-list
```

---

## 2. Create Virtual Environment

```bash
python -m venv venv
```

### Activate

**Windows**

```bash
venv\Scripts\activate
```

**Linux / macOS**

```bash
source venv/bin/activate
```

---

## 3. Install Django

```bash
pip install django
```

---

## 4. Apply Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

---

## 5. Start Development Server

```bash
python manage.py runserver
```

---

## 6. Open in Browser

```
http://127.0.0.1:8000/
```

Other Pages

```
http://127.0.0.1:8000/add/
http://127.0.0.1:8000/complete/
http://127.0.0.1:8000/trash/
http://127.0.0.1:8000/about/
http://127.0.0.1:8000/admin/
```

---

# 📌 Project Highlights

* Clean Django Project Structure
* Beginner Friendly
* Simple CRUD Operations
* Separate Completed and Trash Modules
* Responsive UI
* SQLite Database
* Easy to Extend
* Well Organized Templates

---

# 🔮 Future Improvements

* 👤 User Authentication (Login/Register)
* 📅 Due Dates
* ⭐ Task Priorities
* 🔍 Search Tasks
* 📊 Dashboard & Statistics
* 🌙 Dark Mode
* 📱 Mobile Responsive Improvements
* 🏷️ Task Categories
* 📌 Pin Important Tasks
* 📤 Export Tasks to PDF/Excel
* 🔔 Email or Browser Notifications

---

# 🤝 Contributing

Contributions are welcome!

1. Fork the repository
2. Create a feature branch

```bash
git checkout -b feature-name
```

3. Commit your changes

```bash
git commit -m "Added new feature"
```

4. Push your branch

```bash
git push origin feature-name
```

5. Open a Pull Request

---

# 📝 License

This project is open-source and available under the **MIT License**.

---

# 👨‍💻 Author

**Developed with ❤️ using Django**

If you found this project helpful, consider giving it a ⭐ on GitHub!

