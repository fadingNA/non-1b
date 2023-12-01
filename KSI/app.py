import numpy as np
import pandas as pd
from matplotlib import pyplot as plt


def array_data(data):
    data = np.array(data)
    m, n = data.shape
    np.random.shuffle(data)

    data_train = data[0:1000].T
    Y_train = data_train[0]
    X_train = data_train[1:n]
    X_train = X_train / 255.

    data_test = data[1000:m].T
    Y_trained = data_train[0]
    X_trained = data_train[1:n]
    X_trained = X_train / 255.
    _x, m_train = X_trained.shape

    return X_trained, Y_trained, m_train


def init_params():
    W1 = np.random.rand(10, 784) - 0.5
    b1 = np.random.rand(10, 1) - 0.5
    W2 = np.random.rand(10, 10) - 0.5
    b2 = np.random.rand(10, 1) - 0.5
    return W1, b1, W2, b2


def ReLU(Z):
    return np.maximum(Z, 0)


def softmax(Z):
    A = np.exp(Z) / sum(np.exp(Z))
    return A


def forward_prop(W1, b1, W2, b2, X):
    Z1 = W1.dot(X) + b1
    A1 = ReLU(Z1)
    Z2 = W2.dot(A1) + b2
    A2 = softmax(Z2)
    return Z1, A1, Z2, A2


if __name__ == "__main__":
    data = pd.read_csv(
        '/Users/nonthachaiplodthong/Documents/Nons_work/non-1b/non-1b/data/train.csv')
    print(array_data(data))
