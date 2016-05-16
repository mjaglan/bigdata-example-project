import org.apache.spark.mllib.clustering.{KMeans, KMeansModel}
import org.apache.spark.mllib.linalg.Vectors

import org.apache.spark._
import org.apache.spark.SparkContext._
import org.apache.spark.rdd._
import org.apache.spark.input._
import scala.sys.process._
import scala.collection.JavaConverters._

import org.apache.commons.io.FilenameUtils
import org.apache.commons.io.FileUtils.{deleteDirectory, readFileToByteArray, writeByteArrayToFile}
import org.apache.commons.io.filefilter.PrefixFileFilter

import java.util.{UUID}
import java.io.{File, FileFilter, FileWriter, IOException}
import java.nio.file.Paths
import java.lang.System.{getenv}


object KMEANS_DEMO {

  def main(args: Array[String]) {
        val conf = new SparkConf().setAppName("KMEANS_DEMO")
        val sc = new SparkContext(conf)

        // Load and parse the data
        val data = sc.textFile("hdfs:///tmp/twitter/kmeans_data.txt")
        println("Loaded: " + data.count() + " records")

        val parsedData = data.map(s => Vectors.dense(s.split(' ').map(_.toDouble))).cache()
        println("Parsed: " + parsedData.count() + " records")

        // Cluster the data into two classes using KMeans
        val numClusters = 8
        val numIterations = 30
        val clusters = KMeans.train(parsedData, numClusters, numIterations)
        println("Found " + clusters.k + " centers")

        // Evaluate clustering by computing Within Set Sum of Squared Errors
        val WSSSE = clusters.computeCost(parsedData)
        println("Within Set Sum of Squared Errors = " + WSSSE)

		// save the results model
        // clusters.save(sc, "hdfs:///tmp/twitter_out")

        // save the SSE results
        var rdd = sc.parallelize(List("Ran KMeans on the dataset with final SUM SQUARED ERROR = "+WSSSE))
        rdd.saveAsTextFile("hdfs:///tmp/twitter_out")

  }

}
