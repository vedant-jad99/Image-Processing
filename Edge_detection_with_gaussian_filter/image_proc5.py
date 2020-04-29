import matplotlib.image as mpimg 
import matplotlib.pyplot as plt
from math import factorial
import numpy as np 
import time


class Edge_Detector_gaussian_filter:
    def __init__(self, path):
        self.image = mpimg.imread(path)
        self.orig_image = self.image

    def cvt2gray(self):
        m = np.dot(self.image,[1, 1, 1])//3
        self.image = np.array(m, dtype= "float64")
        self.image /= 255
        # print(self.image)

    def gaussian_filter(self, kernel):
        self.cvt2gray()

        pad_width = (kernel.shape[0] - 1)//2
        new_img = np.zeros(self.image.shape)
        self.image = np.pad(self.image, [(pad_width,), (pad_width,)], mode= 'constant', constant_values= (0, 0))

        trav = kernel.shape[0]

        h_i = self.image.shape[0]
        w_i = self.image.shape[1]
        for i in range(pad_width, h_i - pad_width):
            for j in range(pad_width, w_i - pad_width):
                x = self.image[i - pad_width: i + pad_width + 1, j - pad_width: j + pad_width + 1]
                x = x.flatten() * kernel.flatten()
                sum_ = x.sum()
                new_img[i - pad_width][j - pad_width] = sum_/(trav ** 2) 
        # print(new_img)
        self.image = new_img
        plt.imshow(self.image, cmap= 'gray')
        plt.waitforbuttonpress()

    def edge_detect(self):
        for i in self.image:
            for j in range(len(i) - 1):
                if np.abs(i[j] - i[j + 1]) <= 0.00025:
                    i[j] = 0
                else:
                    i[j] = 1
        loc_time = time.localtime(time.time())
        m = str(loc_time.tm_year) + str(loc_time.tm_mon) + str(loc_time.tm_mday) + str(loc_time.tm_hour) + str(loc_time.tm_min) + str(loc_time.tm_sec)
        img_save_name = 'edge_det_gaussian_filter' + m + ".jpg"
        plt.imsave(img_save_name, self.image)


    def show_image(self, orig = 0):
        if orig == 1:
            plt.imshow(self.orig_image)
            plt.waitforbuttonpress()
        if orig == 0:
            plt.imshow(self.image, cmap= 'gray')
            plt.waitforbuttonpress()

def gaussian_kernel(size):
    kernel = []
    pascal = np.zeros((size, 1))
    for i in range(size):
        pascal[i] = factorial(size - 1)/(factorial(i) * factorial(size - i - 1))
    for i in pascal:
        kernel.append(pascal * i)
    kernel = np.array(kernel).reshape((size, size))/(pascal.sum() ** 2)
    return kernel
        


if __name__ == "__main__":    
    img = Edge_Detector_gaussian_filter("/home/thedarkcoder/Desktop/Computer science/Programs/Python programs/files_for_progs/sample.jpg")
    
    img.show_image(1)
    kernel = gaussian_kernel(7)
    img.gaussian_filter(kernel)
    img.edge_detect()
    img.show_image()