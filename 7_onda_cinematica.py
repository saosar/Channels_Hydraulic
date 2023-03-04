
import numpy as np # se importa la libreria numpy o matematica 
import math  #Libreria para calculo de los angulos teta
import matplotlib.pyplot as plt # libreria para graficar
import pandas as pd #Libreria para calculo de los angulos teta
from tkinter import* #Libreria para interfaz grafica
def entry(): #Es la entrada para que la interfaz de tkinter nos ayude a ingresar las variables
    H1=float(h1.get()) #Ancho del canal    
    H2=float(h2.get()) #Pendiente del canal
    H3=float(h3.get()) #Intervalo del tiempo
    H4=float(h4.get()) #delta de la distancia x del canal
    H5=float(h5.get()) #N de maning
    
    #Calculos
    phi=((H5*(H1)**(2/3))/((H2)**(1/2)))**(3/5)
    tx=(H3/H4)
    la=3/5
    ti=0
    Dt=3# delta del tiempo de transito
    
    
    
    rows = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60]
    
    cols = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    de1 = np.arange(671).reshape(61, 11)
    de = np.asarray(de1, dtype = float)
    de[rows,cols] = (15.0,20.0,25,30,35,40,45,50,55,60,65,63.75,62.5,61.25,60,58.75,57.5,56.25,55,53.75,52.5,51.25,50,48.75,47.5,46.25,45,43.75,42.5,41.25,40,38.75,37.5,36.25,35,33.75,32.5,31.25,30,28.75,27.5,26.25,25,23.75,22.5,21.25,20,18.75,17.5,16.25,15,15,15,15,15,15,15,15,15,15,15)#la debe importar el usuario
    rows=[0,0,0,0,0,0,0,0,0,0,0]
    cols=[0,1,2,3,4,5,6,7,8,9,10]
    de[rows,cols]=(15,15,15,15,15,15,15,15,15,15,15)
    Q1=de[rows,cols][0]# j+1Qi
    Q2=de[rows,cols][1]# jQi+1
    time=[]
    
    
    j=1
    while j<61:
        i=1
        while i<11:
            Q1=de[j][i-1]
            Q2=de[j-1][i]
            Q3=((tx*(Q1)+(phi*la*Q2*((Q2+Q1)/2)**(la-1)))/(tx+(phi*la*((Q1+Q2)/2)**(la-1))))
    
            rows=[j]
            cols=[i]
            de[rows,cols]=(Q3)
            i=i+1    
        j=j+1
        
    dist=de[1:,] 
       
    for i in range (0,len(dist)):
        ti= ti + Dt
        time.append(ti)
        
    np.savetxt('7_onda_cinematica.txt', de,header='onda cinemática', fmt='%10.8f',delimiter='\t')
    time.insert(0,0)
    
    dist1=de[:,1]
    dist2=de[:,2]
    dist3=de[:,3]
    dist4=de[:,4]    
    dist5=de[:,5]
    dist6=de[:,6]    
    dist7=de[:,7]
    dist8=de[:,8]        
    dist9=de[:,9]
    dist10=de[:,10]
    
    data = {'tiempo':time,'km_1000':dist1, 'km_2000':dist2,'km_3000':dist3,'km_4000':dist4, 'km_5000':dist5}
    data2= {'km_6000':dist6, 'km_7000':dist7,'km_8000':dist8, 'km_9000':dist9, 'km_10000':dist10,}
    data_df = pd.DataFrame(data)
    data2_df = pd.DataFrame(data2)
    print()
    print('Tablas de valores')
    print()
    print(data_df)
    print()
    print(data2_df)
    
    fig=plt.figure()
    plt.plot(time,dist1)
    plt.plot(time,dist2)
    plt.plot(time,dist3)
    plt.plot(time,dist4)
    plt.plot(time,dist5)
    plt.plot(time,dist6)
    plt.plot(time,dist7)
    plt.plot(time,dist8)
    plt.plot(time,dist9)
    plt.plot(time,dist10)
    
    plt.title('Transito de crecientes-onda cinematica (Caudal vs Tiempo)')
    plt.xlabel('Tiempo(s)')
    plt.ylabel('Caudal(m3/s)')
    plt.legend(('1000m','2000m', '3000m','4000m','5000m', '6000m','7000m','8000m', '9000m','10000'))
    plt.show()
    
    

