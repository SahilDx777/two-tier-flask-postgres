# Two-Tier Flask Application with PostgreSQL | Docker + Jenkins CI/CD

A production-style **two-tier web application** built using **Flask** and **PostgreSQL**, containerized with **Docker**, deployed on **AWS EC2**, and automated using **Jenkins CI/CD**.

This project demonstrates real-world DevOps practices including container orchestration, CI/CD pipelines, persistent storage, and application debugging.

---

## 🚀 Tech Stack

- **Cloud**: AWS EC2
- **OS**: Ubuntu
- **Backend**: Flask (Python)
- **Database**: PostgreSQL
- **Containerization**: Docker
- **Orchestration**: Docker Compose
- **CI/CD**: Jenkins
- **Version Control**: Git & GitHub

---

## 🧱 Architecture Overview

This project follows a **Two-Tier Architecture**:

- **Application Tier**: Flask web application
- **Database Tier**: PostgreSQL database

All components run as Docker containers on a single EC2 instance.

---

## 🔄 Architecture Flow

User Browser
|
v
AWS Security Group (Port 5000)
|
v
EC2 Instance (Ubuntu)
|
v
Docker Compose
├── Flask Container (Web App)
|
└── PostgreSQL Container (Database)
|
└── Docker Volume (Persistent Data)

---

## 📦 Project Structure

two-tier-flask-postgres/
├── app/
│ ├── app.py
│ ├── requirements.txt
│ └── templates/
│ └── index.html
├── docker-compose.yml
├── Dockerfile
├── Jenkinsfile
└── README.md


---

## ⚙️ Application Features

- Add users (Create)
- View users (Read)
- Delete users (Delete)
- Persistent database using Docker volumes
- Clean and minimal UI
- CI/CD-based automated deployment

---

## 🔁 CI/CD Pipeline (Jenkins)

On every push to the `main` branch:

1. Jenkins pulls the latest code from GitHub
2. Stops running containers
3. Rebuilds Docker images
4. Deploys updated containers using Docker Compose
5. PostgreSQL data remains intact via Docker volumes

---

## 🛠️ How to Run Locally or on EC2

```bash
docker-compose up -d --build
```
### Access the app!
http://<EC2-PUBLIC-IP>:5000

