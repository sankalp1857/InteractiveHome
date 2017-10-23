import numpy as np


def sigmoid(x):
    output = 1/(1+np.exp(-x))
    return output


def sigmoid_output_to_derivative(output):
    return output*(1-output)
