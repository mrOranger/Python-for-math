# Gradient Descent Method

The __Gradient Descet__ is a iterative method used to compute the best-fitting line of a Dataset in input. 

The method is based on the following steps:

> 1. Generate the random dataset. In the following code is a 2-D dataset.
> 2. Generate the derivates of the loss function.
> 3. Chose a random value of the __slope__ and the __intercept__ of the line's function and the __learning rate__.
> 4. Iterate while all the points of the dataset has been used to compute the values or the gradient's norm has reached 
     the input tollerance.

About the last point of the method, it's dividied into the following sub-steps:

> 4.1. Compute the step-size values of slope and intercept.
> 4.2. Compute the new paratemeters of slope and intercept.

