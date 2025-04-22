# Individual containers

## Build the server container
```bash
winpty docker run -it \
    -e POSTGRES_USER="root" \
    -e POSTGRES_PASSWORD="root" \
    -e POSTGRES_DB="ny_taxi" \
    -v D://20_Projects//dezoomcamp//code//week_1//2_docker_sql//ny_taxi_postgres_data:/var/lib/postgresql/data \
    -p 5432:5432 \
    --name pg-database \
    postgres:13

```

## Build the client container
```bash
winpty pgcli -h localhost -p 5432 -u root -d ny_taxi
```

# Network of containers

## Build the network
```bash
winpty docker network create pg-network
```

## Run the database in the network
```bash
winpty docker run -it \
    -e POSTGRES_USER="root" \
    -e POSTGRES_PASSWORD="root" \
    -e POSTGRES_DB="ny_taxi" \
    -v D:\\20_Projects\\dezoomcamp\\code\\week_1\\2_docker_sql\\ny_taxi_postgres_data:/var/lib/postgresql/data \
    -p 5432:5432 \
    --network=pg-network \
    --name pg-database \
    postgres:13
```

## Run pgAdmin in the network
```bash
winpty docker run -it \
    -e PGADMIN_DEFAULT_EMAIL="admin@admin.com" \
    -e PGADMIN_DEFAULT_PASSWORD="root" \
    -p 8080:80 \
    --network=pg-network \
    --name pgadmin \
    dpage/pgadmin4
```

# Dockerizing the ingestion script

## Testing out the script
```bash
    URL="https://raw.githubusercontent.com/niaBaldoni/dezoomcamp/main/code/week_1/2_docker_sql/yellow_tripdata_2021-01.parquet"

    python pipeline_ny_taxi.py \
        --user=root \
        --password=root \
        --host=localhost \
        --port=5432 \
        --db=ny_taxi \
        --table-name=yellow_taxi_trips \
        --url=${URL}
```

## Dockerizing the script
```bash
    docker build -t taxi_ingest:v001 .
```

## Docker container
```bash
    URL="https://raw.githubusercontent.com/niaBaldoni/dezoomcamp/main/code/week_1/2_docker_sql/yellow_tripdata_2021-01.parquet"

    winpty docker run -it \
        --network=pg-network \
        taxi_ingest:v001 \
            --user=root \
            --password=root \
            --host=pg-database \
            --port=5432 \
            --db=ny_taxi \
            --table-name=yellow_taxi_trips \
            --url=${URL}
```