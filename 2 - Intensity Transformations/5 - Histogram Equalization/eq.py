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

# Organiza o plote das imagens
plt.figure()
plt.subplot(221)
plt.imshow(img_1, cmap='gray', interpolation='nearest')
plt.title('Imagem Entrada')
plt.subplot(222)
plt.imshow(img_saida, cmap='gray', interpolation='nearest')
plt.title('Imagem resultante da Equalização de Histograma')

# Plota as imagens de entrada e saída na tela
plt.tight_layout()
plt.show()