# Mindful Moments+ 🌱

A Django-based mood tracking application that helps users monitor their emotional well-being through mindful reflection and mood logging.

## Features ✨

- **User Authentication**: Secure signup, login, and logout with personalized messages
- **Mood Tracking**: Log daily moods with emoji indicators and intensity ratings (1-10)
- **Personal Dashboard**: View recent mood entries and access mindfulness tips
- **Responsive Design**: Mobile-friendly interface using Bootstrap 5
- **Secure Data**: User-specific mood entries with privacy protection

## Technologies Used 🛠️

- **Backend**: Django 4.2.23, Python
- **Database**: PostgreSQL (Neon Cloud)
- **Frontend**: Bootstrap 5.3.0, HTML5, CSS3
- **Deployment**: Heroku with WhiteNoise for static files
- **Security**: Environment variables for sensitive data

## Installation & Setup 🚀

### Prerequisites
- Python 3.11+
- PostgreSQL database
- Git

### Local Development
1. Clone the repository:
   ```bash
   git clone https://github.com/ZaenbA/capstone-project.git
   cd capstone-project
   ```

2. Create virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Set up environment variables (create `env.py`):
   ```python
   import os
   os.environ.setdefault('SECRET_KEY', 'your-secret-key')
   os.environ.setdefault('DEBUG', 'True')
   # Add database configuration
   ```

5. Run migrations:
   ```bash
   python manage.py migrate
   ```

6. Start development server:
   ```bash
   python manage.py runserver
   ```

## Project Structure 📁

```
capstone-project/
├── config/                 # Django settings and configuration
├── Mindful_Moments/        # Main app (authentication, dashboard)
├── moods/                  # Mood tracking app
├── templates/              # HTML templates
├── static/                 # CSS and static files
├── requirements.txt        # Python dependencies
└── README.md              # Project documentation
```

## Live Demo 🌐

Visit the live application: [Mindful Moments+](https://mindful-moments101-4d3848fc02ce.herokuapp.com/)

## Contributing 🤝

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests and documentation
5. Submit a pull request

## License 📄

This project is open source and available under the [MIT License](LICENSE).

## Author 👨‍💻

Created by [ZaenbA](https://github.com/ZaenbA) as a capstone project for mindful mood tracking.