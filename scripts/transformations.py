import pandas as pd

def transform_data(customers_df, products_df, orders_df):
    
    enriched_df = orders_df.join(customers_df, "customer_id", "inner") \
                           .join(products_df, "product_id", "inner")

    enriched_pd = enriched_df.toPandas()

    enriched_pd.to_csv("output/transformed/enriched_data.csv", index=False)

    return enriched_df