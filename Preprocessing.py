
# This code is tested on Jupyter Qt Console
Import matplotlib.pyplot as plt
import os
Import numpy as np

%matplotlib inline

files = [os.path.join('img_align_celeba', file_i) for file_i in os.listdir('img_align_celeba') if file_i.endswith('.jpg')]

 # put all the files in an array of images from img[0] to img[9]

img = [plt.imread(files[i]) for i in range(0,len(files))]

plt.imshow(img[0])

