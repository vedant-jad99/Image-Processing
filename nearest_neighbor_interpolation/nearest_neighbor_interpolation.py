import numpy as np 
import matplotlib.pyplot as plt
from matplotlib import image as im
import time

class nn_interpolation:
    def __init__(self, path):
        self.image = im.imread(path)
        self.copy = self.image
        print(self.image.shape)

    def interpolate(self, height, width):
        interpolated_image = np.zeros((height, width,3), dtype= "uint8")
        row_ratio = self.image.shape[0]/height
        column_ratio = self.image.shape[1]/width

        for i in range(height):
            for j in range(width):
                co_ord = [round(i*row_ratio), round(j*column_ratio)]
                if co_ord[0] == self.image.shape[0]:
                    co_ord[0] -= 1
                if co_ord[1] == self.image.shape[1]:
                    co_ord[1] -= 1
                interpolated_image[i][j][:] = self.image[co_ord[0]][co_ord[1]][:]
        
        self.image = interpolated_image

        loc_time = time.localtime(time.time())
        m = str(loc_time.tm_year) + str(loc_time.tm_mon) + str(loc_time.tm_mday) + str(loc_time.tm_hour) + str(loc_time.tm_min) + str(loc_time.tm_sec)
        img_save_name = 'nearest_neighbor_interpolation_' + m + ".jpg"
        plt.imsave(img_save_name, self.image)
        return interpolated_image

    def show_image(self, orig = 0):  
        if orig == 1:
            plt.imshow(self.copy)
            plt.waitforbuttonpress()
        if orig == 0:
            plt.imshow(self.image)
            plt.waitforbuttonpress()

if __name__ == "__main__":
    img = nn_interpolation("/home/thedarkcoder/Desktop/Computer science/Programs/Python programs/files_for_progs/sample.jpg")
    img.interpolate(700, 1400)
    img.show_image(1)
    img.show_image()