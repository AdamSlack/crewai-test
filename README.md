# CrewAI Python Project

This project is a Python application leveraging CrewAI, containerized using Docker. All Python code resides in the `presales_crew/` directory. The application is designed to be run exclusively via Docker Compose, ensuring a consistent and isolated environment.

## Quick Start

1. Build and start the application:
   ```sh
   docker compose up --build
   ```

2. Access the running application as described in the logs or documentation.

## Project Structure

- `presales_crew/` - All Python source code and modules
- `Dockerfile` - Container build instructions
- `docker-compose.yml` - Multi-container orchestration

## Requirements

- Docker
- Docker Compose

## Environment Variables

To configure secrets and environment variables, create a `.env` file in the `presales_crew/` directory. Use the provided `.env.example` file in the same directory as a template:

1. Copy `.env.example` to `.env`:
   ```sh
   cp presales_crew/.env.example presales_crew/.env
   ```
2. Open `presales_crew/.env` and add the required secrets, such as your `OPENAI_API_KEY`.

**Do not commit your `.env` file to version control.**

## Notes

- Do not run Python locally; use Docker Compose for all development and execution.
- Outputs generated by the crew are stored in the `@outputs` directory. Check this directory for results and artifacts produced by the application.

## Running Tests

To run the unit tests in a containerized environment:

1. Build the Docker image (if not already built):
   ```sh
   docker compose build
   ```

2. Run the tests using the test service:
   ```sh
   docker compose run --rm presales-crew-tests
   ```

This will execute all tests in the `presales_crew/tests` directory using pytest inside the container.