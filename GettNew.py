import numpy as np
import matplotlib.pyplot as plt
import random

import pandas as pd


X_train = np.array([[1],[2], [3], [4],[5],[6]])
Y_train = np.array([[2],[3],[4],[5],[6],[7]])
print Y_train




numIterations= 100
alpha = 0.0005
theta = np.ones(1)
#print theta.shape
cst = []
th = []
xTrans = X_train.transpose()

for v in range(100):
    hypothesis = np.dot(X_train, theta)
    loss = hypothesis - Y_train
    cost = np.sum(loss ** 2) / (2 * 6)
    cst.append(cost)
    th.append(theta)
    print("Iteration %d | Cost: %f" % (v, cost))
    gradient = np.dot(xTrans, loss) / 6
    print (gradient.shape)
    theta = theta - alpha * gradient





plt.plot(cst, th)
plt. show()



