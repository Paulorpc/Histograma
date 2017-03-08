from __future__ import division
import wx
import cv2
import numpy as np
from matplotlib import pyplot as plt
import math


##
# VERIFICA SE A IMAGEM E COLORIDA
#
# param: @img: Imagem
# Retorna: TRUE PARA COLORIDA.
##
def imgColorida(img):
    # Soma os elementos de cada canal
    img = cv2.sumElems(img)

    # Se a soma dos canais BGR forem iguais, entao a imgagem nao e colorida
    if (img[0] != img[1] != img[2]):
        return True
    else:
        return False

##
# HISTOGRAMA DE BARRAS
#
# param: @img: Imagem
##
def HistBarra(img):
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
    ax3.autoscale_view(True, True, True)

    plt.ylabel("Frequencia")
    plt.xlabel("Pixels")

    # Cria um vetor com os dados da imagem
    imgArray = img.ravel()

    if imgColorida(img) is True:

        # Precisa converter img em RGB para usar no pyplot
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        ax1.imshow(img)

    else:
        ax1.imshow(img, 'gray')

    ax3.hist(imgArray, 256, [0, 256])
    # plt.show()



##
# HISTOGRAMA DE LINHAS
#
# param: @img: Imagem
##
def HistLinha(img):
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
    ax2.autoscale_view(True, True, True)

    plt.ylabel("Frequencia")
    plt.xlabel("Pixels")

    if imgColorida(img) is True:
        # vetor de cores para linhas do histogram
        color = ('b', 'g', 'r')

        # Precisa converter img em RGB para usar no pylpot
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        ax1.imshow(img)

    else:
        # img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        color = ('b')
        ax1.imshow(img, 'gray')

    # For com a qtde de indices do vetor
    for i, cor in enumerate(color):
        hist = cv2.calcHist([img], [i], None, [256], [0, 256])
        ax2.plot(hist, color=cor)
        plt.xlim([0, 256])

        # plt.show()


##
# HISROGRAMA DE BARRAS + LINHA (COMPARATIVO)
#
# param: @img: Imagem
##
def HistLinhaBarra(img):
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
    ax2.autoscale_view(True, True, True)
    ax3.autoscale_view(True, True, True)

    plt.ylabel("Frequencia")
    plt.xlabel("Pixels")

    if imgColorida(img) is True:
        # vetor de cores para linhas do histogram
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
    # plt.show()



##
# CONVERSAO DE CORES DO PADRAO RGB PARA O HSI
#
# param: @img: Imagem
#
# Site para comparacao da conversao: http://www.had2know.com/technology/hsi-rgb-color-converter-equations.html
# https://en.wikipedia.org/wiki/HSL_and_HSV#Color-making_attributes
# Obs: Utilizando valores sem arredondamento em S. Para arredondar entre 0 e 1 melhor passar o array para int
##
def cvtColorRGB2HSI(img):

    imprimir = False
    RGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    # Pelo colorspace HSI trabalhar com a saturacao entre 0 e 1 definimoa o vetor com o tipo float
    # diferindo da imagem orifinal unicamente neste item. Original = uint8 (0 a 255)
    HSI = np.ndarray(shape=RGB.shape, dtype='f', order='F')
    linhas, colunas, ch = RGB.shape

    # Propriedades dos arrays de imagem
    if imprimir: print type(RGB), RGB.shape, RGB.size, RGB.dtype, RGB.ndim
    if imprimir: print type(HSI), HSI.shape, HSI.size, HSI.dtype, HSI.ndim


    for l in range(linhas):
        for c in range(colunas):

            if imprimir: print l, c

            # Valores do pxl R, G e B
            R = RGB.item(l, c, 0)
            G = RGB.item(l, c, 1)
            B = RGB.item(l, c, 2)
            if imprimir: print "RGB: ", R, G, B

            # intensidade
            I = (R + G + B) / 3

            # Valor minimo entre as cores RGB
            menor = min(R, G, B)

            #  saturacao
            if (I>0):
                S = 1 - menor / I
            else:
                S = 0
                I = 0


            # equacao para encontra hue
            num = ( 2 * R - G - B )
            den = ( 2 * math.sqrt( math.pow((R-G),2) + (R-B)*(G-B)) )

            # Como o arco cosseno vai apenas de 0 a 180 graus, para valores de B > G devemos subtrair de 360
            # pois H varia de 0-360 no HSI.
            # Importante: math.acos retorna o valor em rad entao e necessario converter para graus
            if ( G >= B ):
                H = math.degrees( math.acos( num / (den+0.000001)) )
            else:
                H = 360 - math.degrees( math.acos( num / (den+0.000001)) )


            H = round(H)
            S = S
            I = round(I)

            if imprimir: print "HSI: ", H, S, I, "\n"

            # Adicionamos os valores de HSI no array da imagem
            HSI.itemset((l, c, 0), H)
            HSI.itemset((l, c, 1), S)
            HSI.itemset((l, c, 2), I)

    return HSI


