
from tkinter import* #Libreria para interfaz grafica
from io import*
def entry():  #Es la entrada para que la interfaz de tkinter nos ayude a ingresar las variables
    Diametro=float(diametro.get()) #Diametro del canal
    Ni=float(ni.get()) #N de manning inferior
    Ns=float(ns.get()) #N de Manning superior
    Qdiseno=float(qdiseno.get()) # Caudal del canal
    Spen=float(spen.get()) # Pendiente del canala
    gr=9.81 # Gravedad
    
    import numpy as np # se importa la libreria numpy o matematica 
    import math #Libreria para calculo de los angulos 
  
    alt=0.3*Diametro
    D=Diametro   
    n1=Ni
    n2=Ns   
    Q=Qdiseno   
    S=Spen
    
    #graficar un círculo
    import matplotlib.pyplot as plt # libreria para graficar
    import numpy as np # se importa la libreria numpy o matematica 
    from math import pi # se importa la libreria matematica 

    def xy(r,phi):
         return r*np.cos(phi), r*np.sin(phi)

    fig = plt.figure()
    ax = fig.add_subplot(111,aspect='equal')  

    phis=np.arange(0,6.28,0.01)
    r =Diametro/2
    ax.plot( *xy(r,phis), c='r',ls='-' )
   
    def nobre(Diametro,Ni,Ns,Qdiseno,Spen,alt,gr):
        if alt <= Diametro/2:
            alfa = 2*(math.acos((1-(2*(alt/Diametro)))))
            A = (alfa-math.sin(alfa))*Diametro**(2)/8
            P = alfa*Diametro/2
            T = (math.sin(alfa/2))*Diametro
            Rh = (1-(math.sin(alfa)/alfa))*Diametro/4
            Dh = A/T
            n = Ni
            V = Qdiseno/A
            Fr = V/((gr*Dh)**(1/2))
            Es = ((V**2)/(2*gr))+ alt
            s = ((Qdiseno*n)/(A*Rh**(2/3)))**2
       
        if alt > Diametro/2:
            alfa = 2*(math.acos((1-(2*(alt/Diametro)))))
            A = (alfa-math.sin(alfa))*((Diametro**2)/8)
            pc = (alfa*Diametro)/2
            pm = (pi/2)*Diametro
            P = pc - pm
            T = (math.sin(alfa/2))*Diametro
            Rh = (1-(math.sin(alfa)/alfa))*Diametro/4
            Dh = A/T
            n = ((((Ni**(3/2))*pm)+((Ns**(3/2))*P))/pc)**(2/3)
            V = Qdiseno/A
            Fr = V/((gr*Dh)**(1/2))
            Es = ((V**2)/(2*gr))+ alt
            s = ((Qdiseno*n)/(A*Rh**(2/3)))**2
        return A,P,T,Rh,Dh,n,V,Fr,Es,s
    f1=0.3*Diametro
    Qn=0.3*Qdiseno
    while Qdiseno!=Qn:
            A,P,T,Rh,Dh,n,V,Fr,Es,s=nobre(Diametro,Ni,Ns,Qdiseno,Spen,f1,gr)
            Qn=(1/n)*A*(Rh)**(2/3)*(Spen)**(1/2)
            if Qn-Qdiseno<0.0001 and Qn-Qdiseno>0:
                yn=f1
                break;
            elif Qdiseno-Qn<0.0001 and Qdiseno-Qn>0:
                yn=f1
                break;    
            if Qn<Qdiseno:
                f1=f1*1.0001
            elif Qn>Qdiseno:
                f1=f1*0.9999
    print(str(yn),"yn")
    print(str(A), "Area")
    print(str(T),"espejo de agua T")
    print(str(P), "perimetro")
    print(str(Rh), "radio hidraulico")
    print(str(Dh), "Profundidad hidraulica")
    print(str(V), "Velocidad")
    print(str(Es), "Energía específica")
    print(str(n), "n Equivalente")
    print(str(Fr), "Numero de Froude")
    f1=0.1*Diametro
    while Fr!=1:
        A,P,T,Rh,Dh,n,V,Fr,Es,s=nobre(Diametro,Ni,Ns,Qdiseno,Spen,f1,gr)
        if Fr-1<0.000001 and Fr-1>0:
            print(str(f1),"Yc")
            Yc=f1
            break;        
        elif 1-Fr<0.000001 and 1-Fr>0:
            print(str(f1),"Yc")
            Yc=f1
            break;
        if Fr>1:        
            f1=f1+0.000001
        elif Fr<1:
            f1=f1-0.000001

    yn1=yn-(Diametro/2)
    lis01=[(-1*(Diametro/2)),(Diametro/2)]
    yc1=Yc-(Diametro/2)
    lis02=[yn1,yn1]
    lis03=[yc1,yc1]
    lis04=[yn,yn]
    lis05=[Yc,Yc]
    lis06=[-10000,10000]
    plt.plot(lis01,lis02)
    plt.plot(lis01,lis03)
    plt.title('Canal Circular')
    plt.legend(('Canal','Yn', 'Yc'))
    #plt.show()
    
    import tkinter
    from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
    from matplotlib.figure import Figure
    import numpy as np
    
    #------------------------------CREAR VENTANA---------------------------------
    root = tkinter.Tk()
    root.wm_title("GRAFICA CANAL CIRCULAR")
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
#INICIO DE INTERFAZ GRAFICA DE USUARIO PARA MEJOR VISUALIZACIÓN 
raiz= Tk()

