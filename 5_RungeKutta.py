
import numpy as np # se importa la libreria numpy o matematica
import matplotlib.pyplot as plt # libreria para graficar
import pandas as pd #Libreria para calculo de los angulos teta
####LIBRERIAS PARA INTERFAZ TKINTER
import math #Libreria para calculo de los angulos teta
from tkinter import* #Libreria para interfaz grafica
def entry(): #Es la entrada para que la interfaz de tkinter nos ayude a ingresar las variables
    H1=float(h1.get()) #Ingrese la altura 1 del canal
    H2=float(h2.get()) #Ingrese la altura 2 del canal
    H3=float(h3.get()) #Ingrese la altura 3 del canal
    H4=float(h4.get()) #Ingrese la altura 4 del canal
    A1=float(a1.get()) #Ingrese el Ancho 1 del canal
    A2=float(a2.get()) #Ingrese el Ancho 2 del canal
    A3=float(a3.get()) #Ingrese el Ancho 3 del canal
    A4=float(a4.get()) #Ingrese el Ancho 4 del canal
    A5=float(a5.get()) #Ingrese el Ancho 5 del canal
    A6=float(a6.get()) #Ingrese el Ancho 6 del canal
    A7=float(a7.get()) #Ingrese el Ancho 7 del canal
    N1=float(n1.get()) #Ingrese el numero de la n de manning del Ancho 1 del canal
    N2=float(n2.get()) #Ingrese el numero de la n de manning del Ancho 2 del canal
    N3=float(n3.get()) #Ingrese el numero de la n de manning del Ancho 3 del canal
    N4=float(n4.get()) #Ingrese el numero de la n de manning del Ancho 4 del canal
    N5=float(n5.get()) #Ingrese el numero de la n de manning del Ancho 5 del canal
    N6=float(n6.get()) #Ingrese el numero de la n de manning del Ancho 6 del canal
    N7=float(n7.get()) #Ingrese el numero de la n de manning del Ancho 7 del canal
    Qcanal=float(Qc.get()) #Ingrese el caudal de diseño del canal en (m^3/s)
    Scanal=float(Sc.get()) #Ingrese la pendiente de diseño del canal (rad) 
    
    teta1=math.atan(A1/H1)
    teta2=math.atan(A3/H2)
    teta3=math.atan(A5/H3)
    teta4=math.atan(A7/H4)




    if H1 + H2 >= H3+H4:
        ymax= H3 + H4
    else:
        ymax= H1+H2
    
    x0=0
    y=ymax
    dx=-1000#float(input("escriba el valor de delta x para el canal : "))
    xf=-5000#float(input("escriba el último valor de x en el canal : "))
    k_list = []
    y_list = []
    p_list= []
    a_list= []
    n_list= []
    t_list= []
    rh_list= []
    dh_list= []
    v_list= []
    sf_list= []
    fr2_list= []
    x_list= []
    
    with open ('5_RungeKutta.txt', 'w') as file:
        file.write("    X            Y             A            P          T            n             V             Rh             Dh             Fr2        Sf           K\n")
        fase = 0
        for i in range (x0,xf+1,dx): 
            y_principal = y
            for e in range(0,4):
                if H3>=H2:
                    if y<=H2:
                        area1=((y**2)*math.tan(teta2))/2
                        area2=A4*y
                        area3=((y**2)*math.tan(teta3))/2
                        areat=area1+area2+area3
                        t=y*math.tan(teta2)+A4+y*math.tan(teta3)
                        pg=y/math.cos(teta2)
                        pi=y/math.cos(teta3)
                        pt=pg+A4+pi
                        nequiv=((((N3**(3/2))*pg)+((N4**(3/2))*A4)+((N5**(3/2))*pi))/pt)**(2/3)
                        rh=areat/pt
                        dh=areat/t
                        fr = (Qcanal)/((areat)*(9.81*dh)**(1/2))
                        Es = (Qcanal**(2))/(2*9.81*areat**(2)) + y
                        s = ((Qcanal*nequiv)/(areat*rh**(2/3)))**2
                        v= Qcanal/areat
                        fr2=fr**2
                        k=(Scanal-s)/(1-fr2)
                        
                    elif y>H2 and y<=H3:
                        area1=((y-H2)**2)*math.tan(teta1)
                        area2=(A2+A3+A4)*(y-H2)
                        area3=((y**2)*math.tan(teta3))/2
                        area4=(A3*H2)/2
                        area5=A4*H2
                        areat= area1 + area2 + area3 + area4 + area5
                        t=(y-H2)*math.tan(teta1)+A2+A3+A4+y*math.tan(teta3)
                        pe=(y-H2)/math.cos(teta1)
                        pg=H2/math.cos(teta2)
                        pi=y/math.cos(teta3)
                        pt=pe+A2+pg+A3+pi
                        nequiv=((((N1**(3/2))*pe)+((N2**(3/2))*A2)+((N3**(3/2))*pg)+((N4**(3/2))*A4)+((N5**(3/2))*pi))/pt)**(2/3)
                        rh=areat/pt
                        dh=areat/t
                        fr = (Qcanal)/((areat)*(9.81*dh)**(1/2))
                        Es = (Qcanal**(2))/(2*9.81*areat**(2)) + y
                        s = ((Qcanal*nequiv)/(areat*rh**(2/3)))**2
                        v= Qcanal/areat
                        fr2=fr**2
                        k=(Scanal-s)/(1-fr2)
                   
                    elif y>H3:
                        area1 = (((y-H2)**(2))*math.tan(teta1))/2
                        area2 = (A2+A3+A4+A5+A6)*(y-H3)
                        area3 = (A2+A3+A4+H2*math.tan(teta3))*(H3-H2)
                        area4=((y-H3)*A7)/2
                        area5= (A3*H2)/2
                        area6=A4*H2
                        area7= ((H2**(2))*(math.tan(teta3)))/2
                        area8= (((H3-H2)**(2))*math.tan(teta3))/2
                        areat = area1 + area2 + area3 + area4 + area5 + area6+ area7+area8
                        t = (y-H2) * math.tan(teta1) + A2 + A3 + A4 + A5 + A6 + (y-H3)*math.tan(teta4)
                        pe = (y - H2) / math.cos(teta1)
                        pg = H2 / math.cos(teta2)
                        pi = H3 / math.cos(teta3)
                        pk = (y - H3) / math.cos(teta4)
                        pt = pe + A2 + pg + A4 + pi + A6 + pk
                        nequiv= ((((N1**(3/2))*pe)+((N2**(3/2))*A2)+((N3**(3/2))*pg)+((N4**(3/2))*A4)+((N5**(3/2))*pi) + ((N6**(3/2))*A6) + ((N7**(3/2))*A7))/pt)**(2/3)
                        rh = areat/pt
                        dh = areat/t
                        fr = (Qcanal)/((areat)*(9.81*dh)**(1/2))
                        Es = (Qcanal**(2))/(2*9.81*areat**(2)) + y
                        s = ((Qcanal*nequiv)/(areat*rh**(2/3)))**2
                        v= Qcanal/areat
                        fr2=fr**2
                        k=(Scanal-s)/(1-fr2)
                    
                if H3 < H2:
                    if y <= H3:
                        area1=((y**2)*math.tan(teta2))/2
                        area2= A4*y
                        area3=((y**2)*math.tan(teta3))/2
                        areat= area1+area2+area3
                        t=y*math.tan(teta2) + A4 + y*math.tan(teta3)
                        pg=y/math.cos(teta2)
                        pi= y/math.cos(teta3)
                        pt= pg + A4 + pi
                        nequiv= ((((N3**(3/2))*pg)+((N4**(3/2))*A4)+((N5**(3/2))*pi))/pt)**(2/3)
                        rh= areat/pt
                        dh=areat/t
                        fr = (Qcanal)/((areat)*(9.81*dh)**(1/2))
                        Es = (Qcanal**(2))/(2*9.81*areat**(2)) + y
                        s = ((Qcanal*nequiv)/(areat*rh**(2/3)))**2
                        v= Qcanal/areat
                        fr2=fr**2
                        k=(Scanal-s)/(1-fr2)
                        
                    elif y > H3 and y <= H2:
                        area1=((y**2)*math.tan(teta2))/2
                        area2= A4*H3
                        area3=(A4 + A5 + A6)*(y - H3)
                        area4=(H3*A5)/2
                        area5=(((y-H3)**2)*math.tan(teta4))/2
                        areat= area1+area2+area3+area4+area5
                        t= y*math.tan(teta2) + A4 + A5 + A6 + (y-H3)/math.cos(teta4)
                        pg=y/math.cos(teta2)
                        pi=H3/math.cos(teta3)
                        pk=(y-H3)/math.cos(teta4)
                        pt=pg+A4+pi+pk+A6
                        nequiv= ((((N3**(3/2))*pg)+((N4**(3/2))*A4)+((N5**(3/2))*pi)+((N6**(3/2))*A6)+((N7**(3/2))*pk))/pt)**(2/3)
                        rh=areat/pt
                        dh=areat/t
                        fr = (Qcanal)/((areat)*(9.81*dh)**(1/2))
                        Es = (Qcanal**(2))/(2*9.81*areat**(2)) + y
                        s = ((Qcanal*nequiv)/(areat*rh**(2/3)))**2
                        v= Qcanal/areat
                        fr2=fr**2
                        k=(Scanal-s)/(1-fr2)
                        
                    elif y > H2:
                        area1=(((y-H2)**2)*math.tan(teta1))/2
                        area2=(A2+A3+A4+A5+A6)*(y-H2)
                        area3=(((y-H3)**2)*math.tan(teta4))/2
                        area4=(A5+A6)*(y-H3)
                        area5=A4*H2
                        area6=(A3*H2)/2
                        area7=(A6*H3)/2
                        areat= area1 + area2 + area3 + area4 * area5 + area6 + area7
                        t=(y-H2)*math.tan(teta1) + A2 + A3 + A4 + A5 + A6 + (y-H3)*math.tan(teta4)
                        pe=(y-H2)/math.cos(teta1)
                        pg=H2/math.cos(teta2)
                        pi=H3/math.cos(teta3)
                        pk=(y-H3)/math.cos(teta4)
                        pt=pe + A2 + pg + A4 + pi + A6 + pk
                        nequiv= ((((N1**(3/2))*pe)+((N2**(3/2))*A2)+((N3**(3/2))*pg)+((N4**(3/2))*A4)+((N5**(3/2))*pi) + ((N6**(3/2))*A6) + ((N7**(3/2))*A7))/pt)**(2/3)
                        rh=areat/pt
                        dh=areat/t
                        fr = (Qcanal)/((areat)*(9.81*dh)**(1/2))
                        Es = (Qcanal**(2))/(2*9.81*areat**(2)) + y
                        s = ((Qcanal*nequiv)/(areat*rh**(2/3)))**2
                        v= Qcanal/areat
                        fr2=fr**2
                        k=(Scanal-s)/(1-fr2)
                file.write('%12.7f %12.7f %12.7f %12.7f %12.7f %12.7f %12.7f %12.7f %12.7f %12.7f %12.7f %12.7f\n' % (i, y, areat, pt, t, nequiv, v,  rh, dh, fr2, s, k))
                if e <= 1:
                    kdx= k*dx
                    y_list.append(y)
                    k_list.append(k)
                    a_list.append(areat)
                    p_list.append(pt)
                    n_list.append(nequiv)
                    t_list.append(t)
                    rh_list.append(rh)
                    dh_list.append(dh)
                    v_list.append(v)
                    sf_list.append(s)
                    fr2_list.append(fr2)
                    y = y_principal+((k*dx)/2)
                
                elif e == 2:
                    kdx= k*dx
                    y_list.append(y)
                    k_list.append(k)
                    a_list.append(areat)
                    p_list.append(pt)
                    n_list.append(nequiv)
                    t_list.append(t)
                    rh_list.append(rh)
                    dh_list.append(dh)
                    v_list.append(v)
                    sf_list.append(s)
                    fr2_list.append(fr2)
                    y = y_principal+(k*dx)
                else:
                    kdx= k*dx
                    y_list.append(y)
                    k_list.append(k)
                    a_list.append(areat)
                    p_list.append(pt)
                    n_list.append(nequiv)
                    t_list.append(t)
                    rh_list.append(rh)
                    dh_list.append(dh)
                    v_list.append(v)
                    sf_list.append(s)
                    fr2_list.append(fr2)
                    y = y_principal + ((dx/6) * (k_list[0+fase] + 2*k_list[1+fase] + 2*k_list[2+fase] + k_list[3+fase]))
                    fase += 4# fase = fase + 4
                x_list.append(i)
                
    
    data = {'x':x_list,'Y':y_list,'Area':a_list,'Perimetro':p_list, 'T':t_list, 'n equiv':n_list, 'V':v_list, 'Rh':rh_list, 'Dh':dh_list, 'Fr2':fr2_list, 'Sf':sf_list, 'K':k_list }            
    data_df = pd.DataFrame(data)
    print()
    print('Grafica y tablas de valores')
    print('El valor de y+i se encuentra desde la fila 4 cada 4 filas, es decir, en cada cambio de la distancia x')
    print()
    print(data_df)
    
    nuevalista=[]
    for i in range(len(y_list)):
    	nuevalista.append(y_list[i]+k_list[i])
     
    fig=plt.figure() 
    plt.plot(x_list,y_list)
    plt.plot(x_list,nuevalista)
    
    plt.title('MUSKINGUM')
    plt.xlabel('x')
    plt.ylabel('y')
    #plt.show()
    import tkinter
    from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
    from matplotlib.figure import Figure
    import numpy as np
    
    #------------------------------CREAR VENTANA---------------------------------
    root = tkinter.Tk()
    root.wm_title("GRAFICA RGKUTTA")
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
    
