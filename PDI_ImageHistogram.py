# Verão simples, sem interface onde usuário pode carregar qualquer imagem. Previsto para v2. 

import cv2
from matplotlib import pyplot as plt

def HistLinha(img, color):

    # Fixa o tamahno do figure
    plt.figure(figsize=(15, 5))

    if color is 1:
        #vetor de cores para linhas do histogram
        color = ('b', 'g', 'r')

        # Precisa converter img em RGB para usar no pylpot
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        plt.subplot(121), plt.imshow(img)

    else:
        color = ('b');
        plt.subplot(121), plt.imshow(img, 'gray')

    # For com a qtde de indices do vetor
    for i, cor in enumerate(color):
        hist = cv2.calcHist([img], [i], None, [256], [0, 256])
        plt.subplot(122), plt.plot(hist, color=cor)
        plt.xlim([0, 256])

    plt.show()


def HistLinhaBarra(img, color):

    # Fixa o tamahno do figure
    plt.figure(figsize=(15, 5))

    if color is 1:
        #vetor de cores para linhas do histogram
        color = ('b', 'g', 'r')

        # Precisa converter img em RGB para usar no pyplot
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        plt.subplot(221), plt.imshow(img)

    else:
        color = ('b');
        plt.subplot(221), plt.imshow(img, 'gray')


    # For com a qtde de indices do vetor
    for i, cor in enumerate(color):
        hist = cv2.calcHist([img], [i], None, [256], [0, 256])
        plt.subplot(222), plt.plot(hist, color=cor)
        plt.xlim([0, 256])

    plt.subplot(224), plt.hist(img.ravel(), 256, [0, 256])
    plt.show()


def HistBarra(img, cor):

    # Fixa o tamahno do figure
    plt.figure(figsize=(15, 5))

    # Cria um vetor com os dados da entrada da imagem
    imgArray = img.ravel()

    if cor is 1:
        
        # Precisa converter img em RGB para usar no pyplot
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        plt.subplot(121), plt.imshow(img)
    else:
        plt.subplot(121), plt.imshow(img, 'gray')

    plt.subplot(122), plt.hist(imgArray, 256, [0, 256])
    plt.show()


# imread: 0 gray; 1 color; -1 alpha
cor = 0
img = cv2.imread('igreja.tif', cor)
HistLinha(img, cor)
HistBarra(img, cor)
HistLinhaBarra(img, cor)

cor = 1
img = cv2.imread('losroques.jpg', cor)
HistLinha(img, cor)
HistBarra(img, cor)
HistLinhaBarra(img, cor)

img = cv2.imread('suco.jpg', cor)
HistLinha(img, cor)
HistBarra(img, cor)
HistLinhaBarra(img, cor)
