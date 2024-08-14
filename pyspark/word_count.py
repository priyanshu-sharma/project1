import sys
from pyspark.sql import SparkSession
spark = SparkSession.builder.appName('word_count').getOrCreate()

sc = spark.sparkContext
# Read the input file and Calculating words count
text_file = sc.textFile(str(sys.argv[1]))
counts = text_file.flatMap(lambda line: line.split(" ")) \
                            .map(lambda word: (word, 1)) \
                           .reduceByKey(lambda x, y: x + y)
output = counts.collect()