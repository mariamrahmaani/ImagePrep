
# This code is tested on Jupyter Qt Console
# This is tested line-by-line in interactive mode. If tested as a whole script, some cmdlines such as %matplotlib inline may not work 
import matplotlib.pyplot as plt
import os
import numpy as np
from scipy.misc import imresize


### Start Function definition
# The function "image_crop_square" takes an image as an input and returns a cropped square image
def image_crop_square(image_1):
      if image_1.shape[0] > image_1.shape[1]:
            extra = (image_1.shape[0] - image_1.shape[1])
            if (extra % 2 == 0):
                  crop = image_1[extra // 2:-extra // 2,:]
            else:
                  crop = image_1[max(0, extra // 2 +1):min(-1, -(extra // 2)), :]
      elif image_1.shape[1] > image_1.shape[0]:
            extra = (image_1.shape[1] - image_1.shape[0])
            if (extra % 2 == 0):
                  crop = image_1[:, extra // 2:-extra //2]
            else:
                  crop = image_1[:, max(0, extra // 2 +1):min(-1, -(extra // 2))]
      else:
            crop = image_1
return crop

### End Function definition


%matplotlib inline

# Put all the files in an array of images from img[0] to img[9]
files = [os.path.join('img_align_celeba', file_i) for file_i in os.listdir('img_align_celeba') if file_i.endswith('.jpg')]
img = [plt.imread(files[i]) for i in range(0,len(files))]
plt.imshow(img[0])

# Show heatmap of images
[plt.imshow(img[i][:,:,0]) for i in range(0,len(files))]

