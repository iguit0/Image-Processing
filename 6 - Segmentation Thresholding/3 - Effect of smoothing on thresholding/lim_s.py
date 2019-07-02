# Como executar:
# $ python lim_s.py <img_entrada> <img_saida> <mask_size>
# Utilizar o filtro da média.
# Utilizar o método de Otsu.
# <mask_size> é um número inteiro. Exemplo: Se mask_size=3 então a máscara possui tamanho 3x3.

import sys
import numpy as np
import matplotlib.pyplot as plt
from scipy import misc 
from skimage import img_as_float, filters
from scipy.ndimage import filters as fil

def loadImg(arg):
    return misc.imread(arg)

# Lê a imagem a partir de um arquivo
img_1 = loadImg(sys.argv[1])
saida = sys.argv[2]+'.tif'
mask_size = int(sys.argv[3])

# Converte os pixels em float, com valores entre 0 e 1
img_1 = img_as_float(img_1)

# Aplica o filtro da média
ave_masc = np.ones([mask_size, mask_size], dtype = float)
ave_masc = ave_masc / (mask_size * mask_size)
img_media = fil.correlate(img_1, ave_masc)

# Limiar de Otsu
l_otsu = filters.threshold_otsu(img_media)

# Segmenta a imagem por limiarização
img_saida = img_media < l_otsu

# Faz o salvamento das imagens de saída após o processamento
misc.imsave(saida, img_saida.astype(np.uint8))

# Organiza o plote das imagens
plt.figure() 
plt.subplot(221); 
plt.imshow(img_1, cmap='gray', interpolation='nearest'); 
plt.title('Imagem Entrada')
plt.subplot(222); 
plt.imshow(img_saida, cmap='gray', interpolation='nearest')
plt.title('Resultado suavização com máscara '+str(mask_size))

# Plota as imagens de entrada e saída na tela
plt.tight_layout()
plt.show()