import pandas as pd
import matplotlib.pyplot as plt
import os

def visualize_data():
    try:
        # Ensure output folder exists
        os.makedirs("output/plots", exist_ok=True)

        # Load enriched CSV
        df=pd.read_csv("d:\\GitAction\\pyspark-ecommerce-pipeline\\output\\transformed\enriched_data.csv")
        print(df.columns.tolist())
        df.columns = df.columns.str.strip()   # removes leading/trailing spaces


        # Group by product_id and sum amounts
        product_sales = df.groupby("product_id")["amount"].sum().sort_values(ascending=False)

        top_products = product_sales.sort_values(ascending=False).head(10)

        plt.figure(figsize=(10, 6))
        top_products.plot(kind="bar", color="skyblue", edgecolor="black")

        plt.title("Top 10 Products by Sales Amount")
        plt.xlabel("Product ID")
        plt.ylabel("Total Sales Amount")
        plt.xticks(rotation=45, ha="right")
        plt.tight_layout()
        plt.show()
        
        plt.savefig("output/top_10_products.png")
        plt.close()


        print("✅ Visualizations saved in output/plots/")

    except Exception as e:
        print(f"❌ Error during visualization: {e}")
        raise
