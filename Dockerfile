FROM python:3.12-slim

WORKDIR /app

COPY crewai_project/requirements.txt ./crewai_project/requirements.txt
RUN pip install --upgrade pip \
    && pip install -r crewai_project/requirements.txt

COPY crewai_project/ ./crewai_project/

WORKDIR /app/crewai_project

ENTRYPOINT ["python", "main.py"] 