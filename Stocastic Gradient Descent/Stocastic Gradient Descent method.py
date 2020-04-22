#!/usr/bin/env python
# coding: utf-8

# In[1]:


'''
    In normal Gradient Descent method, problems arise when a large amount of data is given in input.
    To avoid this problem, the Stocastic Gradient Descent method had been developed.
    Essentially, the method is based on some few steps:
    1. Generate the Dataset;
    2. Chose a starting random values of: slope, intercept and learning-rate;
    3. while (iteration-number < threshold) or (iteration-numer < dataset-length)
        3.0 Chose a random value of the dataset;
        3.1 Compute the step-size values;
        3.2 Update the slope and the intercept;
    4. Return the output values;
'''

import numpy as numpy
import random as random
import matplotlib.pyplot as matplot

random.seed(1)


# In[2]:


# Step 1: generate the Dataset
def generateDataset(datasetLength = 1):
    dataset = []
    slope = 2.01
    intercept = -1.015
    for index in range(0, datasetLength):
        error = random.uniform(1, 1e-2)
        xValue = round(random.uniform(1, 15), 3)
        dataset.append((xValue, round(slope*xValue + intercept + error, 3)))
    return dataset

# Utility function that returns the x asxis values of the dataset
def getXValues(dataset = []):
    values = []
    for index in range(0, len(dataset)):
        values.append(dataset[index][0])
    return values

# Utility function that returns the y axis values of the dataset
def getYValues(dataset = []):
    values = []
    for index in range(0, len(dataset)):
        values.append(dataset[index][1])
    return values


# In[3]:


# Step 2: generate random values of: slope, intercept and learning-rate
slope = 0
intercept = 1
learningRate = 0.001
toll = 1e-4 # Setting the tollerance of gradient's length
dataset = generateDataset(1000) # Generate the random dataset

# Partial derivate of the residual sum respect to the slope
def partialDerivateSlope(m = 1, q = 0, x = 0, y = 0):
    return 2*x*(m*x + q - y)

# Partial derivate of the residual sum respect to the intercept
def partialDerivateIntercept(m = 1, q = 0, x = 0, y = 0):
    return 2*(m*x + q - y)

# Loss function
def loss(dataset = [], m = 1, q = 0):
    total = 0
    for index in range(0, len(dataset)):
        x = dataset[index][0]
        y = dataset[index][1]
        total = total + numpy.power((m*x + q - y), 2)
    return total


# In[4]:


# Step 3: iterative step
iteration = 0
norm = 0
weights = []
lossFunctionVariations = []

while (iteration < 1000) or (norm <= toll):
    
    weights.append((slope, intercept))
    lossFunctionVariations.append(loss(dataset, slope, intercept))
    
    # Step 3.0: chose a random value of the dataset
    currentElement = int(random.uniform(0, len(dataset) - 1))
    currentX = dataset[currentElement][0]
    currentY = dataset[currentElement][1]
    
    # Step 3.1: compute the step size values
    stepSizeSlope = partialDerivateSlope(slope, intercept, currentX, currentY)*learningRate
    stepSizeIntercept = partialDerivateIntercept(slope, intercept, currentX, currentY)*learningRate
    
    # Step 3.2: compute the new slope and the new intercept
    slope = slope - stepSizeSlope
    intercept = intercept - stepSizeIntercept
        
    norm = numpy.linalg.norm(numpy.array([stepSizeSlope, stepSizeIntercept]))
    
    iteration = iteration + 1
    


# In[5]:


# Showing the results of the Stocastic Gradient Descent algoritm
print("Iterations = " + str(iteration))
print("Toll = " + str(toll) + " Norm = " + str(norm))
print("m = " + str(slope) + " q = " + str(intercept))


# In[6]:


# Showing the final line that approaches the results
matplot.scatter(getXValues(dataset), getYValues(dataset))
matplot.plot([0, max(dataset)[0] + 1], [intercept, slope*(max(dataset)[0] + 1) + intercept], color = "red")
matplot.show()


# In[7]:


# Showing the variation of the loss function bases on the iterations
iterations = [i for i in range(0, 1000)]
matplot.scatter(iterations, lossFunctionVariations)
matplot.show()


# 

# In[8]:


# Showing the variation of the slope's value bases on the iterations
matplot.scatter(iterations, [weights[index][0] for index in range(0, len(weights))])
matplot.show()


# In[9]:


# Showing the variation of the intercept's value bases on the iterations
matplot.scatter(iterations, [weights[index][1] for index in range(0, len(weights))])
matplot.show()


# In[ ]:




