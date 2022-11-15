""" A command-line interface

Allows the user to specify which images to use, and what filters to apply
"""


__author__ = "Lewis Morris"
__date__ = "08-11-2022"
__version__ = "1.0.0"
__status__ = "Production"

# 1st party modules
from applyFilters import *

# TODO: Add a while loop to menu
# TODO: Add option to restart that breaks from current loop to "restart"
# TODO: Add menu option to create own kernel
# TODO: Dynamically create the menu
# TODO: Allow for user to specify a directory to search for images


def menu():
    """
    CLI menu
    """
    image_to_compare = ""

    # Get user's choice of image
    while image_to_compare == "":
        print("Which image image would you like to use?")
        print(f'1. victoria.jpg\n'
              f'2. victoria2.jpg\n'
              f'3. cat.jpg\n'
              f'Q. Quit\n\n')

        image_choice = input("Enter a number (1-3/Q): ")
        match image_choice.lower():
            # Reads the selected image
            case "1":
                print("> Using victoria.jpg\n")
                image_to_compare = read_image('./victoria.jpg')
                break
            case "2":
                print("> Using victoria2.jpg!\n")
                image_to_compare = read_image('./victoria2.jpg')
                break
            case "3":
                print("> Using cat.jpg!\n")
                image_to_compare = read_image('./cat.jpg')
                break
            # Program exits
            case "q":
                print("> Quitting!")
                exit(0)
            case "quit":
                print("> Quitting!")
                exit(0)
            # Catch all case
            case _:
                print("Invalid Input, try again!\n")
                image_to_compare = ""

    user_kernel_choice = ""

    # Get user's choice of kernel (filter)
    while user_kernel_choice == "":
        print("Which kernels (filters) would you like to use?")
        print(f'1. Sharpening Kernels\n'
              f'2. Uniform Kernels\n'
              f'3. Edge Detection Kernels\n'
              f'4. 5x5 Kernel\n'
              f'5. 7x7 Kernel\n'
              f'6. Gaussian Kernel\n'
              f'Q. Quit\n\n')

        user_kernel_choice = input("Enter your choice (1-6/Q): ")
        match user_kernel_choice.lower():
            # Calls
            case "1":
                print("> Testing with sharpen kernels!\n"
                      "> Click the x to close the window\n")
                apply_sharpen(image_to_compare)
                user_kernel_choice = ""
            case "2":
                print("> Testing with uniform kernels!\n"
                      "> Click the x to close the window\n")
                apply_uniform(image_to_compare)
                user_kernel_choice = ""
            case "3":
                print("> Testing with edge detection kernels!\n"
                      "> Click the x to close the window\n")
                apply_edgeDetection(image_to_compare)
                user_kernel_choice = ""
            case "4":
                print("> Testing with 5x5 kernel!\n"
                      "> Click the x to close the window\n")
                apply_5x5Kernel(image_to_compare)
                user_kernel_choice = ""
            case "5":
                print("> Testing with 7x7 kernel!\n "
                      "> Click the x to close the window\n")
                apply_7x7Kernel(image_to_compare)
                user_kernel_choice = ""
            case "6":
                print("> Testing with gaussian kernel!\n "
                      "> Click the x to close the window\n")  # TODO: Try to make this a one liner for all lines
                apply_gaussian(image_to_compare)
                user_kernel_choice = ""
            # Program exits
            case "q":
                print("> Quitting!")
                exit(0)
            case "quit":
                print("> Quitting!")
                exit(0)
            # Catch all case
            case _:
                print("> Invalid input, Try again\n")
                user_kernel_choice = ""
