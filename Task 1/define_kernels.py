"""
Defines all the kernels that are used to convolve the image
"""

__author__ = "Lewis Morris"
__date__ = "09-11-2022"
__version__ = "1.0.0"
__status__ = "Production"

# 3rd party modules
import numpy as np

# TODO: Create a function to make a kernel
# TODO: Change the names of the kernels to be more meaningful
# TODO: Store each category as a mega array

######################
# Define the kernels #
######################

# Sharpening kernels
kernel_1 = np.array([[-1, -1, -1],
                     [-1, 4, -1],
                     [-1, -1, -1]])

kernel_2 = np.array([[-0.1, -0.1, -0.1],
                     [-0.1, 0.9, -0.1],
                     [-0.1, -0.1, -0.1]])

kernel_3 = np.array([[-1, -1, -1],
                     [-1, 7, -1],
                     [-1, -1, -1]])

# Uniform kernels
kernel_4 = np.array([[1, 1, 1],
                     [1, 1, 1],
                     [1, 1, 1]])

kernel_5 = np.array([[0, 0, 0],
                     [0, 0, 0],
                     [0, 0, 0]])

# Edge Detection kernels
# X direction
kernel_6 = np.array([[-1, 0, 1],
                     [-1, 0, 1],
                     [-1, 0, 1]])
# Y direction
kernel_7 = np.array([[1, 1, 1],
                     [0, 0, 0],
                     [-1, -1, -1]])

# 5x5 kernel
kernel_5x5 = np.array([[-1, -1, -1, -1, -1],
                       [-1, -1, -1, -1, -1],
                       [-1, 5, 5, 5, -1],
                       [-1, -1, -1, -1, -1],
                       [-1, -1, -1, -1, -1]])

# 7x7 kernel
kernel_7x7 = np.array([[-0.25, -0.25, -0.25, -0.25, -0.25, -0.25, -0.25],
                       [0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5],
                       [-1, -1, -1, 1, -1, -1, -1],
                       [-1, -1, 5, 5, 5, -1, -1],
                       [-1, -1, -1, -1, -1, -1, -1],
                       [0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5],
                       [-0.25, -0.25, -0.25, -0.25, -0.25, -0.25, -0.25]])

kernel_7x7_2 = np.array([[-0.25, -0.25, -0.25, -0.25, -0.25, -0.25, -0.25],
                         [-0.5, -0.5, -0.5, -0.5, -0.5, -0.5, -0.5],
                         [-1, -1, 2, 2, 2, -1, -1],
                         [-1, -1, 2, 2, 2, -1, -1],
                         [-1, -1, 2, 2, 2, -1, -1],
                         [-0.5, -0.5, -0.5, -0.5, -0.5, -0.5, -0.5],
                         [-0.25, -0.25, -0.25, -0.25, -0.25, -0.25, -0.25]])

kernel_gaussian = np.array([[0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0.01, 0.01, 0.01, 0, 0],
                            [0, 0.01, 0.05, 0.11, 0.05, 0.01, 0],
                            [0, 0.01, 0.11, 0.25, 0.11, 0.01, 0],
                            [0, 0.01, 0.05, 0.11, 0.05, 0.01, 0],
                            [0, 0, 0.01, 0.01, 0.01, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0]])
