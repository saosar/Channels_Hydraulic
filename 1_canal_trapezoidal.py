####LIBRERIAS NECESARIAS PARA GRAFICAS PLOT
import numpy as np # se importa la libreria numpy o matematica 
import matplotlib.pyplot as plt # libreria para graficar
import pandas as pd # para crear el data frame
####Libreria para dibujo de canal
import turtle
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
    

 #######------- Para hallar Yn (Y normal) 
    Yn = 2         # Yn asumido=2	
    for i in range(0, 1000): 
        if H3>=H2:      #CASO_1: La altura 3 es mayor o igual a la altura 2.
            if Yn<=H2:  #Yn esta por debajo o igual a la altura 2
                area1=((Yn**2)*math.tan(teta2))/2
                area2=A4*Yn
                area3=((Yn**2)*math.tan(teta3))/2
                areat=area1+area2+area3
                t=Yn*math.tan(teta2)+A4+Yn*math.tan(teta3)
                pA3=Yn/math.cos(teta2)
                pA5=Yn/math.cos(teta3)
                pt=pA3+A4+pA5
                Nequivalente=((((N3**(3/2))*pA3)+((N4**(3/2))*A4)+((N5**(3/2))*pA5))/pt)**(2/3)
                Rh=areat/pt
                Dh=areat/t
            elif Yn>H2 and Yn<=H3: #Yn es mayor a la altura 2 y menor o igual a la altura 3
                area1=((Yn-H2)**2)*math.tan(teta1)
                area2=(A2+A3+A4)*(Yn-H2)
                area3=((Yn**2)*math.tan(teta3))/2
                area4=(A3*H2)/2
                area5=A4*H2
                areat= area1 + area2 + area3 + area4 + area5
                t=(Yn-H2)*math.tan(teta1)+A2+A3+A4+Yn*math.tan(teta3)
                pA1=(Yn-H2)/math.cos(teta1)
                pA3=H2/math.cos(teta2)
                pA5=Yn/math.cos(teta3)
                pt=pA1+A2+pA3+A3+pA5  ########REVISAR, PROBABLEMENTE MALO EN OTRO CODIGO DE AJA porque se suma pendiente A3 Y A3 tambien?
                Nequivalente=((((N1**(3/2))*pA1)+((N2**(3/2))*A2)+((N3**(3/2))*pA3)+((N4**(3/2))*A4)+((N5**(3/2))*pA5))/pt)**(2/3)
                Rh=areat/pt
                Dh=areat/t
            elif Yn>H3: #Yn es mayor a la altura 3
                area1 = (((Yn-H2)**(2))*math.tan(teta1))/2
                area2 = (A2+A3+A4+A5+A6)*(Yn-H3)
                area3 = (A2+A3+A4+H2*math.tan(teta3))*(H3-H2)
                area4=((Yn-H3)*A7)/2
                area5= (A3*H2)/2
                area6=A4*H2
                area7= ((H2**(2))*(math.tan(teta3)))/2
                area8= (((H3-H2)**(2))*math.tan(teta3))/2
                areat = area1+area2+area3+area4+area5+area6+area7+area8
                t = (Yn-H2) * math.tan(teta1) + A2 + A3 + A4 + A5 + A6 + (Yn-H3)*math.tan(teta4)
                pA1 = (Yn - H2) / math.cos(teta1)
                pA3 = H2 / math.cos(teta2)
                pA5 = H3 / math.cos(teta3)
                pA7 = (Yn - H3) / math.cos(teta4)
                pt = pA1 + A2 + A3 + A4 + pA5 + A6 + pA7
                Nequivalente= ((((N1**(3/2))*pA1)+((N2**(3/2))*A2)+((N3**(3/2))*pA3)+((N4**(3/2))*A4)+((N5**(3/2))*pA5) + ((N6**(3/2))*A6) + ((N7**(3/2))*A7))/pt)**(2/3)
                Rh = areat/pt
                Dh = areat/t
            elif H3+H4 >= H2+H1 and Yn> H3+H4: #Si Una altura total de un lado del canal es mayor a la del otro lado, ocurrira desbordamiento
                print("Desbordamiento del agua en el canal")
                
                
        if H3 < H2:         #CASO_2: La altura 3 es menor a la altura 2.
            if Yn <= H3:    #Yn esta por debajo o igual a la altura 3
                area1=((Yn**2)*math.tan(teta2))/2
                area2= A4*Yn
                area3=((Yn**2)*math.tan(teta3))/2
                areat= area1+area2+area3
                t=Yn*math.tan(teta2) + A4 + Yn*math.tan(teta3)
                pA3=Yn/math.cos(teta2)
                pA5= Yn/math.cos(teta3)
                pt= pA3 + A4 + pA5
                Nequivalente= ((((N3**(3/2))*pA3)+((N4**(3/2))*A4)+((N5**(3/2))*pA5))/pt)**(2/3)
                Rh= areat/pt
                Dh=areat/t
            elif Yn > H3 and Yn <= H2: #Yn es mayor a la altura 3 y menor o igual a la altura 2
                area1=((Yn**2)*math.tan(teta2))/2
                area2= A4*H3
                area3=(A4 + A5 + A6)*(Yn - H3)
                area4=(H3*A5)/2
                area5=(((Yn-H3)**2)*math.tan(teta4))/2
                areat= area1+area2+area3+area4+area5
                t= Yn*math.tan(teta2) + A4 + A5 + A6 + (Yn-H3)/math.cos(teta4)
                pA3=Yn/math.cos(teta2)
                pA5=H3/math.cos(teta3)
                pA7=(Yn-H3)/math.cos(teta4)
                pt=pA3+A4+pA5+pA7+A6
                Nequivalente= ((((N3**(3/2))*pA3)+((N4**(3/2))*A4)+((N5**(3/2))*pA5)+((N6**(3/2))*A6)+((N7**(3/2))*pA7))/pt)**(2/3)
                Rh=areat/pt
                Dh=areat/t
            elif Yn > H2: #Yn es mayor a la altura 2
                area1=(((Yn-H2)**2)*math.tan(teta1))/2
                area2=(A2+A3+A4+A5+A6)*(Yn-H2)
                area3=(((Yn-H3)**2)*math.tan(teta4))/2
                area4=(A5+A6)*(Yn-H3)
                area5=A4*H2
                area6=(A3*H2)/2
                area7=(A6*H3)/2
                areat= area1 + area2 + area3 + area4 * area5 + area6 + area7
                t=(Yn-H2)*math.tan(teta1) + A2 + A3 + A4 + A5 + A6 + (Yn-H3)*math.tan(teta4)
                pA1=(Yn-H2)/math.cos(teta1)
                pA3=H2/math.cos(teta2)
                pA5=H3/math.cos(teta3)
                pA7=(Yn-H3)/math.cos(teta4)
                pt=pA1 + A2 + pA3 + A4 + pA5 + A6 + pA7
                Nequivalente= ((((N1**(3/2))*pA1)+((N2**(3/2))*A2)+((N3**(3/2))*pA3)+((N4**(3/2))*A4)+((N5**(3/2))*pA5) + ((N6**(3/2))*A6) + ((N7**(3/2))*A7))/pt)**(2/3)
                Rh=areat/pt                  ###################ARRIBA ES POR A7 O pA7?????
                Dh=areat/t
            elif H1+H2 > H3+H4 and Yn> H1+H2: #Si Una altura total de un lado del canal es mayor a la del otro lado, ocurrira desbordamiento
                print("Desbordamiento del agua en el canal")
                
        caudal_calculado = (areat/Nequivalente) * (Scanal**(1/2)) * (Rh**(2/3))
        Qdelta = Qcanal - caudal_calculado
        if abs(Qdelta) <= 0.001:
            break
        Ydelta = 0.01 * Qdelta
        Yn += Ydelta      # Y nuevo= Yanterior + Ydelta
    Y_Normal = Yn
    
    
 ######----- Para hallar Yc (Y critico)
    Yc = 1   #Yc asumido= 1
    for i2 in range(0, 1000): 
        if H3>=H2: #CASO_1: La altura 3 es mayor o igual a la altura 2.
            if Yc<=H2:   #Yc esta por debajo o igual a la altura 2
                areac1=((Yc**2)*math.tan(teta2))/2
                areac2=A4*Yc
                areac3=((Yc**2)*math.tan(teta3))/2
                areact=areac1+areac2+areac3
                tc=Yc*math.tan(teta2)+A4+Yc*math.tan(teta3)
                pA3=Yc/math.cos(teta2)
                pA5=Yc/math.cos(teta3)
                ptc=pA3+A4+pA5
                Rhc=areact/ptc
                Dhc=areact/tc
            elif Yc>H2 and Yc<=H3: #Yc es mayor a la altura 2 y menor o igual a la altura 3
                areac1=((Yc-H2)**2)*math.tan(teta1)
                areac2=(A2+A3+A4)*(Yc-H2)
                areac3=((Yc**2)*math.tan(teta3))/2
                areac4=(A3*H2)/2
                areac5=A4*H2
                areact= areac1 + areac2 + areac3 + areac4 + areac5
                tc=(Yc-H2)*math.tan(teta1)+A2+A3+A4+Yc*math.tan(teta3)
                pA1=(Yc-H2)/math.cos(teta1)
                pA3=H2/math.cos(teta2)
                pA5=Yc/math.cos(teta3)
                ptc=pA1+A2+pA3+A3+pA5   ###################            
                Rhc=areact/ptc
                Dhc=areact/tc
            elif Yc>H3: #Yc es mayor a la altura 3
                areac1 = (((Yc-H2)**(2))*math.tan(teta1))/2
                areac2 = (A2+A3+A4+A5+A6)*(Yc-H3)
                areac3 = (A2+A3+A4+H2*math.tan(teta3))*(H3-H2)
                areac4=((Yc-H3)*A7)/2
                areac5= (A3*H2)/2
                areac6=A4*H2
                areac7= ((H2**(2))*(math.tan(teta3)))/2
                areac8= (((H3-H2)**(2))*math.tan(teta3))/2
                areact = areac1 + areac2 + areac3 + areac4 + areac5 + areac6+ areac7+areac8
                tc = (Yc-H2) * math.tan(teta1) + A2 + A3 + A4 + A5 + A6 + (Yc-H3)*math.tan(teta4)
                pA1 = (Yc - H2) / math.cos(teta1)
                pA3 = H2 / math.cos(teta2)
                pA5 = H3 / math.cos(teta3)
                pA7 = (Yc - H3) / math.cos(teta4)
                ptc = pA1 + A2 + pA3 + A4 + pA5 + A6 + pA7
                Rhc = areact/ptc
                Dhc = areact/tc
                
        if H3 < H2:  #CASO_2: La altura 3 es menor a la altura 2.
            if Yc <= H3:    #Yc esta por debajo o igual a la altura 3
                areac1=((Yc**2)*math.tan(teta2))/2
                areac2= A4*Yc
                areac3=((Yc**2)*math.tan(teta3))/2
                areact= areac1+areac2+areac3
                tc=Yc*math.tan(teta2) + A4 + Yc*math.tan(teta3)
                pA3=Yc/math.cos(teta2)
                pA5= Yc/math.cos(teta3)
                ptc= pA3 + A4 + pA5           
                Rhc= areact/ptc
                Dhc=areact/tc
            elif Yc > H3 and Yc <= H2:  #Yc es mayor a la altura 3 y menor o igual a la altura 2
                areac1=((Yc**2)*math.tan(teta2))/2
                areac2= A4*H3
                areac3=(A4 + A5 + A6)*(Yc - H3)
                areac4=(H3*A5)/2
                areac5=(((Yc-H3)**2)*math.tan(teta4))/2
                areact= areac1+areac2+areac3+areac4+areac5
                tc= Yc*math.tan(teta2) + A4 + A5 + A6 + (Yc-H3)/math.cos(teta4)
                pA3=Yc/math.cos(teta2)
                pA5=H3/math.cos(teta3)
                pA7=(Yc-H3)/math.cos(teta4)
                ptc=pA3+A4+pA5+pA7+A6
                Rhc=areact/ptc
                Dhc=areact/tc
            elif Yc > H2:  #Yc es mayor a la altura 2
                areac1=(((Yc-H2)**2)*math.tan(teta1))/2
                areac2=(A2+A3+A4+A5+A6)*(Yc-H2)
                areac3=(((Yc-H3)**2)*math.tan(teta4))/2
                areac4=(A5+A6)*(Yc-H3)
                areac5=A4*H2
                areac6=(A3*H2)/2
                areac7=(A6*H3)/2
                areact= areac1 + areac2 + areac3 + areac4 * areac5 + areac6 + areac7
                tc=(Yc-H2)*math.tan(teta1) + A2 + A3 + A4 + A5 + A6 + (Yc-H3)*math.tan(teta4)
                pA1=(Yc-H2)/math.cos(teta1)
                pA3=H2/math.cos(teta2)
                pA5=H3/math.cos(teta3)
                pA7=(Yc-H3)/math.cos(teta4)
                ptc=pA1 + A2 + pA3 + A4 + pA5 + A6 + pA7            
                Rhc=areact/ptc
                Dhc=areact/tc
            
        Fr_calculado = (Qcanal)/((areact)*(9.81*Dhc)**(1/2)) # Para encontrar el Ycritico Fr debe de ser igual a 1
        Frdelta =  1 - Fr_calculado 
        if abs(Frdelta) <= 0.001:
            break
        Ycdelta = 0.01 * Frdelta
        Yc -= Ycdelta
    Y_Critico = Yc
    
    print("\nCANAL TRAPEZOIDAL \n-- Realizado por Andres, Oscar y Sara --\n",
          '\nPara el canal Y Normal (m) es : ',"{:.3f}".format(Y_Normal),
          '\nPara el canal Y Critico (m) es: ',"{:.3f}".format(Y_Critico),
          '\nEl N equivalente es : ',"{:.3f}".format(Nequivalente),
          '\nEl Area mojada (m^2) es : ',"{:.3f}".format(areat),
          '\nEl Espejo de Agua (m) es : ',"{:.3f}".format(t),
          '\nEl Perimetro mojado (m) es : ',"{:.3f}".format(pt),
          '\nEl Radio hidraulico (m) es : ',"{:.3f}".format(Rh),
          '\nEl Diametro hidraulico (m) es : ',"{:.3f}".format(Dh),)
    
    #####-----#####----####
    W1=Y_Normal
    W2=Y_Critico
    W3=Nequivalente
    W4=areat
    W5=t
    W6=pt
    W7=Rh
    W8=Dh
    import tkinter #####PARA MEJOR VISUALIZACIÓN SE CREA UNA VENTANA EMERGENTE CON RESULTADOS
    ventana = tkinter.Tk()
    ventana.geometry("700x100")
    def embed():
        toplevel = tkinter.Toplevel(ventana)
        text = tkinter.Text(toplevel)
        text.pack(fill=tkinter.BOTH, expand=True)
        text.insert(tkinter.END, "\nCANAL TRAPEZOIDAL \n-- Realizado por Andres, Oscar y Sara --\n")
        text.insert(tkinter.END, '\nPara el canal Y Normal (m) es : ')
        text.insert(tkinter.END, W1)
        text.insert(tkinter.END, '\nPara el canal Y Critico (m) es: ')
        text.insert(tkinter.END, W2)
        text.insert(tkinter.END, '\nEl N equivalente es : ')
        text.insert(tkinter.END, W3)
        text.insert(tkinter.END, '\nEl Area mojada (m^2) es : ')
        text.insert(tkinter.END, W4)
        text.insert(tkinter.END, '\nEl Espejo de Agua (m) es : ')
        text.insert(tkinter.END, W5)
        text.insert(tkinter.END, '\nEl Perimetro mojado (m) es : ')
        text.insert(tkinter.END, W6)
        text.insert(tkinter.END, '\nEl Radio hidraulico (m) es : ')
        text.insert(tkinter.END, W7)
        text.insert(tkinter.END, '\nEl Diametro hidraulico (m) es : ')
        text.insert(tkinter.END, W8)
    boton = tkinter.Button(ventana, text="CLICK PARA VER RESULTADOS",command=embed)
    boton.pack()
    #ventana.mainloop() #SE CIERRA LA VENTANA EMERGENTE CON RESULTADOS
    
    #####-----#####----####
    # Dibujo del canal con turtle
    Tamaño_turtle=1.4 #Canal se ve grande= 0.5 y si se ve pequeño 2 o 3 (1 significa normal)
    h1d=H1*Tamaño_turtle
    h2d=H2*Tamaño_turtle
    h3d=H3*Tamaño_turtle
    h4d=H4*Tamaño_turtle
    a1d=A1*Tamaño_turtle
    a2d=A2*Tamaño_turtle
    a3d=A3*Tamaño_turtle
    a4d=A4*Tamaño_turtle
    a5d=A5*Tamaño_turtle
    a6d=A6*Tamaño_turtle
    a7d=A7*Tamaño_turtle
    t1=(a1d+a2d+a3d+a4d+a5d+a6d+a7d)*0.2
    Yd=Y_Normal*Tamaño_turtle
    
    turtle.shape("turtle")
    
    turtle.setup(2000, 300, 0, 0)
    turtle.screensize(200, 150)
    turtle.setworldcoordinates(-20, -20, 449, 188)
    turtle.title("Dibujo del Canal")
    turtle.pencolor("blue")
    turtle.penup()
    turtle.goto(300, 50)
    turtle.pendown()
    turtle.goto(300, 50)
    turtle.goto(300,50)
    turtle.write("Dibujo del canal trapezoidal (seccion transversal)", False,
          "right", ("arial", 10, "bold italic"))
    turtle.penup()
    turtle.goto(300, 50-15)
    turtle.pendown()
    turtle.goto(300, 50-15 )
    turtle.goto(300,50-15)
    turtle.write("hidraulica de canales", False,
          "right", ("arial", 10, "bold italic"))
    turtle.penup()
    turtle.goto(-300, 50-30)
    turtle.pendown()
    turtle.goto(300, 50-30)
    turtle.goto(300,50-30)
    turtle.write("Sara, Oscar, Andres", False,
          "right", ("arial", 10, "bold italic"))
    turtle.fillcolor("black")
    turtle.begin_fill()
    turtle.pencolor("black")
    turtle.penup()
    turtle.goto(0, 0)
    turtle.pendown()
    turtle.goto(0, 0)
    turtle.pensize(3)
    turtle.goto(0, h1d+h2d )
    turtle.goto(t1, h1d+h2d)
    turtle.goto(a1d+t1, h2d)
    turtle.goto(t1+a1d+a2d, h2d)
    turtle.goto(t1+a1d+a2d+a3d, 0)
    turtle.goto(t1+a1d+a2d+a3d+a4d, 0)
    turtle.goto(t1+a1d+a2d+a3d+a4d+a5d,h3d)
    turtle.goto(t1+a1d+a2d+a3d+a4d+a5d+a6d,h3d)
    turtle.goto(t1+a1d+a2d+a3d+a4d+a5d+a6d+a7d,h3d+h4d)
    turtle.goto(t1+t1+a1d+a2d+a3d+a4d+a5d+a6d+a7d,h3d+h4d)
    turtle.goto(t1+t1+a1d+a2d+a3d+a4d+a5d+a6d+a7d,0) #hfinal
    turtle.goto(0,0)
    turtle.end_fill()
    turtle.penup()
    turtle.goto((t1+t1+a1d+a2d+a3d+a4d+a5d+a6d+a7d)/2,0)
    turtle.pendown()
    turtle.goto((t1+t1+a1d+a2d+a3d+a4d+a5d+a6d+a7d)/2,0)
    turtle.pensize(1)
    turtle.pencolor("blue")
    turtle.goto((t1+t1+a1d+a2d+a3d+a4d+a5d+a6d+a7d)/2,Yd)
    turtle.penup()
    turtle.goto(t1,Yd)
    turtle.pendown()
    turtle.goto(t1,Yd)
    turtle.forward(a1d+a2d+a3d+a4d+a5d+a6d+a7d)
    turtle.write("Nivel del flujo de agua (Y normal)")
    #turtle.hideturtle() #para que no se vea la tortuga en la imagen final
    

