"""
This app uses Python, numpy, pandas, matplotlib to generate a set of data points and plot them on a graph.
"""

# Importing the required libraries
import numpy as np                 # NumPy is the fundamental package for scientific computing with Python
import pandas as pd                # Pandas is a fast, powerful, flexible and easy to use open source data analysis and data manipulation library built on top of NumPy
import matplotlib.pyplot as plt    # Matplotlib is a comprehensive library for creating static, animated, and interactive visualizations in Python

"""
Create a function 'gen_data_points' that generates a set of 100 data points (x, f(x)) and returns them as a pandas data frame.
Arguments:
- 'x_range' is a tuple of two integers representing the rang0 e of x values to generate.
Returns:
- A pandas data frame with two columns, 'x' and 'y'.
Details:
- 'x' values are generated randomly between x_range[0] and x_range[1].
- 'y' values are generated as a non-linear function of x with excessive random noise: y = x ^ 1.5  + noise.
- The data frame is sorted by the 'x' values.
- The data frame has 100 rows.
Error Handling:
- Raise a ValueError if x_range is not a tuple of two integers.
- Raise a ValueError if x_range[0] is greater than x_range[1].
Examples:
- gendata((0, 100)) generates a data frame with 'x' values between 0 and 100.
- gendata((-100, 100)) generates a data frame with 'x' values between -100 and 100.
"""

def gen_data_points(x_range):
    if not isinstance(x_range, tuple):
        raise ValueError("x_range is not a tuple of two integers")
    if not all(isinstance(i, int) for i in x_range):
        raise ValueError("x_range is not a tuple of two integers")
    if x_range[0] > x_range[1]:
        raise ValueError("x_range[0] is greater than x_range[1]")
    np.random.seed(0)
    x = np.random.randint(x_range[0], x_range[1], 100)
    noise = np.random.normal(0, 1, 100)
    y = x ** 1.5 + noise
    data = pd.DataFrame({'x': x, 'y': y})
    data = data.sort_values(by='x')
    return data

"""
Create a function 'plot_data' that plots the data points on a graph.
Arguments:
- 'data' is a pandas data frame with two columns, 'x' and 'y'.
Returns:
- A plot showing the data points.
Details:
- The plot has a title 'Data Points'.
- The x-axis is labeled 'x'.
- The y-axis is labeled 'f(x)'.
- The plot has a grid.
- The plot is displayed.
Examples:
- plot_data(data) plots the data points in the data frame.
"""

def plot_data(data):
    plt.plot(data['x'], data['y'], 'o')
    plt.title('Data Points')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.grid()
    plt.show()

"""
Create a function 'main' that generates data points and plots them.
Arguments:
- None
Returns:
- None
"""

def main():
    data = gen_data_points((0, 100))
    plot_data(data)

# Call the main function
if __name__ == '__main__':
    main()
