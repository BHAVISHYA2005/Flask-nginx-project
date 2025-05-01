# 🐳 Flask-NGINX DevOps Project

A **Flask web application** with an **NGINX reverse proxy and caching**, containerized using Docker Compose. This project was built to learn foundational DevOps concepts such as containerization, reverse proxy configuration, and caching.

---

## 🧩 Features

- **Flask Backend**: Serves a simple JSON endpoint with a simulated delay to demonstrate caching.
- **NGINX Reverse Proxy**: Forwards requests to the Flask app and caches responses for improved performance.
- **Docker Compose**: Orchestrates Flask and NGINX containers for easy setup and portability.
- **Caching**: NGINX caches responses for 15 seconds (configurable) to reduce backend load.

---

## 🛠 Prerequisites

- Docker (with Docker Compose plugin)
- Git

---

## ⚙️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/BHAVISHYA2005/Flask-nginx-project.git
cd Flask-nginx-project

### 2. Run the Application Using Docker Compose

'''bash
docker compose up --build

### 

🔮 Future Improvements
Add CI/CD pipeline using GitHub Actions.

Secure the application with SSL/TLS using NGINX.

Deploy the app to a cloud platform like AWS, Render, or Railway.


