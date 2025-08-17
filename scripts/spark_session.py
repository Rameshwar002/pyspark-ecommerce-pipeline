from pyspark.sql import SparkSession

def get_spark_session():
    """Create or get existing SparkSession"""
    return SparkSession.builder \
        .appName("Ecommerce Data Engineering Project") \
        .getOrCreate()