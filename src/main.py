from src.extract import extract
from src.transform import transform
from src.load import load
import logging

logging.basicConfig(level=logging.INFO)

def main():
    logging.info("Starting ETL pipeline")

    data = extract()
    df = transform(data)
    load(df)

    logging.info("ETL pipeline finished")

if __name__ == "__main__":
    main()