import numpy as np
import matplotlib.image as mpimg 
import matplotlib.pyplot as plt 
from math import factorial

class GaussianFilter:
    def __init__(self, path):
        self.image = mpimg.imread(path)
        self.copy = self.image
    
    def cvt2gray(self):
        m = np.dot(self.image,[1, 1, 1])//3
        self.image = np.array(m, dtype= "float64")
        self.image /= 255

    def gaussian_filter(self):
        self.cvt2gray()

        pad_width = (self.kernel.shape[0] - 1)//2
        new_img = np.zeros(self.image.shape)
        self.image = np.pad(self.image, [(pad_width,), (pad_width,)], mode= 'constant', constant_values= (0, 0))

        trav = self.kernel.shape[0]

        h_i = self.image.shape[0]
        w_i = self.image.shape[1]
        for i in range(pad_width, h_i - pad_width):
            for j in range(pad_width, w_i - pad_width):
                x = self.image[i - pad_width: i + pad_width + 1, j - pad_width: j + pad_width + 1]
                x = x.flatten() * self.kernel.flatten()
                sum_ = x.sum()
                new_img[i - pad_width][j - pad_width] = sum_/(trav ** 2)
        self.image = new_img

    def show_image(self, orig = 0):
        if orig == 1:
            plt.imshow(self.copy)
            plt.waitforbuttonpress()
        if orig == 0:
            plt.imshow(self.image, cmap= 'gray')
            plt.waitforbuttonpress()
    
    def gaussian_kernel(self, size):
        self.kernel = []
        pascal = np.zeros((size, 1))
        for i in range(size):
            pascal[i] = factorial(size - 1)/(factorial(i) * factorial(size - i - 1))
        for i in pascal:
            self.kernel.append(pascal * i)
        self.kernel = np.array(self.kernel).reshape((size, size))/(pascal.sum() ** 2)

if __name__ == "__main__":
    img = GaussianFilter("/home/thedarkcoder/Desktop/Computer science/Programs/Python programs/files_for_progs/image.jpg")

    img.show_image(1)
    img.gaussian_kernel(15)
    img.gaussian_filter()
    img.show_image(0)
    