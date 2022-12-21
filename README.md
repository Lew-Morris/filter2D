![License](https://img.shields.io/github/license/Lew-Morris/filter2D)
![GitHub commit activity](https://img.shields.io/github/commit-activity/m/lew-morris/3d-cellular-automata)
![GitHub last commit (branch)](https://img.shields.io/github/last-commit/lew-morris/3d-cellular-automata/main)
![GitHub repo size](https://img.shields.io/github/repo-size/lew-morris/3d-cellular-automata)

---
# Overview

This was made for a University module on computer vision. **I received a grade of 78/100 (1st class) for this assignment**

The filter2D function is used to apply a filter, or kernel, to an input image. This is done by applying a matrix of values (the kernel) to each pixel in the image which results in a final "convolution". 

My reimplementation has an average accuracy of ~97% when compared to OpenCV's version, but this depends on the filter. For example, the uniform kernels are the best with ~99% accuracy, but the gaussian kernel is ~23% accurate. This is likely due to rounding errors as the output of both functions is identical to the human eye. 

# Requirements
This project makes use of:
* Numpy
  * Various uses, `array.shape` as an example
* Matplotlib
  * Output images
* OpenCV
  * Comparing results and various other uses

# Installation and Configuration
1. [Clone the repository](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository)
1. Open in any IDE, or ensure the requirements have been downloaded to the python venv
1. Run with `python3 ~/filter2D/Task 1/main.py` - there are no arguments to worry about!
1. Enjoy 😊

* As of writing this, there is no plan to implement a way to upload your own images without editing the code directly.

# Known Issues
There are currently no known issues
