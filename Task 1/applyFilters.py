""" Function calls to apply each filter category

Calls both OpenCVs and my own implementation for comparison. Calls image_functions to display the output
"""

__author__ = "Lewis Morris"
__date__ = "09-11-2022"
__version__ = "1.0.0"
__status__ = "Production"

# 1st party modules
from image_functions import *
from define_kernels import *
from myFilter import my_filter_2d
from benchmark_functions import assert_eq


def filter_image(input_image, kernel):
    """
    Calls both filter functions and appends results to an array for comparison
    :param input_image: The image that the filter will be applied to
    :param kernel: The filter used on input_image
    """
    my_filter = np.round(my_filter_2d(input_image, kernel)).astype('uint8')
    opencv_filter = cv2.filter2D(input_image, -1, kernel)

    # Append results and titles
    images.append(opencv_filter)
    titles.append('OpenCV Filter')
    images.append(my_filter)
    titles.append('My Filter')

    # Debugging
    # print("My filter pixel type:", type(my_filter[0][0]))
    # print(f"Shape of myFilter {my_filter.shape}")
    # print("OpenCV pixel type", type(opencv_filter[0][0]))
    # print(f"Shape of OpenCV {opencv_filter.shape}")
    # Equality check
    # assert_eq(my_filter, opencv_filter)


def apply_sharpen(image_to_test):
    """
    Calls 'filter_image' function with random kernels to compare outputs
    :param image_to_test: Input image
    """
    # Filter with Random Kernels
    filter_image(image_to_test, kernel_1)
    filter_image(image_to_test, kernel_2)
    filter_image(image_to_test, kernel_3)

    # Plot multiple images in the same window
    multiplot(titles, images, "Random Kernels", int(len(images) / 2))
    # Empty the arrays for the next test
    clear_arrays()


def apply_uniform(image_to_test):
    """
    Compares the outputs with the uniform kernels
    :param image_to_test:
    """
    # Filter with Uniform kernels
    filter_image(image_to_test, kernel_4)
    filter_image(image_to_test, kernel_5)
    multiplot(titles, images, "Uniform Kernels", int(len(images) / 2))
    clear_arrays()


def apply_edgeDetection(image_to_test):
    """
    Compares outputs with the edge detection kernels
    :param image_to_test: Input image
    """
    # Filter with Edge Detection Kernels
    print("Using X direction kernel:")
    filter_image(image_to_test, kernel_6)
    print("Using Y direction kernel:")
    filter_image(image_to_test, kernel_7)
    multiplot(titles, images, "Edge Detection Kernels", int(len(images) / 2))
    clear_arrays()


def apply_5x5Kernel(image_to_test):
    """
    Compares outputs with the larger 5x5 kernel
    :param image_to_test: Input image
    """
    # Trying a 5x5 sized kernel
    filter_image(image_to_test, kernel_5x5)
    multiplot(titles, images, "5x5 Sized Kernel", int(len(images) / 2))
    clear_arrays()


def apply_7x7Kernel(image_to_test):
    """
    Compares outputs with the larger 7x7 kernel
    :param image_to_test: Input image
    """
    # Trying a 7x7 sized kernel
    filter_image(image_to_test, kernel_7x7)
    multiplot(titles, images, "7x7 Kernel", int(len(images) / 2))
    clear_arrays()


def apply_gaussian(image_to_test):
    """
    Compares outputs with a gaussian blur filter
    :param image_to_test: Input image
    """
    # Trying a 7x7 sized kernel
    filter_image(image_to_test, kernel_gaussian)
    multiplot(titles, images, "Gaussian Kernel", int(len(images) / 2))
    clear_arrays()


def clear_arrays():
    """
    Clears the images and titles arrays
    """
    images.clear()
    titles.clear()


# Define arrays to store filter outputs
images = []
titles = []

