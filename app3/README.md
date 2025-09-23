# Django Blog

This project is a simple blog developed using the Django framework. It includes the following features:

*   **BlogPost Model**: A model for blog posts is defined, including title, text, date added, and owner.
*   **Admin Interface**: The BlogPost model is registered with the Django admin panel, allowing for easy management of posts.
*   **Homepage**: Displays all blog posts in chronological order.
*   **Forms for Creating and Editing**: Users can create new posts and edit their existing posts via web forms.
*   **Authentication System**: A user registration, login, and logout system is implemented.
*   **Bootstrap Styling**: The application is styled using Bootstrap for a modern and responsive design.

## Setup and Run

Follow these instructions to set up and run the project on your local machine.

### 1. Clone the Repository

```bash
git clone https://github.com/Shuv1Wolf/web-programming.git
cd web-programming/app3
```

### 2. Create a Virtual Environment and Install Dependencies

```bash
python -m venv .venv
.venv\Scripts\activate # For Windows
# source .venv/bin/activate # For Linux/macOS
pip install -r requirements.txt
```

### 3. Database Setup

Run migrations to create the database tables:

```bash
python manage.py makemigrations blogs
python manage.py migrate
```

### 4. Create a Superuser

Create a superuser to access the Django administration panel:

```bash
python manage.py createsuperuser
```

Follow the prompts in the terminal to create a username, email address, and password.

### 5. Run the Development Server

```bash
python manage.py runserver
```

After starting the server, open your web browser and navigate to `http://127.0.0.1:8000/`.

### 6. Accessing the Admin Panel

You can access the admin panel at `http://127.0.0.1:8000/admin/` and log in using the superuser credentials created in step 4. Here you can create and manage blog posts.

## Usage

*   **View Posts**: The homepage (`http://127.0.0.1:8000/`) displays all blog posts.
*   **Registration**: Unregistered users can register via the "Register" link in the navigation bar.
*   **Login/Logout**: Authenticated users will see their username and a "Logout" link. Unregistered users will see a "Login" link.
*   **Create New Post**: Authenticated users can add a new post by clicking the "Add new post" link on the homepage.
*   **Edit Post**: Authenticated users can edit their posts by clicking the "Edit post" link under the respective post.
