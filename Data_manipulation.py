#splits images into 244x244 blocks from DiBas image dataset (they have now moved to links on github and their original website does not work anymore)

import numpy as np
import PIL as Image
from os import *

#split images into 244 x 244 blocks
def process_image(im):
    imarray = np.array(im)
    im_h, im_w = imarray.shape[:2]
    block_h, block_w = 224, 224
    
    for row in np.arange(im_h - block_h +1, step = block_h):
        for col in np.arange(im_w - block_w +1, step = block_w):
            im1 = imarray[row:row+block_h, col:col+block_w, :]
            im1 = Image.fromarray(im1)
            global i
            global path
            im1.save(path + "\img" + f"{i}" + ".png")
            i+=1
    print("completed")

#was using this to get the names of all folders for the "categories" on the webapp.
def getNames(directory):
    lend = len(os.listdir(directory))
    i = 0
    for filename in os.listdir(directory):
        f = os.path.join(directory, filename)
        i += 1
        if i != lend:
            print(str("'")+str(f[42:len(f)])+"',")
        else:
            print(str("'")+str(f[42:len(f)])+"'")
