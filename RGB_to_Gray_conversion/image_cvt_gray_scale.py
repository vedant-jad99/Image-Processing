import numpy as np 
import matplotlib.image as mpimg
import matplotlib.pyplot as plt

class Cvt2Gray:
    def __init__(self, path):
        self.img = mpimg.imread(path)
        self.copy = self.img
    
    def cvtimg(self):
        print(self.img)
        self.img = np.dot(self.img, [0.2989, 0.5870, 0.1140])
        print(self.img)
    
    def show_image(self, orig = 0):
        if orig == 1:
            plt.imshow(self.copy)
            plt.waitforbuttonpress()
        if orig == 0:
            plt.imshow(self.img, cmap= "gray")
            plt.waitforbuttonpress()

if __name__ == "__main__":
    image = Cvt2Gray("/home/thedarkcoder/Desktop/Computer science/Programs/Python programs/files_for_progs/image.jpg")

    image.cvtimg()
    image.show_image(1)
    image.show_image()
