"""Minimal PySpark example for testing."""

from pyspark.sql import SparkSession
from pyspark.sql import DataFrame


def create_spark_session(app_name: str = "TestApp") -> SparkSession:
    """Create and return a Spark session."""
    return SparkSession.builder.appName(app_name).master("local[1]").getOrCreate()


def count_dataframe_rows(df: DataFrame) -> int:
    """Count the number of rows in a DataFrame.

    Args:
        df: PySpark DataFrame to count

    Returns:
        Number of rows in the DataFrame
    """
    return df.count()


def main():
    """Main function demonstrating PySpark DataFrame row counting."""
    spark = create_spark_session()

    # Create a simple DataFrame
    data = [("Alice", 25), ("Bob", 30), ("Charlie", 35)]
    df = spark.createDataFrame(data, ["name", "age"])

    # Count rows
    row_count = count_dataframe_rows(df)
    print(f"DataFrame has {row_count} rows")

    spark.stop()
    return row_count


if __name__ == "__main__":
    main()
