from pyspark import SparkConf, SparkContext
from pyspark.sql import SparkSession

# Initialize Spark Session
spark = SparkSession.builder \
    .appName("Test Spark Cluster") \
    .master("http://0.0.0.0:8080/") \
    .getOrCreate()

# Example data
data = ["Hello World", "Hello Spark", "Hello Docker"]

# Create RDD
rdd = spark.sparkContext.parallelize(data)

# Word count operation
word_counts = rdd.flatMap(lambda line: line.split(" ")) \
                 .map(lambda word: (word, 1)) \
                 .reduceByKey(lambda a, b: a + b)

# Collect the results
results = word_counts.collect()

# Print the results
for word, count in results:
    print(f"{word}: {count}")

# Stop the Spark session
spark.stop()


# from pyspark.sql import SparkSession


# def main():
#     # Initialize SparkSession
#     spark = SparkSession.builder \
#         .appName("HelloWorld") \
#         .master("spark://127.0.0.1:7077") \
#         .getOrCreate()

#     # Create an RDD containing numbers from 1 to 1000
#     numbers_rdd = spark.sparkContext.parallelize(range(1, 1000))

#     # Count the elements in the RDD
#     count = numbers_rdd.count()

#     print(f"Count of numbers from 1 to 1000 is: {count}")

#     # Stop the SparkSession
#     spark.stop()

# Import the necessary modules
# from pyspark.sql import SparkSession
# from pyspark.sql.functions import *

# # Create a SparkSession
# spark = SparkSession.builder \
#    .appName("My App") \
#    .master("spark://127.0.0.1:8080") \
#    .getOrCreate()

# rdd = spark.sparkContext.parallelize(range(1, 100))

# print("THE SUM IS HERE: ", rdd.sum())
# # Stop the SparkSession
# spark.stop()

# if __name__ == "__main__":
#     main()