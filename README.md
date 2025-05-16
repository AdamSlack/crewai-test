# CrewAI Python Project

This project is a Python application leveraging CrewAI, containerized using Docker. All Python code resides in the `crewai_project/` directory. The application is designed to be run exclusively via Docker Compose, ensuring a consistent and isolated environment.

## Quick Start

1. Build and start the application:
   ```sh
   docker compose up --build
   ```

2. Access the running application as described in the logs or documentation.

## Project Structure

- `crewai_project/` - All Python source code and modules
- `Dockerfile` - Container build instructions
- `docker-compose.yml` - Multi-container orchestration

## Requirements

- Docker
- Docker Compose

## Notes

- Do not run Python locally; use Docker Compose for all development and execution.