# Task Manager

Task Manager is a Django web application for personal task management. Each user can:

- Register and log in  
- Create, edit, and delete tasks  
- Set a title, description, due date, and priority (Low, Medium, High)  
- Mark tasks as completed  
- View a list of their own tasks and task details  

## Technologies

- Python 3.9+  
- Django 5.2.6  
- Bootstrap 4.6  
- SQLite (default development database)  

## Installation and Setup

1. **Clone the repository**  
   ```bash
   git clone https://github.com/Shuv1Wolf/wp_task_manager.git
   cd wp_task_manager
   ```

2. **Create and activate a virtual environment**  
   ```bash
   python -m venv venv
   # Windows
   .\venv\Scripts\activate
   # macOS/Linux
   source venv/bin/activate
   ```

3. **Install dependencies**  
   ```bash
   pip install -r requirements.txt
   ```

4. **Apply migrations and start the development server**  
   ```bash
   python manage.py migrate
   python manage.py runserver
   ```
   Open your browser at `http://127.0.0.1:8000/`.

## Docker

1. **Build the Docker image**  
   ```bash
   docker build -t task-manager .
   ```
2. **Run the container**  
   ```bash
   docker run -it --rm -p 8000:8000 task-manager
   ```
   The application will be available at `http://localhost:8000/`.

## Project Structure

```
task_manager/
├─ task_manager/        # Project settings and URLs  
├─ tasks/               # Task management application  
├─ users/               # Authentication application  
├─ templates/           # Global and app-specific templates  
├─ venv/                # Virtual environment  
├─ db.sqlite3           # SQLite database  
├─ Dockerfile  
├─ requirements.txt  
├─ README.md  
```

## License

This project is licensed under the MIT License.
