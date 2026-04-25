Django Parser Service
Overview

A production-like backend service for parsing web pages with asynchronous task processing.

The project demonstrates a real-world architecture approach:

separation of web server and application
asynchronous task queue
containerized services

Tech Stack
Backend: Django, Gunicorn
Async: Celery + Redis
Web server: Nginx (reverse proxy, static files)
Infrastructure: Docker, Docker Compose

Architecture
Client
  ↓
Nginx (entry point, static, proxy)
  ↓
Django (Gunicorn)
  ↓
Celery Worker → Redis (broker)

Key decisions
Static files are served by Nginx, not Django
All services are containerized and isolated
Only Nginx is exposed to the outside network

Features
Web page parsing (example: extracting page title)
Asynchronous task processing with Celery
Logging for tasks and errors
Production-oriented setup

Quick Start
git clone https://github.com/KAKYADEV/Django-Parser.git
cd django-parser
cp .env.example .env
docker compose up --build

Open in browser:
http://localhost/

Environment variables
See .env.example

Main variables:
SECRET_KEY
DEBUG
ALLOWED_HOSTS

Project Structure (simplified)
django-parser/
├── parser/              # Django project
├── nginx/               # Nginx configuration
├── docker-compose.yml
├── Dockerfile
└── .env.example

What I Practiced
Designing production-like architecture
Working with Docker (multi-service setup)
Configuring Nginx as a reverse proxy
Service responsibility separation
Using task queues (Celery + Redis)
Managing static files in production
Future Improvements
HTTPS (Let's Encrypt)
Rate limiting and security hardening
Monitoring (Prometheus / Grafana)
CI/CD pipeline

Notes
Django is not exposed publicly (no direct port access)
Celery worker uses the same Docker image as Django to ensure a consistent runtime environment