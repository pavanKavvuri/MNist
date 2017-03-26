import numpy as np
import matplotlib.pyplot as plt

#X_train = np.array([[1,2],[3,4],[5,6],[7,8],[9,10],[11,12],[13,14],[2,8],[1,6],[5,4],[9,2],[5,8]])
X_train = np.array([[1, 2],[3, 4]])
print (X_train.shape)

#Y_train = np.array([[3],[7],[11],[15],[19],[23],[27],[10],[7],[9],[11],[13]])
Y_train = np.array([[3], [7]])

def sigmoid (x): return 1/(1 + np.exp(-x))
def sigmoid_(x): return x * (1 - x)



eta = 0.11

out11 = []
W = []

#w1 = np.random.uniform(size=(2, 2))
w2 = np.random.uniform(size=(2, 1))
'''
out1 = sigmoid(np.dot(X_train, w1))
out2 = sigmoid(np.dot(out1, w2))

Err = Y_train - out2
dZ = Err * sigmoid_(out2)

print (out2)



'''
'''
for i in range(10):
    out1 = (np.dot(X_train, w2))
    #out2 = (np.dot(out1, w2))
    Err = Y_train - out1
    w2 = w2 + eta * (np.transpose(X_train))
    print (out1)





#plt.imshow(out11, W)
#plt.show()
'''

out1 = (np.dot(X_train, w2))
Err = Y_train - out1


