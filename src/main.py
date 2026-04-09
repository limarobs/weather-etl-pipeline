from extract import extract
from transform import transform
from load import load

def run_pipeline():
    data = extract()
    df = transform(data)
    load(df)
    print("ETL pipeline executed successfully")

if __name__ == "__main__":
    run_pipeline()