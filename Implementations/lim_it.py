# Como executar:
# $ python lim_it.py <img_entrada> <img_saida> <T_ini>
# <T_ini> é um número tipo float. É o chute inicial do threshold.
# Considerar delta-T mínimo como 0.001

import sys
import numpy as np
import matplotlib.pyplot as plt
from scipy import misc 
from skimage import img_as_float 

def limiar_global_simples(img_entrada, T_ini):
    
    # Consderar delta-T mínimo como 0.001
    min_delta_T = img_entrada.max() * 0.001
		
    # Inicializa T com T_ini
    T = T_ini
	
    # Inicializa delta_T com Infinito
    delta_T = np.inf

    # Iteração
    while delta_T >= min_delta_T:
        # Segmenta a imagem usando T
        g = img_entrada > T
        
		# Calcula o numero de pixels de objeto e de fundo
        num_px_back, num_px_front = np.bincount(g.flatten())
        
		# Constroi imagem com os pixels de objeto
        g_front = img_entrada * g
        
		# Constroi imagem com os pixels de fundo
        g_back = img_entrada * np.invert(g)
        
		# Intensidade média - pixels de objeto
        fg_mean = g_front.sum() / float(num_px_front)
        
		# Intensidade média – pixels de fundo
        bg_mean = g_back.sum() / float(num_px_back)
        
		# Armazena valor atual de T
        T_old = T
        
		# Calcula um novo limiar T
        T = 0.5 * (fg_mean + bg_mean)
        
		# Calcula o novo valor de delta_T
        delta_T = np.abs(T - T_old)
    return T 

def loadImg(arg):
    return misc.imread(arg)

# Lê a imagem a partir de um arquivo
img_1 = loadImg(sys.argv[1])
saida = sys.argv[2]+'.tif'
T_ini = float(sys.argv[3])

# Converte os pixels em float, com valores entre 0 e 1
img_1 = img_as_float(img_1.astype(np.uint8))

# Chama a função para cálculo do limiar global iterativo
valor_T = limiar_global_simples(img_1, T_ini)

# Segmenta a imagem com o limiar T
img_saida = img_1 > valor_T
misc.imsave(saida, img_saida.astype(np.uint8))
