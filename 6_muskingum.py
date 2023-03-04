
from tkinter import* #Libreria para interfaz grafica
from io import*
def entry(): #Es la entrada para que la interfaz de tkinter nos ayude a ingresar las variables
    #H1=float(h1.get()) #Ingrese la altura 1 del canal
    H1=float(h1.get())# Dato de la hidrografa 1
    H2=float(h2.get())# Dato de la hidrograda 2
    H3=float(h3.get())# Dato de la hidrografa 3
    H4=float(h4.get())# Dato de la hidrograda 4
    H5=float(h5.get())# Dato de la hidrografa 5
    H6=float(h6.get())# Dato de la hidrografa 6
    H7=float(h7.get())# Dato de la hidrografa 7        
    H8=float(h8.get())# Dato de la hidrografa 8
    H9=float(h9.get())# Dato de la hidrografa 9
    HH=int(hh.get())# Numero total de las hidrografas utilizadas
    HS=float(hs.get())# intervalos en minutos
    HX=float(hx.get())# Valor de x
    HK=float(hk.get())# Valor de k
    k=HK
    x=HX
    dt=HS
    lis9=[H1,H2,H3,H4,H5,H6,H7,H8,H9]
    lis10=[]
    i=0
    while i < HH:
        lis10.append(lis9[i])
        i=i+1
    i=0    
    tiempo=0
    oi = lis10[0]
    
    c0 = (dt-2*k*x)/(dt+2*k*(1-x))
    c1 = (dt+2*k*x)/(dt+2*k*(1-x))
    c2 = (-dt+2*k*(1-x))/(dt+2*k*(1-x))
    lista_tiempo=[]
    lista_tiempo.append(tiempo)
    lista_o=[]
    lista_o.append(oi)
    while i<HH-1:
        if i==0:
            Oj = c0*lis10[i+1] + c1*lis10[i] + c2*oi
            lista_o.append(Oj)
        else:            
            Oj = c0*lis10[i+1] + c1*lis10[i] + c2*Oj
            lista_o.append(Oj)
        tiempo=tiempo+dt
        lista_tiempo.append(tiempo)
        i=i+1
    print('c0=',"{:.3f}".format(c0),'c1=',"{:.3f}".format(c1),'c2=',"{:.3f}".format(c2),) 
    print('Los caudales medios de salida durante el intervalo son, O =', lista_o[0:9])
    #lista_o.insert(0,oi)
    #data = {'I':lis9,'O':lista_o} 
    #data_df = pd.DataFrame(data)
    #print()
    #print(data)
    import matplotlib.pyplot as plt #importar libreria para graficar
    import numpy as np
    
    fig=plt.figure()  
    plt.plot(lista_tiempo,lis10)
    plt.plot(lista_tiempo,lista_o)


    plt.title('Transito de creciente Muskingum')
    plt.xlabel('tiempo')
    plt.ylabel('caudal')
    plt.legend(('I','O'))
    #plt.show()
    
    import tkinter
    from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
    from matplotlib.figure import Figure
    import numpy as np
    
    #------------------------------CREAR VENTANA---------------------------------
    root = tkinter.Tk()
    root.wm_title("GRAFICA MUSKINGUM")
    #------------------------------CREAR GRAFICA---------------------------------

    canvas = FigureCanvasTkAgg(fig, master=root)  # CREAR AREA DE DIBUJO DE TKINTER.
    canvas.draw()
    canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)
    
    #-----------------------AÑADIR BARRA DE HERRAMIENTAS--------------------------
    toolbar = NavigationToolbar2Tk(canvas, root)# barra de iconos
    toolbar.update()
    canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=5)
    
    #-----------------------------BOTÓN "cerrar"----------------------------------
    def cerrar():
        root.quit()     
        root.destroy()
    
    button = tkinter.Button(master=root, text="cerrar", command=cerrar)
    button.pack(side=tkinter.BOTTOM)
    
    tkinter.mainloop()
    
    
#Comienzo de la interfaz grafica 

raiz= Tk()

raiz.title("Tránsito De Creciente-Muskingum")
raiz.resizable(0,0)
raiz.config(bg="red")

miframe= Frame()
miframe.pack()
miframe.config(bg="darkslategray")
miframe.config(width="1350" , height="600")
miframe.config(bd=10)
miframe.config(relief="groove")
miframe.config(cursor="hand2")
mimage=PhotoImage(file="6_muskingum.png") #Ingresar la imagen llamada:
image= Label(miframe, image=mimage)
image.place(x=230,y=31)



