# Mood Tracker – Dockerized Setup

This guide walks you through the steps taken to set up the `mood-tracker` project using Docker and Docker Compose with a PostgreSQL dependency.

---

## 🐳 Requirements

* Docker (v26+)
* Docker Compose (v2+ recommended)
* Linux shell access (root or sudo privileges)

---

## ⚖️ Installation Steps

### 1. Install Docker

```bash
sudo apt update
sudo apt install docker.io -y
sudo systemctl start docker
sudo systemctl enable docker
```

### 2. Install Docker Compose (v2.x)

Remove any broken symlinks or old versions:

```bash
sudo rm -f /usr/bin/docker-compose /usr/local/bin/docker-compose
```

Install the latest version:

```bash
sudo curl -L "https://github.com/docker/compose/releases/download/v2.18.1/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose
```

Verify version:

```bash
docker-compose --version
```

---

## 📦 Project Setup

### 3. Upload Project to VPS

Instead of cloning the project from GitHub, zip your project folder locally, then copy it to your VPS using `scp`:

```bash
scp mood-tracker.zip root@your-vps-ip:/root/
```

SSH into your VPS:

```bash
ssh root@your-vps-ip
```

Then unzip the project and navigate into it:

```bash
unzip mood-tracker.zip
cd mood-tracker
```

### 4. Create `docker-compose.yml`

Here’s the `docker-compose.yml` file used in the setup:

```yaml
version: '3'

services:
  db:
    image: postgres:13
    environment:
      POSTGRES_DB: moodtracker
      POSTGRES_USER: user
      POSTGRES_PASSWORD: password
    ports:
      - "5432:5432"
    healthcheck:
      test: ["CMD", "pg_isready", "-U", "user", "-d", "moodtracker"]
      interval: 10s
      retries: 5
      start_period: 30s
      timeout: 5s
    networks:
      - moodtracker_network

  web:
    build:
      context: .
      dockerfile: Dockerfile
    ports:
      - "8000:8000"
    depends_on:
      - db
    networks:
      - moodtracker_network

networks:
  moodtracker_network:
    driver: bridge
```

This configuration defines two services: `db` (PostgreSQL) and `web` (your application).

* The PostgreSQL database is configured with a custom database, username, and password.
* The `healthcheck` ensures the database is ready before the app tries to connect.
* The `web` service is built from the local Dockerfile and exposed on port `8000`, allowing you to access the app via `http://your-vps-ip:8000`.
* Services are connected via a shared Docker bridge network.

---

## 🚀 Run the Application

```bash
docker-compose up --build
```

To shut down the containers and remove volumes:

```bash
docker-compose down -v
```

---

## 🔪 Verify Setup

Check container status:

```bash
docker ps
```

View logs:

```bash
docker-compose logs
```

---

## 🐞 Troubleshooting

### ⚖️ Issue: `KeyError: 'ContainerConfig'`

This is typically caused by:

* Incompatible Docker Compose version (fixed by upgrading to v2+)
* Misconfigured `docker-compose.yml`

### ⚖️ Issue: `No module named 'distutils'`

Install missing system dependencies:

```bash
sudo apt install python3-distutils -y
```

---

## ✍️ Author

MOHAMED MIHAMMI
📧 [mmim22138@gmail.com](mailto:mmim22138@gmail.com)
