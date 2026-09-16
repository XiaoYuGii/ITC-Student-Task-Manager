[README.md](https://github.com/user-attachments/files/32286842/README.md)
# ITC Student Task Manager
Portfolio-ready full-stack project: Flutter mobile app + Django REST Framework API.

## Features
- Register and login with token authentication
- Create, read, update and delete tasks
- To Do / In Progress / Done workflow
- Low / Medium / High priority
- Filter tasks by status
- SQLite persistence

## Backend setup
```bash
cd backend
python -m venv .venv
# Windows: .venv\\Scripts\\activate
# macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py runserver 0.0.0.0:8000
```

## Flutter setup
Open a second terminal:
```bash
cd mobile
flutter pub get
flutter run
```
The API URL is `http://10.0.2.2:8000/api` for Android Emulator. For a physical Android phone, edit `lib/services/api_service.dart` and replace `10.0.2.2` with your computer's LAN IP. Keep phone and computer on the same network.

## API endpoints
- POST `/api/register/`
- POST `/api/login/`
- GET/POST `/api/tasks/`
- GET/PUT/DELETE `/api/tasks/<id>/`

## Portfolio description
Built a full-stack mobile task-management application using Flutter/Dart and Django REST Framework. Implemented token authentication, REST API integration, CRUD operations, status filtering, priorities, and SQLite persistence.
