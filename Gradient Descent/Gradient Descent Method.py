#!/usr/bin/env python
# coding: utf-8

# In[2]:


__Author__ = "Edoardo Oranger"

import numpy as numpy
import random as random
import matplotlib.pyplot as matplot

# Step 1: generate the random dataset.
# The function generates a random dataset given the length of the dataset in input

random.seed(1)

def generateDataset(datasetLength = 1):
    dataset = []
    slope = 1.01
    intercept = 0.015
    for index in range(0, datasetLength):
        error = random.uniform(1, 1e-2)
        xValue = round(random.uniform(1, 15), 3)
        dataset.append((xValue, round(slope*xValue + intercept + error, 3)))
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


# In[3]:


# Step 2: take the derivates of the loss function.
# The loss function in our case is the sum of the residuals square.

# Partial derivate of the loss function, respect the slope value
def partialSlope(m = 0, q = 0, dataset = []):
    total = 0
    for index in range(0, len(dataset)):
        total += dataset[index][0]*(m*dataset[index][0] + q - dataset[index][1] )
    return (2/len(dataset))*total

# Partial derivate of the loss function, respect the intercept value
def partialIntercept(m = 0, q = 0, dataset = []):
    total = 0
    for index in range(0, len(dataset)):
        total += (m*dataset[index][0] + q - dataset[index][1])
    return (2/len(dataset))*total

# In[4]:

# Step 3: pick two random values of the slope and the intercept.
# We will start by the values m = 1 and q = 0
# Setting the learning rate to 0.01

m = 1
q = 0
learningRate = 0.001
toll = 1e-4 # Setting the tollerance of the gradient's length
dataset = generateDataset(100) # Generate a dataset of 50 elements

# Step 4: this is the iterative step, and it's split in three substep.

iteration = 0 # The variable represents the number of iteration
norm = 0 # Variable representing the actual value of the norm

while (iteration < len(dataset)) or (norm <= toll):
    
    # Step 4.0: compute the step-size values of slope and intercept
    stepSlope = partialSlope(m, q, dataset)*learningRate
    stepIntercept = partialIntercept(m, q, dataset)*learningRate
    
    # Step 4.1: Compute the new paratemeters of slope and intercept
    m = m - stepSlope
    q = q - stepIntercept
    
    norm = numpy.linalg.norm(numpy.array([stepSlope, stepIntercept]))
    
    iteration = iteration + 1 # Increase the number of iteration
    
print("Norm = " + str(norm) + " toll = " + str(toll))
print("Computed values: m = " + str(m) + " q = " + str(q))
print("Iterations: " + str(iteration))
matplot.scatter(getXValues(dataset), getYValues(dataset))
matplot.plot([0, max(dataset)[0] + 1], [q, m*(max(dataset)[0] + 1) + q], color = "red")
matplot.show()
