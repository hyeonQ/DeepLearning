import numpy as np
import matplotlib.pylab as plt


# for real number
def step_func_for_real_number(x):
    if x>0:
        return 1
    else:
        return 0


# for numpy array
def step_func(x):
    y = x > 0
    return y.astype(np.int)


def sigmoid(x):
    return 1 / (1+np.exp(-x))


def relu(x):
    return np.maximum(0, x)


if __name__ == "__main__":
    x = np.arange(-5.0, 5.0, 0.1)
    #y = step_func(x)
    #y = sigmoid(x)
    # y = relu(x)
    # plt.plot(x, y)
    # plt.ylim(-0.1, 1.1) # y축 범위
    # plt.show()

    X = np.array([1.0, 2.0])            # 1 x 2 or 2 x 1
    A = np.array([[1,3,5], [2,4,6]])    # 2 x 3
    B = np.array([[1,2], [3,4], [5,6]]) # 3 x 2
    print(np.dot(X, A))
    print(np.dot(B, X))
    # print(np.dot(W, X))  # error

