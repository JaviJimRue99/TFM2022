from matplotlib import pyplot as plt
import numpy as np

hrs = np.arange(0,8760,0.1)
# RADIACION AÑO COMPLETO
def muestraRadiacion(x1, y3, s):
    plt.figure()
    plt.plot(x1,y3,'*',hrs,s,c='dodgerblue')
    plt.xlabel("Time(h)")
    plt.ylabel("Solar Irradiance(W/m²)")
    plt.show()
    
# PRIMAVERA
def muestraPrimavera(x1, y3, s, dias):
    plt.figure()
    comienzo = 79
    plt.xlim((comienzo*24, (comienzo+dias)*24))
    plt.plot(x1,y3,'*',hrs,s,c='dodgerblue')
    plt.title('Primavera')
    plt.xlabel("Time(h)")
    plt.ylabel("Solar Irradiance(W/m²)")
    plt.show()
    
# VERANO
def muestraVerano(x1, y3, s, dias):
    plt.figure()
    comienzo = 172
    plt.xlim((comienzo*24, (comienzo+dias)*24))
    plt.plot(x1,y3,'*',hrs,s,c='dodgerblue')
    plt.title('Verano')
    plt.xlabel("Time(h)")
    plt.ylabel("Solar Irradiance(W/m²)")
    plt.show()

# OTOÑO
def muestraOtonio(x1, y3, s, dias):
    plt.figure()
    comienzo = 266
    plt.xlim((comienzo*24, (comienzo+dias)*24))
    plt.plot(x1,y3,'*',hrs,s,c='dodgerblue')
    plt.title('Otoño')
    plt.xlabel("Time(h)")
    plt.ylabel("Solar Irradiance(W/m²)")
    plt.show()

# INVIERNO
def muestraInvierno(x1, y3, s, dias):
    plt.figure()
    comienzo = 355
    plt.xlim((comienzo*24, (comienzo+dias)*24))
    plt.plot(x1,y3,'*',hrs,s,c='dodgerblue')
    plt.title('Invierno')
    plt.xlabel("Time(h)")
    plt.ylabel("Solar Irradiance(W/m²)")
    plt.show()
