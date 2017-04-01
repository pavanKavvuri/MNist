import  numpy as np
import  random
import matplotlib.pyplot as plt




def genData(numPoints, bias, variance):
    x = np.zeros(shape=(numPoints, 2))
    y = np.zeros(shape=numPoints)
    # basically a straight line
    for i in range(0, numPoints):
        # bias feature
        x[i][0] = 1
        x[i][1] = i
        # our target variable
        y[i] = (i + bias) + random.uniform(0, 1) * variance
    return x, y

# gen 100 points with a bias of 25 and 10 variance as a bit of noise
x, y = genData(3, 25, 10)

m, n = np.shape(x)
print (m,n)
numIterations= 100000
alpha = 0.0005
theta = np.ones(n)

print x[0:5,:]
print  y[0:5]

print  (theta.shape)
plt.plot(x[0:5,:], y[0:5], 'ro')
plt. show()
