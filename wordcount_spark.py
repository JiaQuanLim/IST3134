from pyspark.sql import SparkSession
import nltk
import re
import time

spark = SparkSession.builder\
  .master("local[*]")\
  .appName("WordCount")\
  .getOrCreate()

sc=spark.sparkContext 

start_time = time.time()

enron_rdd = sc.textFile("hdfs:///cleaned_enron.csv")
enron_rdd = enron_rdd.map(lambda x: re.sub(r'\t', '', x))
enron_rdd = enron_rdd.map(lambda x: re.sub(r'[^\w\s]', '', x))

enron_rdd = enron_rdd.flatMap(lambda line: line.split(" "))
enron_rdd = enron_rdd.filter(lambda x:x!='')
enron_count = enron_rdd.map(lambda word: (word, 1))
enron_wc = enron_count.reduceByKey(lambda x , y : (x+y))

enron_wc.saveAsTextFile('hdfs:///wordcountspark')

#Display the execution time for pyspark
end_time = time.time()
execution_time = end_time - start_time
print("Execution time: {:.2f} seconds".format(execution_time))

sc.stop()
