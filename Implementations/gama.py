# Como executar:
# $ python gama.py img_1.tif saida <gama>
# <gama> é um número float, maior do que 0.

import sys
import numpy as np
import matplotlib.pyplot as plt
from scipy import misc
from skimage import exposure

def loadImg(arg):
    return misc.imread(arg)

# Lê a imagem a partir de um arquivo
img_1 = loadImg(sys.argv[1])
saida = sys.argv[2]+'.tif'
gama = float(sys.argv[3])

# Aplica a função para obtenção gama
img_saida = exposure.adjust_gamma(img_1, gama)

# Faz o salvamento da imagem de saída após o processamento
misc.imsave(saida, img_saida)
