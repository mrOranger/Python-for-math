# Stocastic Gradient Descent

Differently to "classic" __Gradient Descent__ algorithm, the __Stocastic Gradient Descent__ based its working on the choice of a random value of the Dataset, and computing the __slope__ and the __intercept__ of the line that approximate the values, based on the randomly chosen values.

The iteration step continues while the iteration number is less great that the input values, or the norm of the vector containing the slope and the intercept is less the tollerance in input. The tollerance is set to the value 0.00001

In each step, the __learning rate__ has been chosen equals to 0.01, and the Dataset has been randomly generate by selecting the values of the line y = 2.01x - 1.015. 

## Difference between the classic Gradient Descent

As you know, the Gradient Descent algorithm computes the slope and the intercept using all the values of the Dataset. With huge dataset problems arise, for this reason the Stocastic Gradient Descent works well for big Dataset.