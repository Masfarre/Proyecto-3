# Installation Guide

## Prerequisites
- Python 3.9+
- PostgreSQL
- Redis

## Steps
1. Clone the repository: `git clone https://github.com/your-repo/taskflow.git`
2. Create virtual environment: `python -m venv venv`
3. Activate environment: `source venv/bin/activate` (Linux/Mac) or `venv\Scripts\activate` (Windows)
4. Install dependencies: `pip install -r requirements.txt`
5. Download NLP model: `python -m spacy download en_core_web_sm`
6. Configure environment variables (copy .env.example to .env and set values)
7. Run the application: `flask run`
