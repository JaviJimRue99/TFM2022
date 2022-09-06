from distutils.log import debug
import math
import numpy as np

w = 2*math.pi/8760
dr = math.pi/180
hrs = np.arange(0,8760,0.1)
nPuntos = 8

def leeReferencia(Localizacion):
    ficheroReferencia = "Referencias/TMY_"+Localizacion+".txt"
    print('Localizacion:',Localizacion,'\n----------------------------------------------')
    
    RReferenciaAux = []

    file = open(ficheroReferencia,'r')
    lineas = file.readlines()
    contLinea = 0
    longitud = 0
    for linea in lineas:
        contLinea += 1 
        if contLinea == 1:
            a,b = linea.split(":")
            latitud = float(b)
            print('Latitud:',latitud)
            
        if contLinea == 2:
            a,b = linea.split(":")
            longitud = float(b)
            print('Longitud:',longitud)
        
        if contLinea >= 18  and contLinea <= 8777:
            a,b,c,d,e,f,g,h,i,j = linea.split(",")
            RReferenciaAux.append(float(d))
    file.close

    difUTC = math.floor((longitud+7.5)/15)
    RReferenciaAux = np.roll(RReferenciaAux,difUTC)
    x1 = np.arange(0,8760.1,8760/nPuntos)
    print('Puntos dia:', x1)
    RReferenciaAux = np.roll(RReferenciaAux,240) # Roll para comenzar el 21 de diciembre
    return RReferenciaAux, latitud, longitud, x1


def calcula_y1(Latitud,x1,DebugMode):
    fotoperiodo = []
    y1 = []
    for i in x1:
        dia = i/24
        sd = 23.45*dr*math.sin((2*math.pi*(dia+274))/365) 
        #sd para modelos que empiecen el 1 de enero -> 23.45*dr*math.sin((2*math.pi*(dia+284))/365)
        ws = math.acos(-math.tan(sd)*math.tan(Latitud*dr))
        wts = ws*(180/(math.pi*15))
        Tr = 12 - wts
        Ts = 12 + wts
        HorasDeSol = Ts - Tr
        fotoperiodo.append(HorasDeSol)
        y1.append(1 - HorasDeSol/12)
    if DebugMode == True:
        print('Horas de sol (fotoperiodo)\n--------------------------\n',fotoperiodo,'\n')
        print('y1\n--------------------------\n',y1,'\n')
    return y1, fotoperiodo

def calcula_y23(RReferencia,y1,DebugMode):
    y2 = []
    y3 = []
    cont = 0
    lista = RReferencia.tolist()

    for i in range(0,8760,int(8760/nPuntos)):
        mediaRAD = 0
        for j in range(i,i+168,24):
            mediaRAD += np.max(lista[j:j+168])
        mediaRAD = mediaRAD/7
        y3.append(mediaRAD/1000)
        cont += 1    
        if cont == 5:
            break
            
    # Añadimos los valores de radiacion de los puntos 0 y 1 y para forzar la simetria
    y3.append(y3[3])
    y3.append(y3[2])
    y3.append(y3[1])
    y3.append(y3[0]) 

    for i in range(len(y3)):
        y2.append(y3[i]+y1[i])
    if DebugMode == True:    
        print('y2\n--------------------------\n',y2,'\n')
        print('y3\n--------------------------\n',y3,'\n')
    return y2, y3

def calculaRadiacion(Ac2,hsol):
    s = []
    s1 = []
    s2 = []
    for i in range(87600):
        s1AUX=Ac2[i]*math.sin(2*math.pi/24*hrs[i]+3*math.pi/2)
        s2AUX=s1AUX-hsol[i]
        sAUX=(s2AUX+abs(s2AUX))/2
        s.append(sAUX)
        s1.append(s1AUX)
        s2.append(s2AUX)
    return s