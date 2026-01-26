import pandas as pd
from sqlalchemy import create_engine, text

print("Starting data ingestion script...")

# Database connection
print("Connecting to database...")
try:
    engine = create_engine('postgresql://postgres:postgres@localhost:5433/ny_taxi')
    # Test the connection
    with engine.connect() as conn:
        result = conn.execute(text("SELECT 1"))
        print("SUCCESS: Database connection successful!")
except Exception as e:
    print(f"ERROR: Database connection failed: {e}")
    exit(1)

# Load green taxi data
print("\nLoading green taxi data...")
try:
    df_green = pd.read_parquet('data/green_tripdata_2025-11.parquet')
    print(f"SUCCESS: Loaded {len(df_green)} green taxi trips")
    print(f"Columns: {list(df_green.columns)}")
except Exception as e:
    print(f"ERROR: Failed to load green taxi data: {e}")
    exit(1)

# Load to PostgreSQL
print("\nLoading green taxi data to database...")
try:
    df_green.to_sql('green_taxi_trips', con=engine, if_exists='replace', index=False)
    print("SUCCESS: Green taxi data loaded to database!")
except Exception as e:
    print(f"ERROR: Failed to load to database: {e}")
    exit(1)

# Load zones data
print("\nLoading zones data...")
try:
    df_zones = pd.read_csv('data/taxi_zone_lookup.csv')
    print(f"SUCCESS: Loaded {len(df_zones)} zones")
except Exception as e:
    print(f"ERROR: Failed to load zones: {e}")
    exit(1)

# Load to PostgreSQL
print("\nLoading zones data to database...")
try:
    df_zones.to_sql('zones', con=engine, if_exists='replace', index=False)
    print("SUCCESS: Zones data loaded to database!")
except Exception as e:
    print(f"ERROR: Failed to load zones to database: {e}")
    exit(1)

print("\nAll data loaded successfully!")

