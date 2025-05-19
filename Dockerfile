FROM python:3.12-slim

WORKDIR /app/presales_crew

# Copy only dependency file first for better caching
COPY presales_crew/pyproject.toml ./

RUN pip install --upgrade pip && pip install .[dev]

# Now copy the rest of the source code
COPY presales_crew/ ./

CMD ["crewai", "run"] 