H10= Label(miframe,text="INGRESE LOS VALORES")
H10.place(x=0, y=0, width=200, height=31)
H10.config(bg="cyan2")

valor=DoubleVar() #Grafico del canal
hh222=Label(miframe,text="MUSKINGUM")
hh222.place(x=610, y=0, width=300, height=25)
hh222.config(bg="cyan2")

# Datos de las hidrografas
valor=DoubleVar()
hh1=Label(miframe,text="Hidrógrafa 1=")
hh1.place(x=0, y=31, width=130, height=31)
h1= Entry(miframe,textvariable=valor)
h1.place(x=130,y=31, width=70,height=31)
h1.config(bg="misty rose")

valor1=DoubleVar()
hh2=Label(miframe,text="Hidrógrafa 2=")
hh2.place(x=0, y=62, width=130, height=31)
h2= Entry(miframe,textvariable=valor1)
h2.place(x=130,y=62, width=70,height=31)
h2.config(bg="misty rose")

valor2=DoubleVar()
hh3=Label(miframe,text="Hidrógrafa 3=")
hh3.place(x=0, y=93, width=130, height=31)
h3= Entry(miframe,textvariable=valor2)
h3.place(x=130,y=93, width=70,height=31)
h3.config(bg="misty rose")

valor3=DoubleVar()
hh4=Label(miframe,text="Hidrógrafa 4=")
hh4.place(x=0, y=124, width=130, height=31)
h4= Entry(miframe,textvariable=valor3)
h4.place(x=130,y=124, width=70,height=31)
h4.config(bg="misty rose")

valor4=DoubleVar()
hh5=Label(miframe,text="Hidrógrafa 5=")
hh5.place(x=0, y=155, width=130, height=31)
h5= Entry(miframe,textvariable=valor4)
h5.place(x=130,y=155, width=70,height=31)
h5.config(bg="misty rose")

valor5=DoubleVar()
hh6=Label(miframe,text="Hidrógrafa 6=")
hh6.place(x=0, y=186, width=130, height=31)
h6= Entry(miframe,textvariable=valor5)
h6.place(x=130,y=186, width=70,height=31)
h6.config(bg="misty rose")

valor6=DoubleVar()
hh7=Label(miframe,text="Hidrógrafa 7=")
hh7.place(x=0, y=217, width=130, height=31)
h7= Entry(miframe,textvariable=valor6)
h7.place(x=130,y=217, width=70,height=31)
h7.config(bg="misty rose")

valor7=DoubleVar()
hh9=Label(miframe,text="Hidrógrafa 8=")
hh9.place(x=0, y=248, width=130, height=31)
h8= Entry(miframe,textvariable=valor7)
h8.place(x=130,y=248, width=70,height=31)
h8.config(bg="misty rose")

valor8=DoubleVar()
hh9=Label(miframe,text="Hidrógrafa 9=")
hh9.place(x=0, y=279, width=130, height=31)
h9= Entry(miframe,textvariable=valor8)
h9.place(x=130,y=279, width=70,height=31)
h9.config(bg="misty rose")

#Datos de las variables x,k,dt
valor10=IntVar()
H11= Label(miframe,text="N°total de hidrografas=")
H11.place(x=0, y=310, width=130, height=31)
hh= Entry(miframe,textvariable=valor10)
hh.place(x=130,y=310, width=70,height=31)
hh.config(bg="misty rose")

valorb=DoubleVar()
H12= Label(miframe,text="Valor de los intervalos=")#minutos
H12.place(x=0, y=341, width=130, height=31)
hs= Entry(miframe,textvariable=valorb)
hs.place(x=130,y=341, width=70,height=31)
hs.config(bg="misty rose")

valorc=DoubleVar()
H13= Label(miframe,text="Valor de X= ")
H13.place(x=0, y=372, width=130, height=31)
hx= Entry(miframe,textvariable=valorc)
hx.place(x=130,y=372, width=70,height=31)
hx.config(bg="misty rose")

valord=DoubleVar()
H5= Label(miframe,text="Valor de K=")
H5.place(x=0, y=403, width=130, height=31)
hk= Entry(miframe,textvariable=valord)
hk.place(x=130,y=403, width=70,height=31)
hk.config(bg="misty rose")

#button
enviar=Button(miframe,text="Enviar",command=entry)
enviar.place(x=65, y=450)




raiz.mainloop()