##
# HISTOGRAMAS HSV (HSB), HSL, HSI
#
# param: @img: Imagem
# param: @colorSpace histograma desejado: "HSV", "HSB", "HSL", "HSI"
# Retorna: Imagem convertida
##
def HistHSx(img, colorSpace):

    # Modelos de cores
    # HSV or HSB = Hue, Saturation and Brightness/Values
    # HSL        = Hue, Saturation and Lightness
    # HSI        = Hue, Saturation and Intensity

    # HSV frequentemente e chamado de HSB, ambos representam o mesmo espaco de cores
    arr_colorSpace = ["HSV", "HSB", "HSL", "HSI"]


    # Verifico se foi passado o parametro correto, senao retorna false
    if not arr_colorSpace.__contains__(colorSpace):
        return False


    # Ajustes do Figure
    fig  = plt.figure(4, figsize=(15, 8))
    tit = fig.suptitle("PDI: Histograma " + colorSpace, fontsize="x-large")
    tit.set_y(0.95)
    fig.subplots_adjust(top=0.85)

    ax1 = fig.add_subplot(221)
    ax2 = fig.add_subplot(223)

    if colorSpace.__eq__(arr_colorSpace[3]):
        ax3 = fig.add_subplot(322)
        ax4 = fig.add_subplot(324)
        ax5 = fig.add_subplot(326)

        ax3.set_title("Histograma " + colorSpace)

        ax3.autoscale_view(True, True, True)
        ax4.autoscale_view(True, True, True)
        ax5.autoscale_view(True, True, True)


    else:
        ax3 = fig.add_subplot(122)

    ax1.set_title("Imagem Original")
    ax2.set_title("Imagem " + colorSpace)

    ax1.axis('off')
    ax2.axis('off')


    # Converte imagem para padrao de cores e monta o histograma
    # channels = [0, 1]  # Porque e necessario processar ambos os planos H e S.
    # bins = [180, 256]  # 180 para o plano H e 256 para o plano S
    # range = [0, 180, 0, 256]  # Os valores do Hue estao entre 0 e 180 e da Saturation entre 0 and 256
    if colorSpace.__eq__(arr_colorSpace[0]) or colorSpace.__eq__(arr_colorSpace[1]):
        clr = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    elif colorSpace.__eq__(arr_colorSpace[2]):
        clr = cv2.cvtColor(img, cv2.COLOR_BGR2HLS)


    elif colorSpace.__eq__(arr_colorSpace[3]):
        clr = cvtColorRGB2HSI(img)


    if colorSpace.__eq__("HSI"):

        # Divido as cores da imagem para sua respectiva letra
        h, s, i = cv2.split(clr)

        # converto em um array continuo
        hArr = h.ravel()
        sArr = s.ravel()
        iArr = i.ravel()

        #print hmax, smax, imax

        # Configuracao do histograma de cada array
        ax3.hist(hArr, 361, [0, 361])   # H range de 0 a 360 graus
        ax4.hist(sArr, 100, [0,   1])   # Como a saturacao no HSI tem um range de 0 a 1, criou-se 100 bins neste range
        ax5.hist(iArr, 256, [0, 256])   # I range de 255


    # Se nao for HSI
    else:
        hist = cv2.calcHist([clr], [0, 1], None, [180, 256], [0, 180, 0, 256])
        ax3.imshow(hist)


    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    ax1.imshow(img)
    ax2.imshow(clr)



##
# LIMIARIZACAO RGB
#
# param: @img: Imagem
# param: @ri:  Regiao de interesse. Uma imagem com a regiao de interesse para fazer a mascara
##
def limearizacaoRGB(img, ri, l):

    # Ajustes do Figure
    fig = plt.figure(1, figsize=(15, 8))
    tit = fig.suptitle("PDI: Limiarizacao RGB", fontsize="x-large")
    tit.set_y(0.95)
    fig.subplots_adjust(top=0.85)

    ax1 = fig.add_subplot(221)
    ax2 = fig.add_subplot(223)
    ax3 = fig.add_subplot(122)

    ax1.set_title("Imagem Original")
    ax2.set_title("Mascara")
    ax3.set_title("Limiarizacao RGB")

    ax1.axis('off')
    ax2.axis('off')
    ax3.axis('off')

    # Converte a Regiao de Interesse (ri) da imagem e a imagem para HSV
    ri_hsv = cv2.cvtColor(ri, cv2.COLOR_BGR2HSV)
    img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    # Calcula o histograma da regiao de interesse
    # channels = [0, 1]  # Porque e necessario processar ambos os planos H e S.
    # bins = [180, 256]  # 180 para o plano H e 256 para o plano S
    # range = [0, 180, 0, 256]  # Os valores do Hue estao entre 0 e 180 e da Saturation entre 0 and 256
    ri_hist = cv2.calcHist([ri_hsv], [0, 1], None, [180, 256], [0, 180, 0, 256])

    # E necessario normalizar o histograma da Reg de interesse para aplicar o backProection
    cv2.normalize(ri_hist, ri_hist, 0, 255, cv2.NORM_MINMAX)

    # cria uma nova imagem com cada pixel como seu correspondente provavel da imagem(img) atraves da
    # razao(R = M/I) entre o histograma da regiao de intere (ri) e da imagem (img).
    #
    # Obs: B(x, y) = R[h(x, y), s(x, y)]. Depois disso aplica a condicao B(x, y) = min[B(x, y), 1].
    #
    # M = cv2.calcHist([hsv], [0, 1], None, [180, 256], [0, 180, 0, 256])
    # I = cv2.calcHist([hsvt], [0, 1], None, [180, 256], [0, 180, 0, 256])
    #
    # h, s, v = cv2.split(hsv_img)
    # B = R[h.ravel(), s.ravel()]
    # B = np.minimum(B, 1)
    # B = B.reshape(hsv_img.shape[:2])
    B = cv2.calcBackProject([img_hsv], [0, 1], ri_hist, [0, 180, 0, 256], 1)

    #ax1.imshow(B)

    # Agora e necessario convoluir com um disco circular B=D*B (D=disk kernel)
    disco = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))

    # cv2.filter2D(src, ddepth, kernel, dst) -> when ddepth=-1, the output image will have the same depth as the src
    cv2.filter2D(B, -1, disco, B)

    #ax2.imshow(B)

    # Aplica o threshold da limiarizacao e faz um AND Binario
    # como ja foi feito o recorte da ri, agora o thrsold ajuda a ajustar o resultado da imagem
    #l = limiar(passado por parametro)
    ret, thresh = cv2.threshold(B, l, 255, 0)
    thresh = cv2.merge((thresh, thresh, thresh))
    res = cv2.bitwise_and(img, thresh)


    linhas, colunas, ch = res.shape


    # Converto as cores do threshold da imagem do preto para vermelho
    for l in range(linhas):
        for c in range(colunas):

            if ( (res.item(l, c, 0) == 0) and (res.item(l, c, 1) == 0) and (res.item(l, c, 2) == 0) ):
                res.itemset((l, c, 0), 0)
                res.itemset((l, c, 1), 0)
                res.itemset((l, c, 2), 255)



    # converte padaro de cores para impressao no matplot
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    thresh = cv2.cvtColor(thresh, cv2.COLOR_BGR2RGB)
    res = cv2.cvtColor(res, cv2.COLOR_BGR2RGB)

    ax1.imshow(img)
    ax2.imshow(thresh)
    ax3.imshow(res)

    # Salva apenas a janela desejada
    saveAx2 = ax2.get_window_extent().transformed(fig.dpi_scale_trans.inverted())
    saveAx3 = ax3.get_window_extent().transformed(fig.dpi_scale_trans.inverted())
    fig.savefig('LimiarizacaoRGB_Thr.jpg', bbox_inches=saveAx2)
    fig.savefig('LimiarizacaoRGB_Res.jpg', bbox_inches=saveAx3)

    # Salva o plot como imagem
    #plt.savefig('teste.jpg')

    fig.clear()

    return img, thresh, res



