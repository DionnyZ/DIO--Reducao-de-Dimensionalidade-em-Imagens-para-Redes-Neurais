from PIL import Image
import numpy as np
import os

def acinzentar_imagem(caminho):
    imagem_cinza = Image.open(caminho).convert('L')
    return imagem_cinza

def binarizar_imagem(imagem, limiar=127):
    pixels = np.array(imagem)
    binarizada = np.where(pixels > limiar, 255, 0)
    return binarizada

def salvar_imagem(caminho, pixels):
    imagem_binarizada = Image.fromarray(np.uint8(pixels))
    imagem_binarizada.save(caminho)

caminho_imagens = os.path.join(os.getcwd(), 'images\\')
imagem_origem = caminho_imagens + 'Cachorro.jpg'

imagem_cinza = acinzentar_imagem(imagem_origem)
imagem_binarizada = binarizar_imagem(imagem_cinza)
salvar_imagem(caminho_imagens + 'imagem_binarizada.jpg', imagem_binarizada)
salvar_imagem(caminho_imagens + 'imagem_cinza.jpg', imagem_cinza)

print("Imagens salvas em", caminho_imagens)