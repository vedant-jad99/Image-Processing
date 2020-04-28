import matplotlib.image as mpimg 
import matplotlib.pyplot as plt
import numpy as np 
import time

class Edge_Detector:
    def __init__(self, path):
        self.image = mpimg.imread(path)
        self.orig_image = self.image

    def cvt2gray(self):
        m = np.dot(self.image,[1, 1, 1])//3
        self.image = np.array(m, dtype= "float64")
        self.image /= 255
        print(self.image)

    def edge_detect(self):
        self.cvt2gray()

        for i in self.image:
            for j in range(len(i) - 1):
                if np.abs(i[j] - i[j + 1]) <= 0.03:
                    i[j] = 0
                else:
                    i[j] = 1
        loc_time = time.localtime(time.time())
        m = str(loc_time.tm_year) + str(loc_time.tm_mon) + str(loc_time.tm_mday) + str(loc_time.tm_hour) + str(loc_time.tm_min) + str(loc_time.tm_sec)
        img_save_name = 'edge_det_' + m + ".jpg"
        plt.imsave(img_save_name, self.image)


    def show_image(self, orig = 0):
        if orig == 1:
            plt.imshow(self.orig_image)
            plt.waitforbuttonpress()
        if orig == 0:
            plt.imshow(self.image, cmap= 'gray')
            plt.waitforbuttonpress()


if __name__ == "__main__":    
    img = Edge_Detector("/home/thedarkcoder/Desktop/Computer science/Programs/Python programs/files_for_progs/rubiks-cube.jpg")
    
    img.show_image(1)

    img.edge_detect()
    img.show_image()