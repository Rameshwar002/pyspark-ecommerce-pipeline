from scripts.spark_session import get_spark_session


def analyze_data(df):
    # Example: total sales per category
    sales_by_category = df.groupBy("category").sum("total_value")
    sales_by_category.show()

    # Save final transformed dataset
    df.write.mode("overwrite").csv("output/transformed/enriched_data", header=True)
