# Flask Notes App

A simple web application for creating and managing notes, built with Flask.

## Features

- User registration and authentication
- Create, read, update, and delete notes
- Responsive design
- Docker support for easy deployment

## Installation

### Prerequisites

- Python 3.9+
- pip
- Docker and Docker Compose (optional)

### Local Setup

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/flask-notes-app.git
   cd flask-notes-app
   ```

2. Create a virtual environment and activate it:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

4. Run the application:
   ```
   python run.py
   ```

5. Access the application at http://localhost:5000

### Docker Setup

1. Build and run the application using Docker Compose:
   ```
   docker-compose up --build
   ```

2. Access the application at http://localhost:5000

## Project Structure

```
flask-notes-app/
├── app/
│   ├── __init__.py         # Flask application initialization
│   ├── models.py           # Database models
│   ├── routes.py           # Application routes
│   ├── static/             # Static files (CSS, JS, images)
│   │   └── css/
│   │       └── style.css
│   └── templates/          # HTML templates
│       ├── base.html       # Base template with common elements
│       ├── index.html      # Home page
│       ├── login.html      # Login page
│       ├── register.html   # Registration page
│       ├── notes.html      # Notes list page
│       ├── create_note.html # Create note page
│       └── edit_note.html  # Edit note page
├── Dockerfile              # Docker configuration
├── docker-compose.yml      # Docker Compose configuration
├── requirements.txt        # Python dependencies
├── config.py               # Application configuration
├── run.py                  # Application entry point
└── README.md               # Project documentation
```

## License

This project is licensed under the MIT License - see the LICENSE file for details.