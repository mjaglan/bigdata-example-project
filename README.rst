bigdata-example-project
===============================================================================

Using KMeans clustering with Euclidean distance measure to group together similar data points into 8 clusters. And then reporting the Sum Squared Error of the resulting clusters.

Objective is to run analysis algorithm on openstack cloud, by ansiblizing the major steps. For this we have to use ansible scripts to create the VMs, setup hadoop cluster, install required softwares, retrieve and upload the dataset into HDFS, and copy analysis code to Master-node of Hadoop Cluster. Login to master node, run the analysis code on the data in HDFS, retrieve the results, and show the output of algorithm ran.


``Results:``
The KMeans algorithm, when ran for 30 iterations on 13,700+ records for 8 clusters, the resulting sum squared error (SSE) was coming around 6300 ± 500. We ran our source multiple times from scratch.


``Implementation:``
The entry point to run this project is executing ``launch.sh`` present at `/src </src>`_. The `/src/twitter/ </src/twitter/>`_ contains the main source code::

  site.yml
  |--software.yml  // install necessary softwares on the VM
  |--dataset.yml   // retrieve the dataset and upload it to HDFS
  |--analysis.yml  // copy the analysis code-base

which will install necessary softwares on the VM, retrieve the dataset and upload it to HDFS, copy the following analysis code-base::

  main.sh
  |--twitter.sbt
  |--kmeans.demo.scala
  
to the master node.

To know how to run this project, refer the `installation.rst file <installation.rst>`_. A sample video demo of this project is present on `YouTube Channel <https://youtu.be/PxM0yurCBPQ>`_.



``References:``
   * Academic learnings from CSCI.I590.Topics In Informatics: `Projects On Big Data Software <https://www.soic.indiana.edu/graduate/courses/index.html?number=i590&department=INFO>`_ by Professor `Geoffrey Charles Fox <http://www.soic.indiana.edu/all-people/profile.html?profile_id=203>`_
   * The sample dataset of Emotion Vectors for tweets is obtained from `my previous work <https://github.com/mjaglan/TextSentiment.V1.a.public>`_
   * Using KMeans referred from `MLLib KMeans <http://spark.apache.org/docs/latest/mllib-clustering.html#k-means>`_