##
# LIMIARIZACAO MANUAL HSI
#
# param: @img: Imagem
##
def limearizacaoHSI(img, th_h, th_s, th_i):

    # Ajustes do Figure
    fig = plt.figure(6, figsize=(15, 8))
    tit = fig.suptitle("PDI: Limiarizacao RGB", fontsize="x-large")
    tit.set_y(0.95)
    fig.subplots_adjust(top=0.85)

    ax1 = fig.add_subplot(221)
    ax2 = fig.add_subplot(223)
    #ax3 = fig.add_subplot(122)

    ax1.set_title("Imagem Original")
    ax2.set_title("Limiarizacao HSI")
    # ax3.set_title("Limiarizacao RGB")

    ax1.axis('off')
    ax2.axis('off')
    # ax3.axis('off')


    hsi = cvtColorRGB2HSI(img)
    h,s,i = cv2.split(hsi)

    hArr = h.ravel()
    sArr = s.ravel()
    iArr = i.ravel()

    # Calcula o histograma
    # channels = [0, 1]  # Porque e necessario processar ambos os planos H e S.
    # bins = [180, 256]  # 180 para o plano H e 256 para o plano S
    # range = [0, 180, 0, 256]  # Os valores do Hue estao entre 0 e 180 e da Saturation entre 0 and 256
    hist = cv2.calcHist([img], [0, 1], None, [360, 2], [0, 360, 0, 1])

    # E necessario normalizar o histograma da Reg de interesse para aplicar o backProection
    #cv2.normalize(hist, ri_hist, 0, 255, cv2.NORM_MINMAX)

    # Aplica o threshold da limiarizacao e faz um AND Binario


    ret, imgTh = cv2.threshold(img, th_h, 360, 0)

    print imgTh

    ax1.imshow(hist)
    ax2.imshow(imgTh)




def scale_bitmap(bitmap, width, height):
    image = wx.ImageFromBitmap(bitmap)
    image = image.Scale(width, height, wx.IMAGE_QUALITY_HIGH)
    result = wx.BitmapFromImage(image)
    return result



IMAGEM = 'LimiarizacaoRGB_Res.jpg'


