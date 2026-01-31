"""Unit tests for main.py PySpark functions."""

import pytest
from main import count_dataframe_rows, create_spark_session


@pytest.fixture(scope="module")
def spark():
    """Create a Spark session for testing."""
    spark_session = create_spark_session("TestSession")
    yield spark_session
    spark_session.stop()


def test_count_dataframe_rows(spark):
    """Test that count_dataframe_rows correctly counts rows in a DataFrame."""
    # Create test data
    test_data = [("Alice", 25), ("Bob", 30), ("Charlie", 35), ("David", 40)]
    df = spark.createDataFrame(test_data, ["name", "age"])

    # Test the count function
    result = count_dataframe_rows(df)

    assert result == 4, f"Expected 4 rows, but got {result}"


def test_count_empty_dataframe(spark):
    """Test that count_dataframe_rows handles empty DataFrames."""
    # Create empty DataFrame
    df = spark.createDataFrame([], "name STRING, age INT")

    # Test the count function
    result = count_dataframe_rows(df)

    assert result == 0, f"Expected 0 rows for empty DataFrame, but got {result}"
