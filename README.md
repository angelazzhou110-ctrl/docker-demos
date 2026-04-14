# Dockerized R Object Demo

This project demonstrates how to:

- Load an R object (`.rds`)
- Extract information from it using R
- Run everything inside a Docker container

## How to Run

```bash
docker build -t r-object-demo .
docker run --rm r-object-demo
