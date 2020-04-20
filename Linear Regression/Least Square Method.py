#!/usr/bin/env python
# coding: utf-8

# In[17]:


import matplotlib.pyplot as plt
import numpy as np
import random as rand
import timeit


# Step 1: generate the random dataset.
# The function generates a random dataset given the length of the dataset in input
rand.seed(1)
def generateDataset(datasetSize = 1):
    # Notice that the dataset is in form: [(xAxisValue, yAxisValue)]
    dataset = []
    xValue = rand.uniform(-100, 100)
    yValue = rand.uniform(0, 25)
    dataset.append((xValue, yValue))
    for currIndex in range(0, datasetSize):
        xValue = rand.uniform(-100, 100)
        yValue = rand.uniform(0, 25)
        dataset.append((xValue, yValue))
    return dataset

# Utility functions that returns the values of the y and x axis of the dataset
def getXValues(dataset = []):
    xValues = []
    for index in range(0, len(dataset)):
        xValues.append(dataset[index][0])
    return xValues

def getYValues(dataset = []):
    yValues = []
    for index in range(0, len(dataset)):
        yValues.append(dataset[index][1])
    return yValues

# Function that computes the line's value, passing the slope, the intecept and one random value
def computeLine(m = 0, q = 0, x = 0):
    return m*x + q


# In[1]:


# Function that compute the mean for the x axis values of the Dataset
def computeXMean(dataset = []):
    mean = 0
    for index in range(0, len(dataset)):
        mean = mean + dataset[index][0]
    return mean/len(dataset)

# Function that comput the mean for y axis values of the Dataset
def computeYMean(dataset = []):
    mean = 0
    for index in range(0, len(dataset)):
        mean = mean + dataset[index][1]
    return mean/len(dataset)


# In[6]:


# Function that computes the slope of the fitting function
def computeM(dataset = []):
    numerator = 0
    denominator = 0
    xMean = computeXMean(dataset)
    yMean = computeYMean(dataset)
    for index in range(0, len(dataset)):
        numerator = numerator + (dataset[index][0] - xMean)*(dataset[index][1] - yMean)
        denominator = denominator + np.power((dataset[index][0] - xMean), 2)
    return numerator/denominator

# Function that computes the intercept of the fitting function
def computeQ(dataset = []):
    return computeYMean(dataset) - computeM(dataset)*computeXMean(dataset)


# In[19]:


dataset = generateDataset(20)
m = computeM(dataset)
q = computeQ(dataset)

# Plotting the line
plt.scatter(getXValues(dataset), getYValues(dataset))
plt.plot([-150, 150], [computeLine(m, q, -150), computeLine(m, q, 150)])
plt.show()


# In[ ]:





# In[ ]:




