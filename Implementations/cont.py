# Como executar:
# $ python cont.py img_1.tif saida

import sys
import numpy as np
import matplotlib.pyplot as plt
from scipy import misc
from skimage import exposure

def loadImg(arg):
    return misc.imread(arg)

# Lê a imagem a partir de um arquivo
img_1 = loadImg(sys.argv[1])
saida = sys.argv[2]+'.tif'

# Define os limites do intervalo
v_min, v_max = np.percentile(img_1, (20, 80))

# Aplica a função para esticar os níveis de intensidade
img_saida = exposure.rescale_intensity(img_1, in_range = (v_min, v_max))

# Faz o salvamento da imagem de saída após o processamento
misc.imsave(saida, img_saida)
