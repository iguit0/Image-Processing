# Como executar:
# $ python gaus.py img_1.tif saida <stdev>
# <stdev> é o desvio padrão da Gaussiana.

import sys
import matplotlib.pyplot as plt
from scipy import misc 
from skimage import img_as_float
from scipy.ndimage import filters

def loadImg(arg):
    return misc.imread(arg)

img_1 = loadImg(sys.argv[1])
saida = sys.argv[2]+'.tif'
stdev = float(sys.argv[3])

# Converte os pixels em float, com valores entre 0 e 1
img_1 = img_as_float(img_1)

# Aplica filtro gaussiano
img_saida = filters.gaussian_filter(img_1, sigma = stdev, mode = 'constant', cval = 0) 

# Faz o salvamento da imagem de saída após o processamento
misc.imsave(saida, img_saida)

# Organiza o plote das imagens
plt.figure()
plt.subplot(221)
plt.imshow(img_1, cmap='gray', interpolation='nearest')
plt.title('Imagem Entrada')
plt.subplot(222)
plt.imshow(img_saida, cmap='gray', interpolation='nearest')
plt.title('Resultado gaussiano com desvio padrão '+str(stdev))

# Plota as imagens de entrada e saída na tela
plt.tight_layout()
plt.show()