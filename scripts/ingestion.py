from scripts.spark_session import get_spark_session


def ingest_data():
    spark= get_spark_session()

    coustomer_df=spark.read.csv("data/raw/customers_large.csv",header=True,inferSchema=True)
    product_df=spark.read.csv("data/raw/products_large.csv",header=True,inferSchema=True)
    order_df=spark.read.csv("data/raw/orders_large.csv",header=True,inferSchema=True)

    print("loaded the data : coustomer, product, order ")

    return coustomer_df,product_df,order_df