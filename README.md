# Pen Test Database

A comprehensive, searchable database of penetration testing techniques, powered by a modern web stack. This application allows security professionals to quickly find, categorize, and understand various exploitation vectors, command injections, and security bypass methods.

## Features

- **Advanced Search**: Instant search with FTS (Full-Text Search) capabilities globally across titles and descriptions.
- **Contextual Summaries**: Automatically inferred "Purpose" fields provide quick context for each technique (e.g., "Methods to circumvent security controls").
- **Rich Details**: View detailed technique information including code snippets, platforms, and related technologies, computed and rendered with Markdown support.
- **Categorization**: Filterable by Attack Vector, Security Domain, and Operating System.
- **Modern UI**: Dark-themed, responsive interface built with React and TailwindCSS.

## Tech Stack

- **Frontend**: React, Vite, TypeScript, TailwindCSS
- **Backend**: Python, FastAPI
- **Database**: SQLite (with FTS5)
- **Containerization**: Docker, Docker Compose
- **Proxy**: Nginx

## Getting Started

### Prerequisites

- [Docker](https://docs.docker.com/get-docker/)
- [Docker Compose](https://docs.docker.com/compose/install/)

### Installation & Running

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd Pen_Test_Database
   ```

2. **Navigate to the application directory:**
   ```bash
   cd Pen_Test_App
   ```

3. **Build and start the services:**
   ```bash
   docker compose up -d --build
   ```

4. **Access the Application:**
   Open your browser and navigate to:
   [http://localhost:9595](http://localhost:9595)

### Stopping the Application

To stop the containers:
```bash
docker compose down
```

## Project Structure

- `backend/`: FastAPI application, database models, search logic, and SQLite database.
- `frontend/`: React application source code.
- `docker-compose.yml`: Service orchestration configuration.

## Data

The database is stored in `backend/pen_test.db` and is mounted as a volume in the backend container for persistence.
