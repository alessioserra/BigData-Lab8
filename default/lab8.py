import sys
from pyspark import SparkConf, SparkContext
from datetime import datetime

#Example of datetime
#timestamp = "2008-05-15 12:01:00"
#datetimeObject = datetime.strptime(timestamp, "%Y-%m-%d %H:%M:%S")
#dayOfTheWeek = datetimeObject.strftime("%a")
#hour = datetimeObject.hour
    
#Initialize Spark application
conf = SparkConf().setAppName("Lab_8")
sc = SparkContext(conf = conf)

inputPath  = sys.argv[1]
outputPath = sys.argv[2] 
criticality_threshold = sys.argv[3]
