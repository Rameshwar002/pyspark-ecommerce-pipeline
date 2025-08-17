from scripts.ingestion import ingest_data
from scripts.transformations import transform_data
from scripts.analysis import analyze_data

def main():
    customers_df, products_df, orders_df = ingest_data()
    enriched_df = transform_data(customers_df, products_df, orders_df)
    analyze_data(enriched_df)

if __name__ == "__main__":
    main()
