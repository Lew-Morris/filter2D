""" Helper functions

multiplot
Used to plot multiple images side by side for comparison

read_image
reads an image and returns a grayscale converted image
"""


__author__ = "Lewis Morris"
__date__ = "09-11-2022"
__version__ = "1.0.0"
__status__ = "Production"

# 3rd party imports
import cv2
import matplotlib.pyplot as plt


def multiplot(titlesArr, imagesArr, figureName, sizeY):
    """
    Plot the image in a two x sizeY grid
    :param titlesArr: Titles of the images
    :param imagesArr: Resulting images
    :param figureName: The window's title; the type of kernel used
    :param sizeY: Number of images to plot; the number of kernels compared
    """
    for i in range(len(titlesArr)):
        # Change the title of the window
        plt.figure(figureName)
        # Create a subplot for each element in the 'images' array
        plt.subplot(sizeY, 2, i + 1), plt.imshow(cv2.cvtColor(imagesArr[i], cv2.COLOR_BGR2RGB))
        plt.title(titlesArr[i])
        plt.xticks([]), plt.yticks([])
    plt.show()


def read_image(image_to_read):
    """
    Read an image -> image[] as grayscale
    :param image_to_read: image chosen by the user in the menu
    :return: Grayscale image
    """
    # Read image
    image_to_test = cv2.imread(image_to_read)

    # Convert to grayscale
    image_to_test = cv2.cvtColor(image_to_test, cv2.COLOR_BGR2GRAY)
    return image_to_test
