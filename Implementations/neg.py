# Como executar:
# $ python neg.py img_1.tif saida

import sys
import numpy as np
import matplotlib.pyplot as plt
from scipy import misc

def loadImg(arg):
    return misc.imread(arg)

# Lê a imagem a partir de um arquivo
img_1 = loadImg(sys.argv[1])
saida = sys.argv[2]+'.tif'

# Faz a multiplicação por -1 para obtenção do inverso da imagem
img_saida = img_1 * (-1)

# Faz o salvamento da imagem de saída após o processamento
misc.imsave(saida, img_saida)