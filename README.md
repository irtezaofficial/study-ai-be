# Study-AI-BE

Backend server for the **Study AI** platform, implemented as a Python web application (e.g., Django or Flask), powering AI-assisted study tools through APIs.

##  About

This repository contains the **backend** logic for **Study AI**, including AI-powered modules such as:

- `QuestionGenerator` – automatically creates study questions  
- `QuizChecker` – evaluates quiz responses  
- `Summerization` – generates summaries of input content  
- `AnswereChecker` – verifies answer correctness  

The backend exposes these services via APIs and stores data in a SQLite database (or any configured DB engine).

---

##  Features

- Automated question and quiz utilities  
- Text summarization capabilities  
- RESTful API endpoints for frontend consumption  
- Local SQLite database for ease of development  
- Easily extensible architecture for AI integrations  

---

##  Technologies Used

- **Python** – Primary backend language  
- **Django** (if applicable) – Web framework (indicated by `manage.py`)  
- **SQLite** – Default development database (`db.sqlite3`)  
- AI modules (custom or via third-party libraries) for summarization, quiz generation, etc.

---

##  Setup & Installation

###  Prerequisites

Make sure you have installed:

- [Python 3.8+](https://www.python.org/)  
- `pip` (Python package installer)  
- Optional: a virtual environment tool such as `venv` or `virtualenv`

###  Clone & Install

```bash
git clone https://github.com/irtezaofficial/study-ai-be.git
cd study-ai-be
python -m venv venv
# On macOS/Linux:
source venv/bin/activate
# On Windows:
venv\Scripts\activate
python manage.py runserver
```

###  Project Structure

```
study-ai-be/
├── AnswereChecker.py         # AI logic for answer validation
├── QuestionGenerator.py      # Logic to generate quiz questions
├── QuizChecker.py            # Quiz response evaluation logic
├── Summerization.py          # Text summarization module
├── manage.py                 # Django command-line utility (if Django)
├── db.sqlite3                # SQLite database file
├── requirements.txt          # Python dependencies
├── backend_app/              # (if Django) app directory
│   ├── views.py
│   ├── serializers.py
│   ├── urls.py
│   └── models.py
└── README.md                 # (this documentation)
```

