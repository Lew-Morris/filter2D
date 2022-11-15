""" My implementation of the Filter2D function from OpenCV

[...]
"""
# TODO: Add a description

__author__ = "Lewis Morris"
__date__ = "09-11-2022"
__version__ = "1.0.0"
__status__ = "Production"

# 3rd Party imports
import numpy as np
import cv2


def my_filter_2d(input_image, kernel):
    """
    My own implementation of filter2D from the OpenCV library
    :param input_image: Input image
    :param kernel: Value of the filter to be used
    :return: Resulting convolution of the input image
    """
    # Get size of kernel
    m = kernel.shape[0]
    n = kernel.shape[1]

    # Pad image with 1px of 0's on each side
    input_image = cv2.copyMakeBorder(input_image, 1, 1, 1, 1, cv2.BORDER_CONSTANT, value=0)

    # Store size of image minus the padding
    dim_y = input_image.shape[0] - m + 1
    dim_x = input_image.shape[1] - n + 1

    # Create a new, zeroed array (image)
    new_image = np.zeros((dim_y, dim_x))

    # Loop through each pixel and apply the filter
    for i in range(dim_y):
        for j in range(dim_x):
            # Take the sum of each pixel and then multiply by the kernel (filter)
            conv = (np.sum(input_image[i:i + m, j:j + n] * kernel))

            # Threshold image to prevent clipping
            if conv < 0:
                new_image[i][j] = 0
            elif conv > 255:
                new_image[i][j] = 255
            else:
                new_image[i][j] = conv
    return new_image
