Flask-NGINX DevOps Project
A Flask web application with an NGINX reverse proxy and caching, containerized using Docker Compose. This project was built to learn foundational DevOps concepts such as containerization, reverse proxy configuration, and caching.
Features

Flask Backend: Serves a simple JSON endpoint with a simulated delay to demonstrate caching.
NGINX Reverse Proxy: Forwards requests to the Flask app and caches responses for improved performance.
Docker Compose: Orchestrates Flask and NGINX containers for easy setup and portability.
Caching: NGINX caches responses for 15 seconds (configurable) to reduce backend load.

Prerequisites

Docker (with Docker Compose plugin)
Git

Setup Instructions

Clone the Repository:
git clone https://github.com/BHAVISHYA2005/Flask-nginx-project.git
cd Flask-nginx-project


Run the Application:
docker compose up --build


This builds the Flask app container and starts NGINX and Flask services.
Access the app at http://localhost:80.


Test the Application:

Open a browser and visit http://localhost:80 to see:{"message": "Welcome to DevOps!", "timestamp": "..."}


Or use:curl http://localhost:80




Verify Caching:

Check the cache status:curl -I http://localhost:80


Look for X-Cache-Status: MISS (first request) or HIT (cached requests within 15 seconds).


Stop the Application:
docker compose down



Project Structure
Flask-nginx-project/
├── flask_app/
│   ├── app.py              # Flask application code
│   ├── requirements.txt    # Python dependencies
│   ├── Dockerfile          # Docker configuration for Flask
├── nginx/
│   ├── nginx.conf          # NGINX configuration for reverse proxy and caching
├── nginx_cache/            # Directory for NGINX cache (excluded in .gitignore)
├── docker-compose.yml      # Docker Compose configuration
├── .gitignore              # Git ignore file
├── README.md               # Project documentation

What I Learned

Containerization: Used Docker to package Flask and NGINX services, ensuring consistent environments.
Docker Compose: Orchestrated multiple containers with a single YAML configuration.
NGINX Configuration: Set up a reverse proxy and implemented caching to optimize performance.
Git and GitHub: Managed version control, resolved merge conflicts, and deployed code to a remote repository.
DevOps Workflow: Gained hands-on experience with building, testing, and deploying a containerized application.

Future Improvements

Add CI/CD with GitHub Actions for automated testing and deployment.
Implement SSL/TLS for secure communication using NGINX.
Deploy the app to a cloud platform (e.g., AWS, Render) for public access.

Troubleshooting

Docker Errors: Ensure Docker is running (docker ps) and the daemon is active (sudo systemctl start docker).
NGINX Issues: Check logs with docker logs nginx if http://localhost:80 fails.
Port Conflicts: If port 80 or 5000 is in use, modify docker-compose.yml ports (e.g., 8080:80).

Contributing
Feel free to fork this repository, submit issues, or create pull requests to enhance the project.
License
MIT License (optional, include if you added a license file).
