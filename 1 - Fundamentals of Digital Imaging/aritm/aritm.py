# Operação escolhida: Subtração
# Como executar:
# $ python aritm.py img_1.tif img_2.tif saida

import sys
from scipy import misc
from skimage import data, util, color
import matplotlib.pyplot as plt

def loadImg(arg):
    return misc.imread(arg)

# Lê a imagem a partir de um arquivo
img_1 = loadImg(sys.argv[1])
img_2 = loadImg(sys.argv[2])
saida = sys.argv[3]+'.tif'

# Faz a subtração entre as imagens lidas
img_saida = img_1 - img_2

# Faz o salvamento da imagem de saída após o processamento
misc.imsave(saida, img_saida)

# Organiza o plote das imagens
plt.figure()
plt.subplot(221)
plt.imshow(img_1, cmap='gray', interpolation='nearest')
plt.title('Imagem 1')
plt.subplot(222)
plt.imshow(img_2, cmap='gray', interpolation='nearest')
plt.title('Imagem 2')
plt.subplot(223)
plt.imshow(img_saida, cmap='gray', interpolation='nearest')
plt.title('Resultado Subtração')

# Plota as imagens de entrada e saída na tela
plt.tight_layout()
plt.show()