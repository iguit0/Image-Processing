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
plt.title('Resultado op. lógica AND')

# Plota as imagens de entrada e saída na tela
plt.tight_layout()
plt.show()