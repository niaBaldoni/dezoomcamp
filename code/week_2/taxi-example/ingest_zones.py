import pandas as pd
from sqlalchemy import create_engine

def ingest_zones():
    engine = create_engine('postgresql://root:root@localhost:5432/ny_taxi')
    
    url = 'https://d37ci6vzurychx.cloudfront.net/misc/taxi_zone_lookup.csv'
    
    print(f"Downloading zones data from {url}")
    df = pd.read_csv(url)
    
    print(f"Creating zones table with {len(df)} rows...")
    df.to_sql(name='zones', con=engine, if_exists='replace', index=False)
    
    print("✅ Zones data ingestion complete!")

if __name__ == '__main__':
    ingest_zones()