##### ---// Para REALIZAR LAS GRAFICAS DE  # Es (Energia especifica) y Fr (Froude) # utilizando Y (altura)
    from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
    from matplotlib.figure import Figure
    #------------------------------CREAR VENTANA---------------------------------
    root = tkinter.Tk()
    root.wm_title("Grafica insertada en Tkinter")
    
    q1=50  #La energia especifica se calcula en 4 diferentes caudales
    q2=90
    q3=100
    q4=200
    
    
    if H1 + H2 >= H3+H4:
        ymax= H3 + H4
    else:
        ymax= H1 + H2
    step=0.1   ### PASO
    Y=0.5 ##Altura inicial en las graficas Fr y Es Ejemplo:0.5 
    Y_list = []
    area_list = []
    perimetro_list = []
    Rh_list = []
    Dh_list = []
    t_list = []
    n_list = []
    fr_list = []
    es_list = []
    e1_list = []
    e2_list = []
    e3_list = []
    e4_list = []
    with open ('1_tabla_graficas.txt', 'w') as file:
        file.write("    Area            T             P            Rh          Dh            n             Fr           Es\n")
        for i in range (1,100001):
            if H3>=H2:
                if Y<=H2:
                    area1=((Y**2)*math.tan(teta2))/2
                    area2=A4*Y
                    area3=((Y**2)*math.tan(teta3))/2
                    areat=area1+area2+area3
                    t=Y*math.tan(teta2)+A4+Y*math.tan(teta3)  
                    pA3=Y/math.cos(teta2)
                    pA5=Y/math.cos(teta3)
                    pt=pA3+A4+pA5
                    Nequivalente=((((N3**(3/2))*pA3)+((N4**(3/2))*A4)+((N5**(3/2))*pA5))/pt)**(2/3)
                    Rh=areat/pt
                    Dh=areat/t
                    fr = (Qcanal)/((areat)*(9.81*Dh)**(1/2))
                    Es = (Qcanal**(2))/(2*9.81*areat**(2)) + Y
                    E1 = (q1**(2))/(2*9.81*areat**(2)) + Y
                    E2 = (q2**(2))/(2*9.81*areat**(2)) + Y
                    E3 = (q3**(2))/(2*9.81*areat**(2)) + Y
                    E4 = (q4**(2))/(2*9.81*areat**(2)) + Y
                elif Y>H2 and Y<=H3:
                    area1=((Y-H2)**2)*math.tan(teta1)
                    area2=(A2+A3+A4)*(Y-H2)
                    area3=((Y**2)*math.tan(teta3))/2
                    area4=(A3*H2)/2
                    area5=A4*H2
                    areat= area1 + area2 + area3 + area4 + area5
                    t=(Y-H2)*math.tan(teta1)+A2+A3+A4+Y*math.tan(teta3)
                    pA1=(Y-H2)/math.cos(teta1)
                    pA3=H2/math.cos(teta2)
                    pA5=Y/math.cos(teta3)
                    pt=pA1+A2+pA3+A3+pA5  
                    Nequivalente=((((N1**(3/2))*pA1)+((N2**(3/2))*A2)+((N3**(3/2))*pA3)+((N4**(3/2))*A4)+((N5**(3/2))*pA5))/pt)**(2/3)
                    Rh=areat/pt
                    Dh=areat/t
                    fr = (Qcanal)/((areat)*(9.81*Dh)**(1/2))
                    Es = (Qcanal**(2))/(2*9.81*areat**(2)) + Y
                    E1 = (q1**(2))/(2*9.81*areat**(2)) + Y
                    E2 = (q2**(2))/(2*9.81*areat**(2)) + Y
                    E3 = (q3**(2))/(2*9.81*areat**(2)) + Y
                    E4 = (q4**(2))/(2*9.81*areat**(2)) + Y
                elif Y>H3:
                    area1 = (((Y-H2)**(2))*math.tan(teta1))/2
                    area2 = (A2+A3+A4+A5+A6)*(Y-H3)
                    area3 = (A2+A3+A4+H2*math.tan(teta3))*(H3-H2)
                    area4=((Y-H3)*A7)/2
                    area5= (A3*H2)/2
                    area6=A4*H2
                    area7= ((H2**(2))*(math.tan(teta3)))/2
                    area8= (((H3-H2)**(2))*math.tan(teta3))/2
                    areat = area1 + area2 + area3 + area4 + area5 + area6+ area7+area8
                    t = (Y-H2) * math.tan(teta1) + A2 + A3 + A4 + A5 + A6 + (Y-H3)*math.tan(teta4)
                    pA1 = (Y - H2) / math.cos(teta1)
                    pA3 = H2 / math.cos(teta2)
                    pA5 = H3 / math.cos(teta3)
                    pA7 = (Y - H3) / math.cos(teta4)
                    pt = pA1 + A2 + A3 + A4 + pA5 + A6 + pA7
                    Nequivalente= ((((N1**(3/2))*pA1)+((N2**(3/2))*A2)+((N3**(3/2))*pA3)+((N4**(3/2))*A4)+((N5**(3/2))*pA5) + ((N6**(3/2))*A6) + ((N7**(3/2))*A7))/pt)**(2/3)
                    Rh = areat/pt
                    Dh = areat/t
                    fr = (Qcanal)/((areat)*(9.81*Dh)**(1/2))
                    Es = (Qcanal**(2))/(2*9.81*areat**(2)) + Y
                    E1 = (q1**(2))/(2*9.81*areat**(2)) + Y
                    E2 = (q2**(2))/(2*9.81*areat**(2)) + Y
                    E3 = (q3**(2))/(2*9.81*areat**(2)) + Y
                    E4 = (q4**(2))/(2*9.81*areat**(2)) + Y
                    
            if H3 < H2:
                if Y <= H3:
                    area1=((Y**2)*math.tan(teta2))/2
                    area2= A4*Y
                    area3=((Y**2)*math.tan(teta3))/2
                    areat= area1+area2+area3
                    t=Y*math.tan(teta2) + A4 + Y*math.tan(teta3)
                    pA3=Y/math.cos(teta2)
                    pA5= Y/math.cos(teta3)
                    pt= pA3 + A4 + pA5
                    Nequivalente= ((((N3**(3/2))*pA3)+((N4**(3/2))*A4)+((N5**(3/2))*pA5))/pt)**(2/3)
                    Rh= areat/pt
                    Dh=areat/t
                    fr = (Qcanal)/((areat)*(9.81*Dh)**(1/2))
                    Es = (Qcanal**(2))/(2*9.81*areat**(2)) + Y
                    E1 = (q1**(2))/(2*9.81*areat**(2)) + Y
                    E2 = (q2**(2))/(2*9.81*areat**(2)) + Y
                    E3 = (q3**(2))/(2*9.81*areat**(2)) + Y
                    E4 = (q4**(2))/(2*9.81*areat**(2)) + Y
                elif Y > H3 and Y <= H2:
                    area1=((Y**2)*math.tan(teta2))/2
                    area2= A4*H3
                    area3=(A4 + A5 + A6)*(Y - H3)
                    area4=(H3*A5)/2
                    area5=(((Y-H3)**2)*math.tan(teta4))/2
                    areat= area1+area2+area3+area4+area5
                    t= Y*math.tan(teta2) + A4 + A5 + A6 + (Y-H3)/math.cos(teta4)
                    pA3=Y/math.cos(teta2)
                    pA5=H3/math.cos(teta3)
                    pA7=(Y-H3)/math.cos(teta4)
                    pt=pA3+A4+pA5+pA7+A6
                    Nequivalente= ((((N3**(3/2))*pA3)+((N4**(3/2))*A4)+((N5**(3/2))*pA5)+((N6**(3/2))*A6)+((N7**(3/2))*pA7))/pt)**(2/3)
                    Rh=areat/pt
                    Dh=areat/t
                    fr = (Qcanal)/((areat)*(9.81*Dh)**(1/2))
                    Es = (Qcanal**(2))/(2*9.81*areat**(2)) + Y
                    E1 = (q1**(2))/(2*9.81*areat**(2)) + Y
                    E2 = (q2**(2))/(2*9.81*areat**(2)) + Y
                    E3 = (q3**(2))/(2*9.81*areat**(2)) + Y
                    E4 = (q4**(2))/(2*9.81*areat**(2)) + Y
                elif Y > H2:
                    area1=(((Y-H2)**2)*math.tan(teta1))/2
                    area2=(A2+A3+A4+A5+A6)*(Y-H2)
                    area3=(((Y-H3)**2)*math.tan(teta4))/2
                    area4=(A5+A6)*(Y-H3)
                    area5=A4*H2
                    area6=(A3*H2)/2
                    area7=(A6*H3)/2
                    areat= area1 + area2 + area3 + area4 * area5 + area6 + area7
                    t=(Y-H2)*math.tan(teta1) + A2 + A3 + A4 + A5 + A6 + (Y-H3)*math.tan(teta4)
                    pA1=(Y-H2)/math.cos(teta1)
                    pA3=H2/math.cos(teta2)
                    pA5=H3/math.cos(teta3)
                    pA7=(Y-H3)/math.cos(teta4)
                    pt=pA1 + A2 + pA3 + A4 + pA5 + A6 + pA7
                    Nequivalente= ((((N1**(3/2))*pA1)+((N2**(3/2))*A2)+((N3**(3/2))*pA3)+((N4**(3/2))*A4)+((N5**(3/2))*pA5) + ((N6**(3/2))*A6) + ((N7**(3/2))*A7))/pt)**(2/3)
                    Rh=areat/pt                  
                    Dh=areat/t
                    fr = (Qcanal)/((areat)*(9.81*Dh)**(1/2))
                    Es = (Qcanal**(2))/(2*9.81*areat**(2)) + Y
                    E1 = (q1**(2))/(2*9.81*areat**(2)) + Y
                    E2 = (q2**(2))/(2*9.81*areat**(2)) + Y
                    E3 = (q3**(2))/(2*9.81*areat**(2)) + Y
                    E4 = (q4**(2))/(2*9.81*areat**(2)) + Y
            if Y>=ymax:
                break
            Y_list.append(Y)
            area_list.append(areat)
            perimetro_list.append(pt)
            Rh_list.append(Rh)
            Dh_list.append(Dh)
            t_list.append(t)
            n_list.append(Nequivalente)
            fr_list.append(fr)
            es_list.append(Es)
            e1_list.append(E1)
            e2_list.append(E2)
            e3_list.append(E3)
            e4_list.append(E4)
            Y += step
            file.write('%12.7f %12.7f %12.7f %12.7f %12.7f %12.7f %12.7f %12.7f\n' % (areat, t, pt, Rh, Dh, Nequivalente, fr, Es))
    
    data = {'Y':Y_list,'Area':area_list,'Perimetro':perimetro_list, 'n equiv':n_list, 'Rh':Rh_list, 'Dh':Dh_list,'E':es_list,'Fr':fr_list,}
    data_df = pd.DataFrame(data)
    print()
    print('GRAFICAS Y TABLA CON VALORES')
    print()
    print(data_df)
    
    FROUDE=plt.figure() 
    plt.plot(fr_list,Y_list)
    plt.title('Froude(Fr) vs Altura(Y)')
    plt.xlabel("Fr")
    plt.ylabel("Y")
    #plt.show() #Muestra grafica en consola y no en thinker
    #PARA CREAR FROUDE EN THINKTER
    canvas = FigureCanvasTkAgg(FROUDE, master=root)  # CREAR AREA DE DIBUJO DE TKINTER.
    canvas.draw()
    canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)
    
    ENERGIA=plt.figure() 
    plt.plot(es_list,Y_list)
    plt.plot(e1_list,Y_list)
    plt.plot(e2_list,Y_list)
    plt.plot(e3_list,Y_list)
    plt.plot(e4_list,Y_list)
    plt.title('Energía específica(Es) vs Altura(Y) a diferentes caudales')
    plt.xlabel('Es')
    plt.ylabel('Y')
    plt.legend(('Es','50', '90', '100','200'))
    #plt.show() #Muestra grafica en consola y no en thinker
    #PARA CREAR ENERGIA EN THINKTER
    canvas1 = FigureCanvasTkAgg(ENERGIA, master=root)  # CREAR AREA DE DIBUJO DE TKINTER.
    canvas1.draw()
    canvas1.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)
    
    turtle.exitonclick() ##exit a turtle
    turtle.bye() #cerrar turtle
    ventana.mainloop() #SE CIERRA LA VENTANA EMERGENTE CON RESULTADOS
    #tkinter.mainloop() #CERRAR THINKER DE GRAFICA FROUDE
    #tkinter.mainloop() #CERRAR THINKER DE GRAFICA ENERGIA
    root.mainloop() #cerrar thinker que grafica
 
    
