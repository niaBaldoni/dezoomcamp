import pandas as pd
from sqlalchemy import create_engine
from tqdm.auto import tqdm
import click

dtype = {
    "VendorID": "Int64",
    "passenger_count": "Int64",
    "trip_distance": "float64",
    "RatecodeID": "Int64",
    "store_and_fwd_flag": "string",
    "PULocationID": "Int64",
    "DOLocationID": "Int64",
    "payment_type": "Int64",
    "fare_amount": "float64",
    "extra": "float64",
    "mta_tax": "float64",
    "tip_amount": "float64",
    "tolls_amount": "float64",
    "improvement_surcharge": "float64",
    "total_amount": "float64",
    "congestion_surcharge": "float64"
}

parse_dates = [
    "tpep_pickup_datetime",
    "tpep_dropoff_datetime"
]

@click.command()
@click.option('--pg-user', default='root', help='PostgreSQL user')
@click.option('--pg-pass', default='root', help='PostgreSQL password')
@click.option('--pg-host', default='localhost', help='PostgreSQL host')
@click.option('--pg-port', default=5432, type=int, help='PostgreSQL port')
@click.option('--pg-db', default='ny_taxi', help='PostgreSQL database name')
@click.option('--target-table', default='yellow_taxi_data', help='Target table name')
@click.option('--url', default='https://github.com/DataTalksClub/nyc-tlc-data/releases/download/yellow/yellow_tripdata_2021-01.csv.gz', help='URL of the CSV file')
def run(pg_user, pg_pass, pg_host, pg_port, pg_db, target_table, url):
    """Ingest NYC taxi data into PostgreSQL"""
    
    # Create database connection
    engine = create_engine(f'postgresql://{pg_user}:{pg_pass}@{pg_host}:{pg_port}/{pg_db}')
    
    print(f"Downloading data from {url}")
    
    # Read CSV in chunks
    df_iter = pd.read_csv(
        url,
        dtype=dtype,
        parse_dates=parse_dates,
        iterator=True,
        chunksize=100000
    )
    
    # Get first chunk to create table
    first_chunk = next(df_iter)
    
    # Create table with schema only (no data yet)
    print(f"Creating table {target_table}...")
    first_chunk.head(0).to_sql(
        name=target_table,
        con=engine,
        if_exists="replace",
        index=False
    )
    
    # Insert first chunk
    print(f"Inserting first chunk: {len(first_chunk)} rows")
    first_chunk.to_sql(
        name=target_table,
        con=engine,
        if_exists="append",
        index=False
    )
    
    # Insert remaining chunks with progress bar
    print("Inserting remaining chunks...")
    for df_chunk in tqdm(df_iter, desc="Progress"):
        df_chunk.to_sql(
            name=target_table,
            con=engine,
            if_exists="append",
            index=False
        )
    
    print(f"✅ Data ingestion complete! Table '{target_table}' created in database '{pg_db}'")

if __name__ == '__main__':
    run()
