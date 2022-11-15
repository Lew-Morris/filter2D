""" Checks if the two output arrays are the same

"""

__author__ = "Lewis Morris"
__date__ = "09-11-2022"
__studentID__ = "201492909"
__version__ = "1.0.0"
__status__ = "Production"

# Third-party modules
import timeit

import myFilter


def assert_eq(array1, array2):
    """

    :param array1:
    :param array2:
    :return:
    """
    counter = 0
    total = 0

    for i in range(len(array1) - 1):
        for j in range(len(array2) - 1):
            if array1[i][j] == array2[i][j]:
                counter += 1
                # Debugging
            # else:
                # print(f"My filter value for element {i},{j}: {array1[i][j]*255}\n"
                #       f"Should be --> {array2[i][j]}")
                # print(f"{array1[i][j]} should be {array2[i][j]}")
            total += 1

    percentage = 100 * (counter / total)
    print(f'Accuracy of my filter: {percentage:.2f}%\n')


def benchmark():
    import cv2
    import define_kernels
    src = cv2.cvtColor(cv2.imread('./victoria.jpg'), cv2.COLOR_BGR2GRAY)

    print("My Filter")
    start_time = timeit.default_timer()
    print("The start time is :", start_time)
    myFilter.my_filter_2d(src, define_kernels.kernel_1)
    print("The function took:", timeit.default_timer() - start_time)

    print("OpenCV Filter")
    start_time = timeit.default_timer()
    print("The start time is :", start_time)
    cv2.filter2D(src, -1, define_kernels.kernel_1)
    print("The function took:", timeit.default_timer() - start_time)

    # 3226.0672 TIMES SLOWER!!!!


def bench():
    import_module = "import testing_file"
    testcode_mf = '''
def test():
    return np.round(myFilter2D(image, kernel).astype('uint8'))

    '''

    testcode_ocv = '''
def test2():
    return cv2.filter2D(image, -1, kernel)

    '''
    my_filter_results = []
    open_cv_results = []
    my_filter_results.append(timeit.repeat(stmt=testcode_mf, setup=import_module, repeat=10))
    open_cv_results.append(timeit.repeat(stmt=testcode_ocv, setup=import_module, repeat=10))

    print(f"My filter runtimes: {my_filter_results}")
    print(f"OpenCV runtimes: {open_cv_results}")