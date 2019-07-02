# Como executar:
# $ python grad.py <img_entrada> <img_saida>
# Utilizar o gradiente de Sobel.

import sys
import numpy as np
import matplotlib.pyplot as plt
from scipy import misc
from scipy.ndimage import filters
from skimage import img_as_float

def loadImg(arg):
    return misc.imread(arg)

img_1 = loadImg(sys.argv[1])
saida = sys.argv[2]+'.tif'

# Converte os pixels em float, com valores entre 0 e 1
img_1 = img_as_float(img_1)

# Operadores de Sobel Horizontal
sob_h = np.array([[-1., -2., -1.],
                  [ 0.,  0.,  0.],
                  [ 1.,  2.,  1.]], dtype = float)

# Aplica Gradiente de Sobel
img_saida = filters.correlate(img_1, sob_h)

# Faz o salvamento das imagens de saída após o processamento
misc.imsave(saida, img_saida)