#------------------------///------FIN CÁLCULOS NÚMERICOS---------
#INICIO DE INTERFAZ GRAFICA DE USUARIO PARA MEJOR VISUALIZACIÓN  
interfaz=Tk() #Nombre de la interfaz
interfaz.title("CÁLCULO DEL METODO RUNGE KUTTA")
interfaz.resizable(1,1)
interfaz.config(bg="black")
miframe=Frame()
miframe.pack()
miframe.config(bg="darkslategray")
miframe.config(width="1350" , height="600") #Tamaño del recuadro base de la interfaz
miframe.config(bd=10)
miframe.config(relief="raised")
miframe.config(cursor="arrow")
mimage=PhotoImage(file="5_RungeKutta.png") #Ingresar la imagen llamada:
image= Label(miframe, image=mimage)
image.place(x=230,y=31)

ubicacioN41=DoubleVar() #ingrese valores
hh111=Label(miframe,text="INGRESE VALORES")
hh111.place(x=0, y=0, width=201, height=25)
hh111.config(bg="cyan2")

ubicacioN41=DoubleVar() #Grafico del canal
hh222=Label(miframe,text="RUNGE KUTTA")
hh222.place(x=630, y=0, width=300, height=25)
hh222.config(bg="cyan2")

ubicacioN41=DoubleVar() #Para la primera altura H1
hh1=Label(miframe,text="H1=")
hh1.place(x=0, y=31, width=31, height=31)
h1=Entry(miframe,textvariable=ubicacioN41)
h1.place(x=31,y=31, width=70,height=31)
h1.config(bg="misty rose")

