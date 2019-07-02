# Como executar:
# $ python lap.py <img_entrada> <img_saida>
# Utilizar máscara laplaciana com centro -4.

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

# Aplica borramento sobre a imagem
img_blur = filters.gaussian_filter(img_1, sigma = 3)

# Laplaciano -4
lap_4 = np.array([[  0.,  1.,  0.],
                  [  1., -4.,  1.],
                  [  0.,  1.,  0.]], dtype = float)

# Calcula os imagens filtradas pelas máscaras laplacianas.
img_saida = filters.correlate(img_blur, lap_4)

# Faz o salvamento das imagens de saída após o processamento
misc.imsave(saida, img_saida)
