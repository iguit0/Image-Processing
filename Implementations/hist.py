# Como executar:
# $ python hist.py img_1.tif

import sys
import matplotlib.pyplot as plt
from scipy import misc 

def loadImg(arg):
    return misc.imread(arg)

# Lê a imagem a partir de um arquivo
img_1 = loadImg(sys.argv[1])
saida = 'histograma.tif'

# Transforma os níveis de intensidade numa imagem de uma dimensão
histograma = img_1.flatten()	
