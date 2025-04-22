# Individual containers

## Build the server container
```
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
```
winpty pgcli -h localhost -p 5432 -u root -d ny_taxi
```