raiz.title("Calculo del canal circular")
raiz.resizable(0,0)
raiz.config(bg="red")

miframe= Frame()
miframe.pack()
miframe.config(bg="darkslategray")
miframe.config(width="1350" , height="600")
miframe.config(bd=10)
miframe.config(relief="raised")
miframe.config(cursor="arrow")
mimage=PhotoImage(file="2_canal_circular.png")
image= Label(miframe, image=mimage)
image.place(x=230,y=31,)

valor=DoubleVar() #ingrese valores
hh111=Label(miframe,text="INGRESE VALORES")
hh111.place(x=0, y=0, width=201, height=31)
hh111.config(bg="cyan2")

valor=DoubleVar() #Grafico del canal
hh222=Label(miframe,text="CANAL CIRCULAR")
hh222.place(x=600, y=0, width=300, height=25)
hh222.config(bg="cyan2")

#primera altura
valor=DoubleVar()
H1= Label(miframe,text="Diámetro del canal =")
H1.place(x=0, y=31, width=131, height=31)
diametro= Entry(miframe,textvariable=valor)
diametro.place(x=131,y=31, width=70,height=31)
diametro.config(bg="misty rose")

#segunda altura
valorb=DoubleVar()
H2= Label(miframe,text="n manning inferior =")
H2.place(x=0, y=62, width=131, height=31)
ni= Entry(miframe,textvariable=valorb)
ni.place(x=131,y=62, width=70,height=31)
ni.config(bg="misty rose")

#tercera altura
valorc=DoubleVar()
H3= Label(miframe,text="n manning superior =")
H3.place(x=0, y=93, width=131, height=31)
ns= Entry(miframe,textvariable=valorc)
ns.place(x=131,y=93, width=70,height=31)
ns.config(bg="misty rose")

#cuarta altura
valord=DoubleVar()
H4= Label(miframe,text="Caudal de diseño =")
H4.place(x=0, y=124, width=131, height=31)
qdiseno= Entry(miframe,textvariable=valord)
qdiseno.place(x=131,y=124, width=70,height=31)
qdiseno.config(bg="misty rose")

#primer ancho
valore=DoubleVar()
A1= Label(miframe,text="Pendiente del canal =")
A1.place(x=0, y=155, width=131, height=31)
spen= Entry(miframe,textvariable=valore)
spen.place(x=131,y=155, width=70,height=31)
spen.config(bg="misty rose")
#segundo ancho

#button
enviar=Button(miframe,text="Enviar",command=entry)
enviar.place(x=30, y=210, width=132,height=31)

ubicacionScanal=DoubleVar() #Para el valor de la pendiente Scanal
Scc=Label(miframe,text=" Nota: Diametro (m) -  N de manning - Caudal del canal (m^3/s) - Pendiente del canal")
Scc.place(x=0, y=530, width=800, height=31)

raiz.mainloop()