ubicacioN42=DoubleVar() #para la segunda altura H2
hh2=Label(miframe,text="H2=")
hh2.place(x=0, y=62, width=31, height=31)
h2=Entry(miframe,textvariable=ubicacioN42)
h2.place(x=31,y=62, width=70,height=31)
h2.config(bg="misty rose")

#Para la tercera altura H3
ubicacioN43=DoubleVar() #Para la tercera altura H3
hh3= Label(miframe,text="H3=")
hh3.place(x=0, y=93, width=31, height=31)
h3=Entry(miframe,textvariable=ubicacioN43)
h3.place(x=31,y=93, width=70,height=31)
h3.config(bg="misty rose")

ubicacioN44=DoubleVar() #Para la cuarta altura H4
hh4= Label(miframe,text="H4=")
hh4.place(x=0, y=124, width=31, height=31)
h4=Entry(miframe,textvariable=ubicacioN44)
h4.place(x=31,y=124, width=70,height=31)
h4.config(bg="misty rose")

ubicacionA1=DoubleVar() #Para el primer ancho A1
aa1=Label(miframe,text="A1=")
aa1.place(x=0, y=155, width=31, height=31)
a1=Entry(miframe,textvariable=ubicacionA1)
a1.place(x=31,y=155, width=70,height=31)
a1.config(bg="misty rose")

