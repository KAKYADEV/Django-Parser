![Python](https://img.shields.io/badge/Python-3.12-blue)
![Django](https://img.shields.io/badge/Django-Backend-green)
![Docker](https://img.shields.io/badge/Docker-Containerized-blue)
![Celery](https://img.shields.io/badge/Celery-Async-orange)

# 🚀 Django Parser Service

## 📌 About the Project

A production-oriented backend service for asynchronous web page parsing.

This project started as an exploration of how web applications actually work under the hood.

After building a simple parser earlier, I became interested in how requests and responses flow through a system, how services communicate, and how real backend architecture differs from a typical development setup.

Instead of creating another simple pet project, I wanted to build something closer to a production-like system. My goal was to understand:

- how services interact within a network  
- how asynchronous tasks are handled  
- how a backend system is structured in production  

As a result, I built a service that collects and analyzes key metrics relevant for website visibility and SEO.  

While the analysis itself is relatively simple, the project proved useful in practice — it even helped identify missing elements in a real-world website.

---

## 🧰 Tech Stack

* **Backend:** Django, Gunicorn
* **Async Processing:** Celery + Redis
* **Web Server:** Nginx (reverse proxy, static files)
* **Infrastructure:** Docker, Docker Compose

---

## 🏗 Architecture

```
Client
  ↓
Nginx (entry point, static, proxy)
  ↓
Django (Gunicorn)
  ↓
Celery Worker → Redis (broker)
```

---

## ⚙️ How It Works

1. A client sends a request to the server
2. Nginx receives the request and proxies it to Django
3. Django processes the request and sends a task to Celery
4. Celery pushes the task to Redis (message broker)
5. Worker picks up the task and processes it asynchronously
6. The result is logged and returned when ready

---

## ✨ Features

* Asynchronous web page parsing
* Task queue processing using Celery
* Service isolation via Docker
* Static file handling through Nginx
* Logging for tasks and errors
* Production-oriented architecture

---

## 🚀 Quick Start

```bash
git clone https://github.com/KAKYADEV/Django-Parser.git
cd django-parser
cp .env.example .env
docker compose up --build
```

Open in browser:
👉 http://localhost/

---

## 🔐 Environment Variables

See `.env.example`

Main variables:

* `SECRET_KEY`
* `DEBUG`
* `ALLOWED_HOSTS`

---

## 📁 Project Structure

```
django-parser/
├── parser/              # Django project
├── nginx/               # Nginx configuration
├── docker-compose.yml
├── Dockerfile
└── .env.example
```

---

## 🧠 What I Learned

This project was less about using tools and more about understanding how systems behave in a production-like environment.

### 🔧 Working with DEBUG=False

Switching Django to production mode (`DEBUG=False`) exposed real-world limitations:

- static files stopped working  
- Django could no longer handle everything on its own  

This forced me to introduce Nginx as a dedicated web server for serving static files and handling requests properly.

---

### 🐳 Docker & Networking

One of the biggest challenges was understanding how services communicate inside Docker.

Key takeaways:

- services communicate within an internal network, not via localhost  
- each service must be addressed by its container name  
- configuration differs significantly from local development  

I also encountered issues with Docker caching, where outdated layers caused unexpected behavior during rebuilds.

---

### ⚙️ Celery & Asynchronous Processing

Initially, I underestimated the importance of proper task separation.

At first, I considered handling tasks more directly, but realized that:

- asynchronous workers should be isolated  
- task queues improve scalability  
- improper setup leads to delays and bottlenecks  

Understanding the roles of broker (Redis) and worker was a key step.

---

### 🧠 Core Insight

The most challenging part was realizing that services do not "just work together" —  
they must be explicitly configured to communicate.

This changed my understanding of backend systems from "code that runs" to  
"independent services that interact through well-defined boundaries".

---

## 🔧 Key Engineering Decisions

* Static files are served by Nginx instead of Django
* All services are containerized and isolated
* Only Nginx is exposed to the outside network
* Celery worker uses the same image as Django for consistency

---

## 📈 Future Improvements

* HTTPS (Let's Encrypt)
* Rate limiting & security hardening
* Monitoring (Prometheus / Grafana)
* CI/CD pipeline

---

## 🧪 Notes

* Django is not exposed publicly (no direct port access)
* The system is designed to simulate a production-like environment locally

---

## 💬 Personal Reflection

The goal of this project was not to solve a single problem, but to explore a broad and complex area of backend development.

### 🔥 Biggest Challenge

The hardest part was understanding how networking works in practice, especially within Docker.  
At times, the system would not work at all, and the reason was not obvious.

---

### 💡 Key Insight

The biggest realization was that backend development is not just about writing code —  
it's about understanding how systems communicate and operate as a whole.

---

### 🔄 What I Would Do Differently

If I started again, I would spend less time focusing on individual libraries and more time understanding:

- system design fundamentals  
- networking concepts  
- how applications behave at a lower level  

This would make the learning process much more efficient.

---
