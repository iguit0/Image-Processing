# Como executar:
# $ python eq.py img_1.tif saida

import sys
import matplotlib.pyplot as plt
from scipy import misc 
from skimage import exposure

def loadImg(arg):
    return misc.imread(arg)

# Lê a imagem a partir de um arquivo
img_1 = loadImg(sys.argv[1])
saida = sys.argv[2]+'.tif'

# Aplica a equalização do histograma e retorna a imagem
img_saida = exposure.equalize_hist(img_1)

# Faz o salvamento da imagem de saída após o processamento
misc.imsave(saida, img_saida)
