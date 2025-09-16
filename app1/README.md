# Learning Log

Learning Log is a web application built with Django that allows users to keep a log of topics they're learning about. For each topic, users can add entries to record their thoughts and progress.

## Features

*   **User Authentication:** Users can register, log in, and log out.
*   **Topic Management:** Authenticated users can create, view, and manage their own learning topics.
*   **Entry Management:** For each topic, users can add, edit, and delete entries.
*   **Private Topics:** Each user's topics and entries are private and only accessible to them.

## Technologies Used

*   **Backend:** Django 4.2.24
*   **Frontend:** HTML, CSS (with Bootstrap 4)
*   **Database:** SQLite (default for Django development)
*   **Dependencies:**
    *   `asgiref==3.9.1`
    *   `beautifulsoup4==4.13.5`
    *   `django-bootstrap4==25.2`
    *   `soupsieve==2.8`
    *   `sqlparse==0.5.3`
    *   `typing_extensions==4.15.0`
    *   `tzdata==2025.2`

## Setup and Installation

Follow these steps to get your development environment up and running:

### 1. Clone the Repository

```bash
git clone https://github.com/Shuv1Wolf/wp_lerning_log.git
cd wp_lerning_log
```

### 2. Create a Virtual Environment

It's recommended to use a virtual environment to manage project dependencies.

```bash
python -m venv venv
```

### 3. Activate the Virtual Environment

*   **On Windows:**
    ```bash
    .\venv\Scripts\activate
    ```
*   **On macOS/Linux:**
    ```bash
    source venv/bin/activate
    ```

### 4. Install Dependencies

Install the required Python packages using `pip`:

```bash
pip install -r requirements.txt
```

### 5. Apply Migrations

Apply the database migrations to set up the database schema:

```bash
python manage.py migrate
```

### 6. Create a Superuser (Optional)

To access the Django admin interface, you can create a superuser:

```bash
python manage.py createsuperuser
```

Follow the prompts to set up a username, email, and password.

### 7. Run the Development Server

Start the Django development server:

```bash
python manage.py runserver
```

The application will be accessible at `http://127.0.0.1:8000/` in your web browser.

## Docker Setup

This project also includes a `Dockerfile` and `.dockerignore` for containerization.

### 1. Build the Docker Image

```bash
docker build -t learning-log .
```

### 2. Run the Docker Container

```bash
docker run -p 8000:8000 learning-log
```

The application will be accessible at `http://localhost:8000/` after the container starts.

## Project Structure

*   `learning_log/`: Main project settings, URL configurations.
*   `learning_logs/`: Core application for managing topics and entries.
*   `users/`: Application for user authentication and registration.
*   `templates/`: HTML templates for the web application.
*   `requirements.txt`: Lists all Python dependencies.
*   `Dockerfile`: Docker configuration for containerization.
*   `.gitignore`: Specifies intentionally untracked files to ignore.
*   `.dockerignore`: Specifies files and directories to ignore when building Docker images.
