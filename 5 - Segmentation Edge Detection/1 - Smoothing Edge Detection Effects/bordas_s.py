# Como executar:
# $ python bordas_s.py <img_entrada> <img_saida> <mask_size>
# Utilizar o filtro da média.
# Utilizar o gradiente de Sobel

import sys
import numpy as np
import matplotlib.pyplot as plt
from scipy import misc
from scipy.ndimage import filters
from skimage import img_as_float

def loadImg(arg):
    return misc.imread(arg)

# Lê a imagem a partir de um arquivo
img_1 = loadImg(sys.argv[1])
saida = sys.argv[2]+'.tif'
mask_size = int(sys.argv[3]) # tamanho da mascara

# Converte os pixels em float, com valores entre 0 e 1
img_1 = img_as_float(img_1)

# Aplica o filtro da média
ave_masc = np.ones([mask_size, mask_size], dtype = float)
ave_masc = ave_masc / (mask_size * mask_size)
img_1 = filters.correlate(img_1, ave_masc)

# Operadores de Sobel Horizontal
sob_h = np.array([[ -1., -2., -1.],
                 [  0.,  0.,  0.],
                 [  1.,  2.,  1.]], dtype = float)

# Operadores de Sobel Vertical				 
sob_v = np.array([[ -1.,  0.,  1.],
                  [ -2.,  0.,  2.],
                  [ -1.,  0.,  1.]], dtype = float)

# Aplica Gradiente de Sobel
img_saida_h = filters.correlate(img_1, sob_h)
img_saida_v = filters.correlate(img_1, sob_v)

# Magnitude do gradiente
img_saida = np.sqrt(img_saida_h**2 + img_saida_v**2)

# Faz o salvamento das imagens de saída após o processamento
misc.imsave(saida, img_saida)

# Organiza o plot das imagens
plt.figure() 
plt.subplot(221); 
plt.imshow(img_1, cmap='gray', interpolation='nearest'); 
plt.title('Imagem Entrada')
plt.subplot(222); 
plt.imshow(img_saida, cmap='gray', interpolation='nearest')
plt.title('Resultado com máscara '+str(mask_size))

# Plota as imagens de entrada e saída na tela
plt.tight_layout()
plt.show()