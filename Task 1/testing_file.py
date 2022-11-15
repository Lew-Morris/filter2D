from myFilter import *

kernel = np.array([[-1, -1, -1],
                   [-1, 7, -1],
                   [-1, -1, -1]])

image = cv2.imread('./victoria.jpg')
