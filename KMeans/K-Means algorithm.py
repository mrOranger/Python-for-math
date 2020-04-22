#!/usr/bin/env python
# coding: utf-8

# In[7]:


import numpy as numpy
import random as random
import matplotlib.pyplot as matplotlib

# Generate the Dataset in a random way based on a defined pattern
def generateDataset(datasetSize = 1):
    dataset = []
    # First cluster generation 
    xValue_1 = 100
    yValue_1 = 100
    for index in range(0, int(datasetSize/3)):
        x = random.uniform(0, xValue_1)
        y = random.uniform(0, yValue_1)
        dataset.append((x, y))
            
    # Second cluster generation
    xValue_2 = 200
    yValue_2 = 200
    for index in range(0, int(datasetSize/3)):
        x = random.uniform(xValue_1, xValue_2)
        y = random.uniform(yValue_1, yValue_2)
        dataset.append((x, y))
    
    # Third cluster generation
    xValue_3 = 300
    yValue_3 = -100
    for index in range(0, int(datasetSize/3)):
        x = random.uniform(xValue_2, xValue_3)
        y = random.uniform(0, yValue_3)
        dataset.append((x, y))
    return dataset

# Utility function to get the x values of a dataset in input
def getDatasetXValues(dataset):
    xValues = []
    for index in range(0, len(dataset)):
        xValues.append(dataset[index][0])
    return xValues

# Utility function to get the x values of a dataset in input
def getDatasetYValues(dataset):
    yValues = []
    for index in range(0, len(dataset)):
        yValues.append(dataset[index][1])
    return yValues

# Utility function to check if the Dataset has or not the input element
def hasElement(dataset, elem):
    for index in range(0, len(dataset)):
        if dataset[index] == elem:
            return True
    return False

# Generates the Dataset and shows the results in a 2-D graph
dataset = generateDataset(100)
matplotlib.scatter(getDatasetXValues(dataset), getDatasetYValues(dataset))
matplotlib.show()


# In[8]:


# Method that chekcs if the dataset are different or not
def checkInequality(firstDataset = [], secondDataset = []):
    if len(firstDataset) == len(secondDataset):
        for indexDataset in range(len(firstDataset)):
            if len(firstDataset[indexDataset]) == len(secondDataset[indexDataset]):
                for indexElem in range(0, len(firstDataset[indexDataset])):
                    if not (firstDataset[indexDataset][indexElem] == secondDataset[indexDataset][indexElem]):
                        return False
            else:
                return False
    else:
        return False
    return True

# Euclidian distance between two n-dimensional points
def euclidianDistance(point_1 = [], point_2 = []):
    distance = 0
    if len(point_1) == len(point_2):
        for index in range(0, len(point_1)):
            distance += numpy.power(point_1[index] - point_2[index], 2)
    return numpy.sqrt(distance)

# Chose two centroids of the dataset in a randon way
def choseCentroid(dataset = [], centroidsNumber = 1):
    chosenCentroids = []
    for currentCentroid in range(0, centroidsNumber):
        centroid = int(random.uniform(0, len(dataset)))
        if not hasElement(chosenCentroids, centroid):
            chosenCentroids.append((dataset[centroid][0], dataset[centroid][1]))
    return chosenCentroids

# Compute the cetroid of a dataset
def computeCentroid(dataset = []):
    xValues = 0
    yValues = 0
    for index in range(0, len(dataset)):
        xValues = xValues + dataset[index][0]
        yValues = yValues + dataset[index][1]
    return (xValues/len(dataset), yValues/len(dataset))

# Get the minimum value and the index of a dataset
def getMinElementIndex(elements = []):
    minElement = elements[0]
    minIndex = 0
    for index in range(1, len(elements)):
        if elements[index] < minElement:
            minElement = elements[index]
            minIndex = index
    return (minElement, minIndex)

# Method that compute a cluster based on the centroids and a dataset
def computeClusters(dataset = [], centroids = [], clustersNumber = 1):
    clusters = []
    for currCluster in range(0, clustersNumber):
        clusters.append([])
    for currElem in range(0, len(dataset)):
        distances = []
        for currCentroid in range(0, len(centroids)):
            distances.append(euclidianDistance(dataset[currElem], centroids[currCentroid]))
        clusters[getMinElementIndex(distances)[1]].append(dataset[currElem])
    return clusters
    
# KMeans alorithm implementation
def kMeans(dataset = [], clustersNumber = 1, centroids = []):
    currCentroids = centroids
    oldClusters = []
    newClusters = computeClusters(dataset, centroids, clustersNumber)
    while not checkInequality(oldClusters, newClusters):
        for index in range(0, len(centroids)):
            currCentroids[index] = computeCentroid(newClusters[index])
        oldClusters = newClusters
        newClusters = computeClusters(dataset, currCentroids, clustersNumber)
    return newClusters


# Executing of the algorithm and showing the result
centroids = choseCentroid(dataset, 3)
clusters = kMeans(dataset, len(centroids), centroids)

for clusterIndex in range(0, len(clusters)):
    matplotlib.scatter(getDatasetXValues(clusters[clusterIndex]), getDatasetYValues(clusters[clusterIndex]), color = "C" + str(clusterIndex))    

# Final centroids
matplotlib.scatter(getDatasetXValues(centroids), getDatasetYValues(centroids), color = "black")
matplotlib.show()


# In[ ]:





# In[ ]:




