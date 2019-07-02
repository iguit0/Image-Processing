# Como executar:
# $ python maxmin.py <img_entrada> <img_saida_min> <imgsaida_max> <mask_size>
# <mask_size> é um número inteiro. Exemplo: Se mask_size=3 então a máscara possui tamanho 3x3.
# Gera duas imagens de saída.

import sys
import matplotlib.pyplot as plt
from scipy import misc 
from skimage import img_as_float
from scipy.ndimage import filters 

def loadImg(arg):
    return misc.imread(arg)

img_1 = loadImg(sys.argv[1])
saida_1 = sys.argv[2]+'.tif'
saida_2 = sys.argv[3]+'.tif'
mask_size = int(sys.argv[4])

# Converte os pixels em float, com valores entre 0 e 1
img_1 = img_as_float(img_1)

# Aplica o filtro de mínimo
img_saida_min = filters.minimum_filter(img_1, size = mask_size, mode = 'constant', cval = 0)

# Aplica o filtro de máximo
img_saida_max = filters.maximum_filter(img_1, size = mask_size, mode = 'constant')

# Faz o salvamento das imagens de saída após o processamento
misc.imsave(saida_1, img_saida_min)
misc.imsave(saida_2, img_saida_max)

# Organiza o plote das imagens
plt.figure() 
plt.subplot(221); 
plt.imshow(img_1, cmap='gray', interpolation='nearest'); 
plt.title('Imagem Entrada')
plt.subplot(222); 
plt.imshow(img_saida_min, cmap='gray', interpolation='nearest')
plt.title('Imagem Saída Min.')
plt.subplot(223); 
plt.imshow(img_saida_max, cmap='gray', interpolation='nearest')
plt.title('Imagem Saída Máx.')

# Plota as imagens de entrada e saída na tela
plt.tight_layout()
plt.show()
