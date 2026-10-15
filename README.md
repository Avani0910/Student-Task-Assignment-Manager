# Student Task and Assignment Manager
A Django project using Python, HTML, CSS and SQLite. No JavaScript is used.

## Features
- Register, log in and log out
- Add, edit, complete/reopen and delete assignments
- Due dates, priorities, descriptions and status
- Users can only access their own assignments

## Run on Windows PowerShell
```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python manage.py makemigrations tasks
python manage.py migrate
python manage.py runserver
```
Open http://127.0.0.1:8000/ in your browser.
