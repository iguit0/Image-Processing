# Como executar:
# $ python media.py img_1.tif saida <mask_size>
# <mask_size> é um número inteiro. Exemplo: Se mask_size=3 então a máscara possui tamanho 3x3.

import sys
import numpy as np
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

# Define a máscara
masc_25 = np.ones([mask_size, mask_size], dtype = float)
masc_25 = masc_25 / (mask_size * mask_size)

# Aplica a média
img_saida = filters.correlate(img_1, masc_25, mode = 'constant', cval = 0)

# Faz o salvamento da imagem de saída após o processamento
misc.imsave(saida, img_saida)

# Organiza o plote das imagens
plt.figure()
plt.subplot(221)
plt.imshow(img_1, cmap='gray', interpolation='nearest')
plt.title('Imagem Entrada')
plt.subplot(222)
plt.imshow(img_saida, cmap='gray', interpolation='nearest')
plt.title('Resultado com filtro média máscara '+str(mask_size))

# Plota as imagens de entrada e saída na tela
plt.tight_layout()
plt.show()