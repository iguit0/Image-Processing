# Como executar:
# $ python logic.py img_1.tif img_2.tif saida

import sys
import numpy as np
import matplotlib.pyplot as plt
from scipy import misc

def loadImg(arg):
    return misc.imread(arg)

# Lê a imagem a partir de um arquivo
img_1 = loadImg(sys.argv[1])
img_2 = loadImg(sys.argv[2])
saida = sys.argv[3]+'.tif'

# Faz a operacao logica AND entre as imagens lidas
img_saida = np.logical_and(img_1,img_2)

# Faz o salvamento da imagem de saída após o processamento
misc.imsave(saida, img_saida.astype(np.uint8))
