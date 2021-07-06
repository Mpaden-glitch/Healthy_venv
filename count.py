from pyspark import SparkContext
sc = SparkContext("local", "count app")
words = sc.parallelize (
    ["scala",
    "java",
    "hadoop",
    "spark",
    "akka",
    "aparks vs hadoop"]
)
counts = words.count()
print("Number of elements in RDD -> {}".format(counts))
