import math
import numpy as np
import funcionAjuste
import funcionesAuxiliares as fun_aux


hrs = np.arange(0,8760,0.1)

def ejecutaTest(Test,Debug, latitud, sAjuste):
    dr = math.pi/180
    if Test:
        contF, contA = 0,0
        for dia in range(365):
            if Debug:
                print(dia,'\n------------------------------------------------')
            sd = 23.45*dr*math.sin((2*math.pi*(dia+274))/365) 
            ws = math.acos(-math.tan(sd)*math.tan(latitud*dr))
            wts = ws*(180/(math.pi*15))
            Tr = 12 - wts
            Ts = 12 + wts
            HorasDeSol = Ts - Tr
            
            duracion = 0
            
            for i in sAjuste[(dia*240):(dia*240)+240]:
                if i != 0:
                    duracion = duracion + 1
            duracion = duracion   /10
            diferenciaAUX = abs(HorasDeSol-duracion)
            if diferenciaAUX <= 0.3:
                contA += 1
                if Debug:
                    print(HorasDeSol,'',duracion,'-> OK(',abs(HorasDeSol-duracion),')\n') 
            else:
                contF += 1
                if Debug:
                    print(HorasDeSol,'',duracion,'-> ********FALLO(',abs(HorasDeSol-duracion),')********\n')


        print('ACIERTOS =',contA,'FALLOS =',contF)
    else:
        print('TEST DESACTIVADO')

def radAjustada(y1,y2,x1,delta,epsilon):
    # normalizacion entre 0 y 1 -> (x_i - min(x)) / (max(x) - min (x))
    y1Ajuste = []
    y2Ajuste = []
    for cont in range(0,9,1):
        if cont == 0 or cont == 8:
            y1Ajuste.append(y1[cont]+delta)
            y2Ajuste.append(y2[cont]+delta)
        elif cont ==1:
            dif = (y1[cont] - y1[2]) / (y1[0]-y1[2])
            y1Ajuste.append(y1[cont]+delta*dif)
            y2Ajuste.append(y2[cont]+delta*dif)
        elif cont ==2 or cont == 6:
            y1Ajuste.append(y1[cont])
            y2Ajuste.append(y2[cont])
        elif cont ==3:
            dif = (y1[cont] - y1[2]) / (y1[4]-y1[2])
            y1Ajuste.append(y1[cont]+epsilon*dif)
            y2Ajuste.append(y2[cont]+epsilon*dif)
        elif cont ==4:
            y1Ajuste.append(y1[cont]+epsilon)
            y2Ajuste.append(y2[cont]+epsilon)
        elif cont ==5:
            dif = (y1[cont] - y1[6]) / (y1[4]-y1[6])
            y1Ajuste.append(y1[cont]+epsilon*dif)
            y2Ajuste.append(y2[cont]+epsilon*dif)
        elif cont ==7:
            dif = (y1[cont] - y1[6]) / (y1[8]-y1[6])
            y1Ajuste.append(y1[cont]+delta*dif)
            y2Ajuste.append(y2[cont]+delta*dif)

    #------------------------------------------------------------------
    hsolAjuste = funcionAjuste.ajuste(y1Ajuste,x1)
    Ac2Ajuste = funcionAjuste.ajuste(y2Ajuste,x1)
    sAjuste = fun_aux.calculaRadiacion(Ac2Ajuste, hsolAjuste)       
    return sAjuste
