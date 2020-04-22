# KMeans algorithm

The __KMeans algorithm__ is a clustering algorithm that allows to identify, given an input Dataset, hidden Clusters of the Dataset. 

The algorithm works using an iterative process based on __Centroids__ and tune operations. For the first step, three random element of the Dataset are choosed to be the Centroids of the Dataset, in the example, 3 Centroids have benn choosen for 3 Clusters, then the nearest values to the Centroids are assigned to a Cluster identified by the Centroid. The next step computes the Centroids of the selected Clusters and proceede changing the values of the Clusters. The process stops when no changes are performed on the Clusters.