
# This code is tested on Jupyter Qt Console
# This is tested line-by-line in interactive mode. If tested as a whole script, some cmdlines such as %matplotlib inline may not work 
import matplotlib.pyplot as plt
import os
import numpy as np

%matplotlib inline

# Put all the files in an array of images from img[0] to img[9]
files = [os.path.join('img_align_celeba', file_i) for file_i in os.listdir('img_align_celeba') if file_i.endswith('.jpg')]
img = [plt.imread(files[i]) for i in range(0,len(files))]
plt.imshow(img[0])

# Show heatmap of images
[plt.imshow(img[i][:,:,0]) for i in range(0,len(files))]

