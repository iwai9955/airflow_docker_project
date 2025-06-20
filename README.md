# Airflow Docker Project for EV Demand Prediction

This is a simple ETL + ML pipeline built with Apache Airflow and Docker to predict Electric Vehicle (EV) charging demand.

## Project Structure

```
airflow_docker_project/
│
├── dags/
│   └── predict_dag.py           # Airflow DAG for running prediction
│
├── config/
│   └── airflow.cfg              # Airflow configuration file
│
├── docker-compose.yaml          # Docker-based deployment setup
├── .gitignore                   # Excludes .env, __pycache__, etc.
```

## Features
- Data ingestion and preprocessing
- Model training (one-time setup)
- Model prediction using scheduled Airflow DAG
- Containerized with Docker

## Getting Started

```bash
git clone https://github.com/iwai9955/airflow_docker_project.git
cd airflow_docker_project
docker-compose up
```

## Use Case
This project demonstrates how to automate machine learning prediction workflows in a reproducible and scalable manner using Airflow.

## Author
Soobok Yoon | PhD in Energy Optimization | Monash University | LinkedIn](https://www.linkedin.com/in/soo-monash)
