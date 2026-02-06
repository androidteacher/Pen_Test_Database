# Pen Test Database

A comprehensive, searchable database of penetration testing techniques. This application allows security professionals to quickly find, categorize, and understand various exploitation vectors, command injections, and security bypass methods.


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
