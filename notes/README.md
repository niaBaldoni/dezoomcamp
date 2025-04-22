# Notes

This folder contains all the notes I'm taking as I progress through the online bootcamp. It includes summaries, explanations, diagrams, and anything else that helps me understand the material better. Below is a table of contents to help navigate the different topics.

## Module 1: Containerization and Infrastructure as Code

In the first half of this module, we start to use and understand Docker. We begin by setting up a basic ingestion pipeline to load New York taxi data into a Postgres database, connecting to it via pgAdmin to explore the ingested data. To streamline the process, we refactor the Jupyter Notebook into a Python script, which we then Dockerize to ensure portability and reproducibility. Finally, we simplify infrastructure management by using Docker Compose — allowing us to define and orchestrate both Postgres and pgAdmin in a single configuration file.

### Table of Contents [(detailed table of contents here)](week_1/README.md)

- [Ingesting NY Taxi Data to Postgres](week_1/1.2.2_Ingesting_NY_Taxi_Data_to_Postgres.md)

- [Connecting pgAdmin and Postgres](week_1/1.2.3_Connecting_pgAdmin_and_Postgres.md)

- [Dockerizing the Ingestion Script](week_1/1.2.4_Dockerizing_the_Ingestion_Script.md)

- [Running Postgres and pgAdmin with Docker-Compose](1.2.5_Docker-Compose.md)