ubicacionA2=DoubleVar() #Para el segundo ancho A2
aa2=Label(miframe,text="A2=")
aa2.place(x=0, y=186, width=31, height=31)
a2=Entry(miframe,textvariable=ubicacionA2)
a2.place(x=31,y=186, width=70,height=31)
a2.config(bg="misty rose")

ubicacionA3=DoubleVar() #Para el tercer ancho A3
aa3=Label(miframe,text="A3=")
aa3.place(x=0, y=217, width=31, height=31)
a3=Entry(miframe,textvariable=ubicacionA3)
a3.place(x=31,y=217, width=70,height=31)
a3.config(bg="misty rose")

ubicacionA4=DoubleVar() #Para el cuarto ancho A4
aa4=Label(miframe,text="A4=")
aa4.place(x=0, y=248, width=31, height=31)
a4=Entry(miframe,textvariable=ubicacionA4)
a4.place(x=31,y=248, width=70,height=31)
a4.config(bg="misty rose")

ubicacionA5=DoubleVar() #Para el quinto ancho A5
aa5=Label(miframe,text="A5=")
aa5.place(x=0, y=279, width=31, height=31)
a5=Entry(miframe,textvariable=ubicacionA5)
a5.place(x=31,y=279, width=70,height=31)
a5.config(bg="misty rose")

ubicacionA6=DoubleVar() #Para el sexto ancho A6
aa6= Label(miframe,text="A6=")
aa6.place(x=0, y=310, width=31, height=31)
a6= Entry(miframe,textvariable=ubicacionA6)
a6.place(x=31,y=310, width=70,height=31)
a6.config(bg="misty rose")

ubicacionA7=DoubleVar() #Para el septimo ancho A7
aa7= Label(miframe,text="A7=")
aa7.place(x=0, y=341, width=31, height=31)
a7= Entry(miframe,textvariable=ubicacionA7)
a7.place(x=31,y=341, width=70,height=31)
a7.config(bg="misty rose")

ubicacionN1=DoubleVar() #Para el número de manning N1
nn1=Label(miframe,text="N1=")
nn1.place(x=102, y=31, width=31, height=31)
n1= Entry(miframe,textvariable=ubicacionN1)
n1.place(x=132,y=31, width=70,height=31)
n1.config(bg="misty rose")

ubicacionN2=DoubleVar() #Para el número de manning N2
nn2=Label(miframe,text="N2=")
nn2.place(x=102, y=62, width=31, height=31)
n2=Entry(miframe,textvariable=ubicacionN2)
n2.place(x=132,y=62, width=70,height=31)
n2.config(bg="misty rose")

ubicacionN3=DoubleVar() #Para el número de manning N3
nn3=Label(miframe,text="N3=")
nn3.place(x=102, y=93, width=31, height=31)
n3=Entry(miframe,textvariable=ubicacionN3)
n3.place(x=132,y=93, width=70,height=31)
n3.config(bg="misty rose")

ubicacionN4=DoubleVar() #Para el número de manning N4
nn4=Label(miframe,text="N4=")
nn4.place(x=102, y=124, width=31, height=31)
n4=Entry(miframe,textvariable=ubicacionN4)
n4.place(x=132,y=124, width=70,height=31)
n4.config(bg="misty rose")

ubicacionN5=DoubleVar() #Para el número de manning N5
nn5=Label(miframe,text="N5=")
nn5.place(x=102, y=155, width=31, height=31)
n5=Entry(miframe,textvariable=ubicacionN5)
n5.place(x=132,y=155, width=70,height=31)
n5.config(bg="misty rose")

ubicacionN6=DoubleVar() #Para el número de manning N6
nn6=Label(miframe,text="N6=")
nn6.place(x=102, y=186, width=31, height=31)
n6=Entry(miframe,textvariable=ubicacionN6)
n6.place(x=132,y=186, width=70,height=31)
n6.config(bg="misty rose")

ubicacionN7=DoubleVar() #Para el número de manning N7
nn7=Label(miframe,text="N7=")
nn7.place(x=102, y=217, width=31, height=31)
n7=Entry(miframe,textvariable=ubicacionN7)
n7.place(x=132,y=217, width=70,height=31)
n7.config(bg="misty rose")

ubicacionQcanal=DoubleVar() #Para el caudal del canal en (m3/s)
Qcc=Label(miframe,text="Qcanal=")
Qcc.place(x=102, y=248, width=50, height=31) #cambia el tamaño del recuadro
Qc=Entry(miframe,textvariable=ubicacionQcanal)
Qc.place(x=132,y=248, width=70,height=31)
Qc.config(bg="misty rose")

ubicacionScanal=DoubleVar() #Para el valor de la pendiente Scanal
Scc=Label(miframe,text="Scanal=")
Scc.place(x=102, y=279, width=50, height=31)
Sc=Entry(miframe,textvariable=ubicacionScanal)
Sc.place(x=132,y=279, width=70,height=31)
Sc.config(bg="misty rose")

#button
enviar=Button(miframe,text="Enviar datos",command=entry)
enviar.place(x=70, y=405)
enviar.config(bg="misty rose")

ubicacionScanal=DoubleVar() #Para el valor de la pendiente Scanal
Scc=Label(miframe,text=" Nota: H alturas (m) - θ angulos (°) - A distancias (m) - N de manning - Qcan Caudal del canal (m^3/s) - Scan Pendiente del canal")
Scc.place(x=0, y=530, width=800, height=31)

interfaz.mainloop()  #Fin de la interfaz grafica