#------------------------///------FIN CÁLCULOS NÚMERICOS---------
#INICIO DE INTERFAZ GRAFICA DE USUARIO PARA MEJOR VISUALIZACIÓN  
interfaz=Tk() #Nombre de la interfaz
interfaz.title("CÁLCULO DE CANAL TRAPEZOIDAL")
interfaz.resizable(1,1)
interfaz.config(bg="black")
miframe=Frame()
miframe.pack()
miframe.config(bg="darkslategray")
miframe.config(width="1350" , height="550") #Tamaño del recuadro base de la interfaz
miframe.config(bd=10)
miframe.config(relief="raised")
miframe.config(cursor="arrow")
mimage=PhotoImage(file="1_canal_trapezoidal.png") #Ingresar la imagen llamada:
image= Label(miframe, image=mimage)
image.place(x=230,y=31)

ubicacioN41=DoubleVar() #ingrese valores
hh111=Label(miframe,text="INGRESE VALORES")
hh111.place(x=0, y=0, width=201, height=25)
hh111.config(bg="cyan2")

ubicacioN41=DoubleVar() #Grafico del canal
hh222=Label(miframe,text="GRÁFICO DEL CANAL")
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
Scc.place(x=0, y=490, width=800, height=31)

interfaz.mainloop()  #Fin de la interfaz grafica










