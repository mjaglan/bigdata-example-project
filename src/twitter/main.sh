sbt package

spark-submit  --deploy-mode cluster  --master yarn  --class KMEANS_DEMO  target/scala-2.10/twitter_2.10-1.0.jar

rm -rf twitter_out
hadoop dfs -copyToLocal  /tmp/twitter_out .

#zip -r twitter_out twitter_out/*

cat twitter_out/part*
