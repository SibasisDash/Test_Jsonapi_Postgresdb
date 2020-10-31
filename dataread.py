from pyspark.sql import functions as F
import os

from pyspark import SparkConf
from pyspark.sql import SparkSession

spark = SparkSession.builder.master("local").config(conf=SparkConf()).getOrCreate()

df = spark.read.json("file:///C://Users/user/PycharmProjects/flaskProject1/data2.json")

url = "jdbc:postgresql://http://127.0.0.1:64418/browser/#"
properties = {
    "driver": "org.postgresql.Driver",
    "user": "postgres",
    "password": "password"
}

mode = "overwrite"
df.write.format("jdbc") \
    .option("url", url) \
    .option("dbtable", hist_data) \
    .option(**properties) \
    .option("driver", driver) \
    .load(mode=mode)
