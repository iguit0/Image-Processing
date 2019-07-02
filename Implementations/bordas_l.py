# Como executar:
# $ python bordas_l.py <img_entrada> <img_saida> <mask_size>
# Utilizar o filtro da média.
# Utilizar o gradiente de Sobel.
# Utilizar o limiar de 20% da maior intensidade da imagem.

import numpy as np
import matplotlib.pyplot as plt
import sys
from scipy import misc
from scipy.ndimage import filters
from scipy import ndimage as ndi
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

# Limiarização
percent = 0.2 # Porcentagem da intensidade maxima
img_saida = img_saida <= img_saida.max() * percent
	
# Faz o salvamento das imagens de saída após o processamento
misc.imsave(saida, img_saida.astype(np.uint8))
