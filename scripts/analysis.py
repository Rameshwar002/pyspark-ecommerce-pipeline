from scripts.spark_session import get_spark_session
def analyze_data(enriched_df):
    try:
        print("\n📊 Top 10 Customers by Total Sales:")
        sales_per_customer = enriched_df.groupBy("customer_id").sum("amount")
        sales_per_customer.show(10)

        print("\n📊 Top 10 Products by Total Sales:")
        sales_per_product = enriched_df.groupBy("product_id").sum("amount")
        sales_per_product.show(10)

        print("✅ Analysis completed.")

    except Exception as e:
        print(f"❌ Error during analysis: {e}")
        raise
