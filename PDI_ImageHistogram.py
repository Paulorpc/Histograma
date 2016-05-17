# Versao simples, sem interface onde usuario pode carregar qualquer imagem. Previsto para v2.

import cv2
from matplotlib import pyplot as plt

def HistLinha(img, color):

    # Ajustes do Figure
    fig = plt.figure(3, figsize=(15, 8))
    tit = fig.suptitle("PDI: Histogramas", fontsize="x-large")
    tit.set_y(0.95)
    fig.subplots_adjust(top=0.85)

    ax1 = fig.add_subplot(121)
    ax2 = fig.add_subplot(122)

    ax1.set_title("Imagem Original")
    ax2.set_title("Histograma de Linhas ")

    ax1.axis('off')

    plt.ylabel("Frequencia")
    plt.xlabel("Pixels")

    if color is 1:
        #vetor de cores para linhas do histogram
        color = ('b', 'g', 'r')

        # Precisa converter img em RGB para usar no pylpot
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        ax1.imshow(img)

    else:
        color = ('b');
        ax1.imshow(img, 'gray')

    # For com a qtde de indices do vetor
    for i, cor in enumerate(color):
        hist = cv2.calcHist([img], [i], None, [256], [0, 256])
        ax2.plot(hist, color=cor)
        plt.xlim([0, 256])

    #plt.show()


def HistLinhaBarra(img, color):

    # Ajustes do Figure
    fig = plt.figure(1, figsize=(15, 8))
    tit = fig.suptitle("PDI: Histogramas", fontsize="x-large")
    tit.set_y(0.95)
    fig.subplots_adjust(top=0.85)

    ax1 = fig.add_subplot(221)
    ax2 = fig.add_subplot(222)
    ax3 = fig.add_subplot(224)

    ax1.set_title("Imagem Original")
    ax2.set_title("Histograma de Linhas ")
    ax3.set_title("Histograma de Barras ")

    ax1.axis('off')

    plt.ylabel("Frequencia")
    plt.xlabel("Pixels")

    if color is 1:
        #vetor de cores para linhas do histogram
        color = ('b', 'g', 'r')

        # Precisa converter img em RGB para usar no pyplot
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        ax1.imshow(img)

    else:
        color = ('b');
        ax1.imshow(img, 'gray')


    # For com a qtde de indices do vetor
    for i, cor in enumerate(color):
        hist = cv2.calcHist([img], [i], None, [256], [0, 256])
        ax2.plot(hist, color=cor)
        plt.xlim([0, 256])

    ax3.hist(img.ravel(), 256, [0, 256])
    #plt.show()


def HistBarra(img, cor):

    # Ajustes do Figure
    fig = plt.figure(2, figsize=(15, 8))
    tit = fig.suptitle("PDI: Histogramas", fontsize="x-large")
    tit.set_y(0.95)
    fig.subplots_adjust(top=0.85)

    ax1 = fig.add_subplot(121)
    ax3 = fig.add_subplot(122)

    ax1.set_title("Imagem Original")
    ax3.set_title("Histograma de Barras ")

    ax1.axis('off')

    plt.ylabel("Frequencia")
    plt.xlabel("Pixels")

    # Cria um vetor com os dados da imagem
    imgArray = img.ravel()

    if cor is 1:

        # Precisa converter img em RGB para usar no pyplot
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        ax1.imshow(img)

    else:
        ax1.imshow(img, 'gray')

    ax3.hist(imgArray, 256, [0, 256])
    #plt.show()




# imread: 0 gray; 1 color; -1 alpha
cor = 0
img = cv2.imread('igreja.tif', cor)
HistLinhaBarra(img, cor)
HistBarra(img, cor)
HistLinha(img, cor)
plt.show()

cor = 1
img = cv2.imread('losroques.jpg', cor)
HistLinhaBarra(img, cor)
HistBarra(img, cor)
HistLinha(img, cor)
plt.show()

img = cv2.imread('suco.jpg', cor)
HistLinhaBarra(img, cor)
HistBarra(img, cor)
HistLinha(img, cor)
plt.show()