class MainWindow(wx.Frame):
    def __init__(self):

        self.frame = wx.Frame.__init__(self, None, -1, "PDI: Software Histrogramas / Limiarizacao", size=(1024, 768))

        self.panel = wx.Panel(self, -1)
        self.bmp = wx.Image('color.jpg', wx.BITMAP_TYPE_JPEG).ConvertToBitmap()
        self.bmp = scale_bitmap(self.bmp, 513, 383)
        self.sbitmap = wx.StaticBitmap(self.panel, -1, self.bmp, (400, 10))

        self.label1 = wx.StaticText(self.panel, label="Limiarizacao RGB:", pos=(10, 10))
        self.label2  = wx.StaticText(self.panel, label="Digite o valor do Limiar (0-255):", pos=(10, 53))
        self.label3 = wx.StaticText(self.panel, label="Histogramas:", pos=(10, 250), size=(115, -1))
        self.label4 = wx.StaticText(self.panel, label="Limiar:", pos=(10, 73))
        self.textbox_Limiar = wx.TextCtrl(self.panel, pos=(50, 70), size=(115, -1))

        self.button1 =  wx.Button(self.panel, label="Atualizar Imagem", pos=(50, 130))
        self.button2 = wx.Button(self.panel, label="Imagem Original", pos=(50, 160))
        self.button3 = wx.Button(self.panel, label="Mascara", pos=(50, 190))
        self.button4 = wx.Button(self.panel, label="Histograma de Barra/Linha", pos=(50, 280))
        self.button5 = wx.Button(self.panel, label="Histogramas HSV", pos=(50, 310))
        self.button6 = wx.Button(self.panel, label="Histogramas HSL", pos=(50, 340))
        self.button7 = wx.Button(self.panel, label="Histogramas HSI", pos=(50, 370))

        self.button1.Bind(wx.EVT_BUTTON, self.OnButtonAction1)
        self.button2.Bind(wx.EVT_BUTTON, self.OnButtonAction2)
        self.button3.Bind(wx.EVT_BUTTON, self.OnButtonAction3)
        self.button4.Bind(wx.EVT_BUTTON, self.OnButtonAction4)
        self.button5.Bind(wx.EVT_BUTTON, self.OnButtonAction5)
        self.button6.Bind(wx.EVT_BUTTON, self.OnButtonAction6)
        self.button7.Bind(wx.EVT_BUTTON, self.OnButtonAction7)

        self.button3.Enable(False)

        self.button1.SetDefault()
        self.labelAuxImg = wx.StaticText(self.panel, label=IMAGEM, pos=(9999, 9999))


    ##
    ## HISTOGRAMA HSI
    ##
    def OnButtonAction7(self, event):
        img = cv2.imread('losroques.jpg')
        HistHSx(img, "HSI")
        plt.show()

        img = cv2.imread('color.png')
        HistHSx(img, "HSI")
        plt.show()


    ##
    ## HISTOGRAMA HSL
    ##
    def OnButtonAction6(self, event):
        img = cv2.imread('losroques.jpg')
        HistHSx(img, "HSL")
        plt.show()


    ##
    ## HISTOGRAMA HSV / HSB
    ##
    def OnButtonAction5(self, event):
        img = cv2.imread('losroques.jpg')
        HistHSx(img, "HSV")
        plt.show()


    ##
    ## HISTROGRAMAS DE BARRA E LINHA
    ##
    def OnButtonAction4(self, event):
        img = cv2.imread('igreja.tif')
        HistLinhaBarra(img)
        HistBarra(img)
        HistLinha(img)
        plt.show()

        img = cv2.imread('losroques.jpg')
        HistLinhaBarra(img)
        HistBarra(img)
        HistLinha(img)
        plt.show()

        

    ##
    ## LIMIARIZACAO RGB - Mascara
    ##
    def OnButtonAction3(self, event):
        img = 'LimiarizacaoRGB_Thr.jpg'
        self.labelAuxImg.SetLabel(img)

        self.bmp = wx.Image(img, wx.BITMAP_TYPE_JPEG).ConvertToBitmap()
        self.bmp = scale_bitmap(self.bmp, 513, 383)
        self.sbitmap.Destroy()
        self.sbitmap = wx.StaticBitmap(self.panel, -1, self.bmp, (400, 10))


    ##
    ## LIMIARIZACAO RGB - Imagem Original
    ##
    def OnButtonAction2(self, event):
        img = 'color.jpg'
        self.labelAuxImg.SetLabel(img)

        self.bmp = wx.Image(img, wx.BITMAP_TYPE_JPEG).ConvertToBitmap()
        self.bmp = scale_bitmap(self.bmp, 513, 383)
        self.sbitmap.Destroy()
        self.sbitmap = wx.StaticBitmap(self.panel, -1, self.bmp, (400, 10))



    ##
    ## LIMIARIZACAO RGB
    ##
    def OnButtonAction1(self, event):

        l = float(self.textbox_Limiar.GetValue())

        if (l is not ""):
            self.button3.Enable(True)

        #print type(l)
        img = cv2.imread('color.png')
        ri = cv2.imread('color_m1.png')
        limearizacaoRGB(img, ri, l)
        IMAGEM = 'LimiarizacaoRGB_Res.jpg'

        self.labelAuxImg.SetLabel(IMAGEM)

        self.bmp = wx.Image(IMAGEM, wx.BITMAP_TYPE_JPEG).ConvertToBitmap()
        self.bmp = scale_bitmap(self.bmp, 513, 383)
        self.sbitmap.Destroy()
        self.sbitmap = wx.StaticBitmap(self.panel, -1, self.bmp, (400, 10))



app = wx.PySimpleApp()
MainWindow().Show()
app.MainLoop()
