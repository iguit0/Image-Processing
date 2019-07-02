# Como executar:
# $ python med.py <img_entrada> <img_saida> <mask_size>
# <mask_size> é um número inteiro. Exemplo: Se mask_size=3 então a máscara possui tamanho 3x3.

import sys
import matplotlib.pyplot as plt
from scipy import misc 
from skimage import img_as_float
from scipy.ndimage import filters 

def loadImg(arg):
    return misc.imread(arg)

img_1 = loadImg(sys.argv[1])
saida = sys.argv[2]+'.tif'
mask_size = int(sys.argv[3])

# Converte os pixels em float, com valores entre 0 e 1
img_1 = img_as_float(img_1)

# Aplica a mediana
img_saida = filters.median_filter(img_1, size = mask_size, mode = 'constant', cval = 0) 

# Faz o salvamento da imagem de saída após o processamento
misc.imsave(saida, img_saida)
