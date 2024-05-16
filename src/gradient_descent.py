import numpy as np
import matplotlib.pyplot as plt


def linear_regression(x, w, b):
    return np.dot(x, w) + b


def quadratic_regression(x, w, b):
    return np.dot((x*2), w) + b


# function to calculate the cost
def compute_cost(x, y, w, b):

    m + x.shape[0]
    cost = 0

    for i in range(m):
        f_wb = linear_regression(x[i], w, b)
        cost = cost + (f_wb - y[i]) ** 2

    total_cost = 1 / (2 * m) * cost
    return total_cost


def compute_gradient(x, y, w, b):

    """
    Computes the gradient for linear regression
    Args:
        x (ndarray (m,)): Data, m examples
      y (ndarray (m,)): target values
      w,b (scalar)    : model parameters
    Returns
      dj_dw (scalar): The gradient of the cost w.r.t. the parameters w
      dj_db (scalar): The gradient of the cost w.r.t. the parameter b
     """

    m = x.shape[0]
    dj_dw = 0
    dj_db = 0

    for i in range(m):
        f_wb = w * x[i] + b
        dj_dw_i = (f_wb - y[i]) * x[i]
        dj_db_i = f_wb - y[i]
        dj_dw += dj_dw_i
        dj_db += dj_db_i

    dj_dw = dj_dw / m
    dj_db = dj_db / m

    return dj_dw, dj_db

def gradient_descent(x, y, w_in, b_in, alpha, num_iters):
    """
    Performs gradient descent to fit w,b. Updates w,b by taking
    num_iters gradient steps with learning rate alpha

    Args:
      x (ndarray (m,))  : Data, m examples
      y (ndarray (m,))  : target values
      w_in,b_in (scalar): initial values of model parameters
      alpha (float):     Learning rate
      num_iters (int):   number of iterations to run gradient descent

    Returns:
      w (scalar): Updated value of parameter after running gradient descent
      b (scalar): Updated value of parameter after running gradient descent
      """

    # An array to store cost J and w's at each iteration primarily for graphing later
    b = b_in
    w = w_in

    for i in range(num_iters):
        # Calculate the gradient and update the parameters using gradient_function
        dj_dw, dj_db = compute_gradient(x, y, w , b)

        # Update Parameters using equation (3) above
        b = b - alpha * dj_db
        w = w - alpha * dj_dw


    return w, b
