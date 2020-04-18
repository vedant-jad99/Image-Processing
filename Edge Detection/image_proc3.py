import matplotlib.image as mpimg 
import matplotlib.pyplot as plt
import numpy as np 
import time

#path = (Specify path here)

def cvt2gray(img):
    m = np.dot(img,[1, 1, 1])//3
    arr = np.array(m, dtype= "float64")
    print(arr)
    return arr

img = mpimg.imread("/home/thedarkcoder/images7.jpg")

image = cvt2gray(img)
image /= 255
for i in image:
    for j in range(len(i) - 1):
        if np.abs(i[j] - i[j + 1]) <= 0.03:
            i[j] = 0
        else:
            i[j] = 255

print(image)

loc_time = time.localtime(time.time())
m = str(loc_time.tm_year) + str(loc_time.tm_mon) + str(loc_time.tm_mday) + str(loc_time.tm_hour) + str(loc_time.tm_min) + str(loc_time.tm_sec)
img_save_name = 'edge_det_' + m + ".jpg"

plt.imshow(img)
plt.waitforbuttonpress()
plt.imsave(img_save_name, image)
plt.imshow(image,cmap = 'gray')
plt.waitforbuttonpress()
