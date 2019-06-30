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

# Organiza o plote das imagens
plt.figure()
plt.subplot(221)
plt.hist(histograma, bins=256, range=(0,255))
plt.title('Histograma')
plt.savefig(saida)
plt.subplot(222)
plt.imshow(img_1, cmap='gray', interpolation='nearest')
plt.title('Imagem Entrada')

# Plota as imagens de entrada e saída na tela
plt.tight_layout()
plt.show()