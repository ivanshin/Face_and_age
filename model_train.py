import os
import tarfile
import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt
from PIL import Image

PATH = 'dataset/'


tar = tarfile.open(os.path.join(PATH, 'faces.tar.gz'), 'r')

cnt = 0
for filename in tar.getnames():
    try:
        f = tar.extractfile(filename)
        f = Image.open(f)
        plt.imshow(f)
        #Data = f.read()
        #print(f'{filename}, : , {Data}')
        cnt += 1
        if cnt == 1:
            break
    except :
        print (f'ERROR: Did not find {filename} in tar archive')