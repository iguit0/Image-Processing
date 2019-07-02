# Como executar:
# $ python nit.py <img_entrada> <img_saida>

import sys
import matplotlib.pyplot as plt
from scipy import misc
from scipy import ndimage

def loadImg(arg):
    return misc.imread(arg)

img_1 = loadImg(sys.argv[1])
saida = sys.argv[2]+'.tif'

# Aplica o gaussiano, borrando a imagem
img_blurred = ndimage.gaussian_filter(img_1, sigma = 7)
img_mask = img_1 - img_blurred
img_saida = img_blurred + (4.5 * img_mask)

# Faz o salvamento das imagens de saída após o processamento
misc.imsave(saida, img_saida)

# Organiza o plote das imagens
plt.figure() 
plt.subplot(221); 
plt.imshow(img_1, cmap='gray', interpolation='nearest'); 
plt.title('Imagem Entrada')
plt.subplot(222); 
plt.imshow(img_saida, cmap='gray', interpolation='nearest')
plt.title('Resultado Máscara Nitidez e high-boost')

# Plota as imagens de entrada e saída na tela
plt.tight_layout()
plt.show()