#------------------------///------FIN CÁLCULOS NÚMERICOS---------
#INICIO DE INTERFAZ GRAFICA DE USUARIO PARA MEJOR VISUALIZACIÓN  
interfaz=Tk() #Nombre de la interfaz
interfaz.title("CÁLCULO DE LA ONDA CINEMATICA")
interfaz.resizable(1,1)
interfaz.config(bg="black")
miframe=Frame()
miframe.pack()
miframe.config(bg="darkslategray")
miframe.config(width="1350" , height="600") #Tamaño del recuadro base de la interfaz
miframe.config(bd=10)
miframe.config(relief="raised")
miframe.config(cursor="arrow")
mimage=PhotoImage(file="7_onda_cinematica.png") #Ingresar la imagen llamada:
image= Label(miframe, image=mimage)
image.place(x=230,y=31)

ubicacioN41=DoubleVar() #ingrese valores
hh111=Label(miframe,text="INGRESE VALORES")
hh111.place(x=0, y=0, width=201, height=25)
hh111.config(bg="cyan2")

ubicacioN41=DoubleVar() #Grafico del canal
hh222=Label(miframe,text="ONDA CINEMATICA")
hh222.place(x=630, y=0, width=300, height=25)
hh222.config(bg="cyan2")

ubicacioN41=DoubleVar() #Para la primera altura H1
hh1=Label(miframe,text="Ancho del canal=")
hh1.place(x=0, y=31, width=131, height=31)
h1=Entry(miframe,textvariable=ubicacioN41)
h1.place(x=131,y=31, width=70,height=31)
h1.config(bg="misty rose")

ubicacioN42=DoubleVar() #para la segunda altura H2
hh2=Label(miframe,text="Pendiente del canal=")
hh2.place(x=0, y=62, width=131, height=31)
h2=Entry(miframe,textvariable=ubicacioN42)
h2.place(x=131,y=62, width=70,height=31)
h2.config(bg="misty rose")

#Para la tercera altura H3
ubicacioN43=DoubleVar() #Para la tercera altura H3
hh3= Label(miframe,text="Intervalo del tiempo=")
hh3.place(x=0, y=93, width=131, height=31)
h3=Entry(miframe,textvariable=ubicacioN43)
h3.place(x=131,y=93, width=70,height=31)
h3.config(bg="misty rose")

ubicacioN44=DoubleVar() #Para la cuarta altura H4
hh4= Label(miframe,text="Delta x=")
hh4.place(x=0, y=124, width=131, height=31)
h4=Entry(miframe,textvariable=ubicacioN44)
h4.place(x=131,y=124, width=70,height=31)
h4.config(bg="misty rose")

ubicacionA1=DoubleVar() #Para el primer ancho A1
aa1=Label(miframe,text="N de maninng=")
aa1.place(x=0, y=155, width=131, height=31)
h5=Entry(miframe,textvariable=ubicacionA1)
h5.place(x=131,y=155, width=70,height=31)
h5.config(bg="misty rose")

enviar=Button(miframe,text="Enviar datos",command=entry)
enviar.place(x=70, y=230)
enviar.config(bg="misty rose")

ubicacionScanal=DoubleVar() #Para el valor de la pendiente Scanal
Scc=Label(miframe,text=" Nota: Ancho del canal (m) -  N de manning - Delta de x (m) - Intervalo de tiempo (min) - Pendiente del canal")
Scc.place(x=0, y=530, width=800, height=31)

interfaz.mainloop()  #Fin de la interfaz grafica