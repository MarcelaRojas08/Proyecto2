from tkinter import *
from tkinter.ttk import *
from tkinter import ttk
from PIL import ImageTk, Image
import tkinter
from tkinter import messagebox

"""
Funcionalidad: crea la ventana principal, se define el tamaño, el título
               el ícono y la imagen de fondo
"""

ventana = Tk()#ventana principal
ventana.geometry("600x300")#tamaño de la ventana
ventana.title("Sistema de reservación de boletos")#titulo de la ventana
ventana.iconbitmap("python.ico")#ícono de la ventana

#imagen de fondo de la ventana
imagen = ImageTk.PhotoImage(Image.open(r"e1323c623d127b87e800b4701f5d3224.gif").resize((600,300)))
label = Label(image=imagen)
label.pack()

#---------------------------------------------------------------------------------------------------------------------------------
"""
Nombre: ventanaPrincipal
Funcionalidad: crea la barra del menú principal en la ventana principal
"""
def ventanaPrincipal():
    menu = Menu(ventana)
    ventana.config(menu=menu)
    menuPrincipal = Menu(menu,tearoff = 0)#quita la linea de puntos
    #opciones del menú principal, fuente, tamaño, inclinación y espesor
    menuPrincipal.add_command(label = "1 - Opciones administrativas",font =("Times new roman","12","italic","bold"),command = clave)
    menuPrincipal.add_command(label = "2 - Opciones de usuario normal",font =("Times new roman","12","italic","bold"),command = menuGeneral)
    menuPrincipal.add_command(label = "3 - Salir",font =("Times new roman","12","italic","bold"),command = ventana.destroy)

    menu.add_cascade(label="Menú principal", menu = menuPrincipal)#diseño del menú principal

    
def menuAdministrativo():
    abrirVentana = Tk()
    abrirVentana.geometry("600x300")
    abrirVentana.title("Menú administrativo")
    abrirVentana.config(bg = "skyblue")
    abrirVentana.iconbitmap("python.ico")

    menu = Menu(abrirVentana)
    abrirVentana.config(menu=menu)

    opAdmi = Menu(menu,tearoff = 0)
    opAdmi.add_command(label = "1 - Gestión de empresas",font=("Times new roman","12"),command = gestionEmpresa)
    opAdmi.add_command(label = "2 - Gestión de transporte por empresa",font=("Times new roman","12"),command = gestionTransporte)
    opAdmi.add_command(label = "3 - Gestión de viaje",font=("Times new roman","12"), command = gestionViaje)
    opAdmi.add_command(label = "4 - Consultar historial de reservaciones",font=("Times new roman","12"), command = consultaHistorial)
    opAdmi.add_command(label = "5 - Estadísticas de viaje",font=("Times new roman","12"), command = estadisticas)
    opAdmi.add_command(label = "6 - Salir de menu administrativo", font=("Times new roman","12"),command = ventanaPrincipal)
    menu.add_cascade(label="1 - Opciones administrativas", font=("Times new roman","12"), menu = opAdmi)
    

    
def clave():
    ventana.destroy()
    ventanaClave = Tk()
    ventanaClave.geometry("600x300")
    ventanaClave.title("Clave de acceso")
    ventanaClave.config(bg = "skyblue")
    ventanaClave.iconbitmap("python.ico")
    entrada= tkinter.StringVar()

    etiqueta=tkinter.Label(ventanaClave,text="Escriba la clave de acceso",bg = "white",font =("Times new roman","14","italic","bold"))
    etiqueta.place(x=180,y=60)
    
    entrada = tkinter.Entry(ventanaClave, textvariable = entrada)
    entrada.place(x=225,y=90)
    boton = tkinter.Button(ventanaClave,text = "Ingresar",font=("Times new roman","12"),
                      command = lambda: verificar(entrada.get(),ventanaClave))
    boton.place(x=260,y=120)

def verificar(entrada,ventanaClave):
    Acceso = leerArchivo()
    if (entrada in Acceso):
        return menuAdministrativo()
    else:
        messagebox.showerror("Error","La contraseña es incorrecta")

def leerArchivo():
    Archivo = open("clave de acceso.txt")
    Lineas = Archivo.readlines()
    Archivo.close()
    editLines = []
    for linea in Lineas:
        linea = linea.replace("\n","")
        editLines += [linea]
    return editLines

    
def gestionEmpresa():
    ventana2 = Tk()
    ventana2.geometry("250x200")
    ventana2.title("Menú administrativo")
    ventana2.config(bg = "Turquoise")
    ventana2.iconbitmap("python.ico")

    menu1 = Menu(ventana2)
    op2 = Menu(menu1,tearoff = 0)
    op2.add_command(label = "1 - Incluir empresa",font=("Times new roman","12"),command = IncluirEmpresa)
    op2.add_command(label = "2 - Eliminar empresa",font=("Times new roman","12"),command = eliminarEmpresa)
    op2.add_command(label = "3 - Modificar empresa",font=("Times new roman","12"),command = modificarEmpresa)
    op2.add_command(label = "4 - Mostrar empresas",font=("Times new roman","12"),command = mostrarEmpresas)
    op2.add_command(label = "5 - Retornar",font=("Times new roman","12"),command = menuAdministrativo)
    menu1.add_cascade(label=" Gestión de empresa",font=("Times new roman","12"), menu = op2)
    ventana2.config(menu=menu1)
    ventana2.mainloop()


def IncluirEmpresa():
    ventanaIncluirEmpresa = tkinter.Tk()
    ventanaIncluirEmpresa.geometry("600x300")
    ventanaIncluirEmpresa.title("Incluir empresa")
    ventanaIncluirEmpresa.config(bg = "Turquoise")
    ventanaIncluirEmpresa.iconbitmap("python.ico")
    

    etiquetaCedula = tkinter.Label(ventanaIncluirEmpresa,text="Dígite el número de cédula jurídica:",
                                    font=("Times new roman","12")).place(x=10,y=20)
    Cedula = tkinter.Entry(ventanaIncluirEmpresa,text="",font=("Times new roman","12"))
    Cedula.place(x=280,y=20)

    etiquetaNombre = tkinter.Label(ventanaIncluirEmpresa,text="Escriba el nombre de la empresa:",
                                    font=("Times new roman","12")).place(x=10,y=60)
    Nombre = tkinter.Entry(ventanaIncluirEmpresa,text="",font=("Times new roman","12"))
    Nombre.place(x=280,y=60)

    etiquetaDireccion = tkinter.Label(ventanaIncluirEmpresa,text="Escriba la direccion de la empresa:",
                                        font=("Times new roman","12")).place(x=10,y=100)
    Direccion = tkinter.Entry(ventanaIncluirEmpresa,text="",font=("Times new roman","12"))
    Direccion.place(x=280,y=100)

    etiquetaProvincia = tkinter.Label(ventanaIncluirEmpresa,text="Escriba la provincia de la empresa:",
                                        font=("Times new roman","12")).place(x=10,y=140)
    Provincia = tkinter.Entry(ventanaIncluirEmpresa,text="",font=("Times new roman","12"))
    Provincia.place(x=280,y=140)

    etiquetaSeñas = tkinter.Label(ventanaIncluirEmpresa,text="Escriba las señas exactas de la empresa:",
                                      font=("Times new roman","12")).place(x=10,y=180)
    Señas = tkinter.Entry(ventanaIncluirEmpresa,text="",font=("Times new roman","12"))
    Señas.place(x=280,y=180)

    def agregarAux():
        return agregarEmpresa(Cedula.get(),Nombre.get(),Direccion.get(),Provincia.get(),Señas.get())

    boton = tkinter.Button(ventanaIncluirEmpresa,text = "Agregar empresa",font=("Times new roman","12"),
                    command= agregarAux)
    boton.place(x=200,y=230)
    
    ventanaIncluirEmpresa.mainloop()

def agregarEmpresa(Cedula,Nombre,Direccion,Provincia,Señas):
    Archivo = open("Información de la empresa.txt","a")
    if len(Cedula) == 10:
        Archivo2 = open("Información de la empresa.txt")
        Comprobar = Archivo2.readlines()
        if("Cédula júridica:"+Cedula+"\n") in Comprobar:
            answer = messagebox.showerror("Error", "La cedula juridica ya existe")
        else:
            Archivo.write("Cédula júridica:"+Cedula+"\n")
            Archivo.write("Nombre de la empresa:"+Nombre+"\n")
            Archivo.write("Direccion de la empresa:"+Direccion+"\n")
            Archivo.write("Provincia de la empresa:"+Provincia+"\n")
            Archivo.write("Señas exactas de la empresa:"+Señas+"\n")
            Archivo.write(".............................................."+"\n")
            Archivo.close()
            answer1 = messagebox.showinfo(title = "Agregar Empresa",message = "La empresa ha sido agregada")
    else:
        answer2 = messagebox.showerror("Error", "La cedula juridica debe tener 10 digitos")

    
#---------------------------------------------------------------------------------------------------------------------------------
def eliminarEmpresa():
    ventanaEliminarEmpresa = Tk()
    ventanaEliminarEmpresa.geometry("500x400")
    ventanaEliminarEmpresa.title("Eliminar empresa")
    ventanaEliminarEmpresa.config(bg = "Turquoise")
    ventanaEliminarEmpresa.iconbitmap("python.ico")

    etiquetaEliminar = tkinter.Label(ventanaEliminarEmpresa,text="Dígite el número de cédula jurídica:",
                                        font=("Times new roman","12")).place(x=10,y=20)
    Cedula = tkinter.Entry(ventanaEliminarEmpresa,text="",font=("Times new roman","12"))
    Cedula.place(x=300,y=20)

    boton = tkinter.Button(ventanaEliminarEmpresa, text = "Eliminar empresa",font=("Times new roman","12"),
                        command= eliminarEmpresa_aux).place(x=200,y=200)

def eliminarEmpresa_aux():
    Almacen = open("Información de la empresa.txt")
    Borrar = Almacen.readlines()
    if("Cédula júridica:"+Cedula.get()+ "\n")in Borrar:
        ContarLineas = Borrar.index("Cédula júridica:"+Cedula.get()+ "\n")
        Almacen2 = open("Información del transporte.txt")
        Linea = Almacen2.readlines()
        if("Empresa del transporte:"+Borrar[ContarLineas+1][21:])in Linea:
                    answer = messagebox.showerror("Error", "La empresa esta asociada a un transporte")
        else:
            BorrarLineas = EliminarEmpresa_aux(Borrar,ContarLineas,0)
            Almacen.close()
            Abrir = open("Información de la empresa.txt","w")
            Abrir.write(BorrarLineas)
            Abrir.close()
            answer1 = messagebox.showinfo("Eliminar empresa","La empresa ha sido eliminada")
    else:
        answer2 = messagebox.showerror("Error", "La empresa no existe")

def EliminarEmpresa_aux(Borrar,ContarLineas,contador):
    if contador == 6:
        return TransformarString(Borrar)
    else:
        print(Borrar[ContarLineas].rstrip())
        Borrar.pop(ContarLineas)
        return EliminarEmpresa_aux(Borrar,ContarLineas,contador+1)

def TransformarString(Borrar):
    if isinstance(Borrar,list):
        string = ""
        for linea in Borrar:
            string += linea
            return string
        else:
            print("")

    
    ventanaEliminarEmpresa.mainloop()
#-------------------------------------------------------------------------------------------------------------------------------
def modificarEmpresa():
    ventanaModificarEmpresa = Tk()
    ventanaModificarEmpresa.geometry("600x300")
    ventanaModificarEmpresa.title("Modificar empresa")
    ventanaModificarEmpresa.config(bg = "Turquoise")
    ventanaModificarEmpresa.iconbitmap("python.ico")

    etiquetaCedula = tkinter.Label(ventanaModificarEmpresa,text="Dígite el número de cédula jurídica:",
                                    font=("Times new roman","12")).place(x=180,y=60)
    Cedula = tkinter.Entry(ventanaModificarEmpresa,text = "",font=("Times new roman","12"))
    Cedula.place(x=210,y=90)

    boton = tkinter.Button(ventanaModificarEmpresa,text = "Modificar empresa",font=("Times new roman","12"),
                           command = lambda:Modificar_aux(Cedula.get()))
    boton.place(x=225,y=120)

def Modificar_aux(Cedula):
    Archivo = open("Información de la empresa.txt")
    Leer = Archivo.readlines()
    if("Cédula júridica:"+Cedula+ "\n") in Leer:
        Cedula = str(Cedula)
        Indice = Leer.index("Cédula júridica:"+Cedula+ "\n")
        Modificar2(Leer,Indice+1,1)
        Archivo.close()
    else:
        answer2 = messagebox.showerror("Error", "La empresa no existe")

        
def Modificar2(leer,indice,contador):
    Modificar = Tk()
    Modificar.geometry("500x300")
    Modificar.title("Modificar empresa")
    Modificar.config(bg = "Turquoise")
    Modificar.iconbitmap("python.ico")

    etiqueta = tkinter.Label(Modificar,text="Escriba el nombre de la empresa:",font=("Times new roman","12"))
    etiqueta.place(x=10,y=20)
    entry=tkinter.Entry(Modificar)
    entry.place(x=270,y=20)

    etiqueta2=tkinter.Label(Modificar,text="Escriba la direccion de la empresa:",font=("Times new roman","12"))
    etiqueta2.place(x=10,y=60)
    entry2=tkinter.Entry(Modificar)
    entry2.place(x=270,y=60)

    etiqueta3=tkinter.Label(Modificar,text="Escriba la provincia de la empresa:",font=("Times new roman","12"))
    etiqueta3.place(x=10,y=100)
    entry3=tkinter.Entry(Modificar)
    entry3.place(x=270,y=100)

    etiqueta4=tkinter.Label(Modificar,text="Escriba las señas exactas de la empresa:",font=("Times new roman","12"))
    etiqueta4.place(x=10,y=140)
    entry4=tkinter.Entry(Modificar)
    entry4.place(x=270,y=140)

    def modificar_aux():
        Nombre= entry.get()
        Direccion = entry2.get()
        Provincia= entry3.get()
        Señas = entry4.get()
        print(Nombre,Direccion,Provincia,Señas)
        return Modificar3(Nombre,Direccion,Provincia,Señas,leer,indice)

    boton=tkinter.Button(Modificar,text="Modificar",command= modificar_aux)
    boton.place(x=200,y=200)

def Modificar3(Nombre,Direccion,Provincia,Señas,leer,indice):
    Abrir = open("Información de la empresa.txt","w")
    leer[indice]=("Nombre de la empresa:"+Nombre+"\n")
    leer[indice+1]=("Direccion de la empresa:"+Direccion+"\n")
    leer[indice+2]=("Provincia de la empresa:"+Provincia+"\n")
    leer[indice+3]=("Señas exactas de la empresa:"+Señas+"\n")
    print(leer)
    Abrir.write(TransformarString_aux(leer))
    answer = messagebox.showinfo("Modificar empresa", "La empresa se ha modificado")

def TransformarString_aux(dato):
    if isinstance(dato,list):
        string = ""
        for linea in dato:
            string += linea
        return string
    else:
        print("")
#-----------------------------------------------------------------------------------------------------------------------------
def mostrarEmpresas():
    ventanaMostrarEmpresa = Tk()
    ventanaMostrarEmpresa.geometry("500x400")
    ventanaMostrarEmpresa.title("Mostrar empresas")
    ventanaMostrarEmpresa.iconbitmap("python.ico")
    Archivo = open("Información de la empresa.txt")
    Abrir = Archivo.readlines()
    Mostrar = tkinter.Listbox(ventanaMostrarEmpresa)
    Mostrar.pack(fill=X,expand=YES)
    contador = 0
    for informacion in Abrir:
        Mostrar.insert(contador,informacion)
        contador += 1
    boton = tkinter.Button(ventanaMostrarEmpresa,text = "Mostrar empresas",font=("Times new roman","12"))
    boton.pack()

#-----------------------------------------------------------------------------------------------------------------------------        

                
def gestionTransporte():
    ventana3 = Tk()
    ventana3.geometry("250x200")
    ventana3.title("Menú administrativo")
    ventana3.config(bg = "Turquoise")
    ventana3.iconbitmap("python.ico")

    menu2 = Menu(ventana3)
    op2 = Menu(menu2,tearoff = 0)
    op2.add_command(label = "1 - Incluir transporte",font=("Times new roman","12"),command =IncluirTransporte)
    op2.add_command(label = "2 - Eliminar transporte",font=("Times new roman","12"),command = eliminarTransporte)
    op2.add_command(label = "3 - Modificar transporte",font=("Times new roman","12"),command = modificarTransporte)
    op2.add_command(label = "4 - Mostrar transportes",font=("Times new roman","12"),command = mostrarTransportes)
    op2.add_command(label = "5 - Retornar",font=("Times new roman","12"),command = menuAdministrativo)
    menu2.add_cascade(label=" Gestión de transporte por empresa",font=("Times new roman","12"), menu = op2)
    ventana3.config(menu=menu2)
    ventana3.mainloop()
   
#------------------------------------------------------------------------------------------------------------------------------
def IncluirTransporte():
    ventanaIncluirTransporte = Tk()
    ventanaIncluirTransporte.geometry("600x500")
    ventanaIncluirTransporte.title("Incluir transporte")
    ventanaIncluirTransporte.config(bg = "Turquoise")
    ventanaIncluirTransporte.iconbitmap("python.ico")
    Placa = tkinter.StringVar()
    Tipo = tkinter.StringVar()
    Marca = tkinter.StringVar()
    Modelo = tkinter.StringVar()
    Año = tkinter.StringVar()
    Empresa = tkinter.StringVar()
    AsientosVIP = tkinter.StringVar()
    AsientosNor = tkinter.StringVar()
    AsientosEco = tkinter.StringVar()

    etiquetaPlaca = tkinter.Label(ventanaIncluirTransporte,text="Escriba la placa del transporte:",
                                    font=("Times new roman","12")).place(x=10,y=20)
    Placa = tkinter.Entry(ventanaIncluirTransporte,textvariable = Placa,font=("Times new roman","12"))
    Placa.place(x=270,y=20)

    etiquetaTipo = tkinter.Label(ventanaIncluirTransporte,text="Tipo de transporte Buseta - Limosina:",
                                    font=("Times new roman","12")).place(x=10,y=60)
    Tipo = tkinter.Entry(ventanaIncluirTransporte,textvariable = Tipo,font=("Times new roman","12"))
    Tipo.place(x=270,y=60)

    etiquetaMarca = tkinter.Label(ventanaIncluirTransporte,text="Escriba la marca del transporte:",
                                      font=("Times new roman","12")).place(x=10,y=100)
    Marca = tkinter.Entry(ventanaIncluirTransporte,textvariable = Marca,font=("Times new roman","12"))
    Marca.place(x=270,y=100)

    etiquetaModelo = tkinter.Label(ventanaIncluirTransporte,text="Escriba el modelo del transporte:",
                                    font=("Times new roman","12")).place(x=10,y=140)
    Modelo = tkinter.Entry(ventanaIncluirTransporte,textvariable = Modelo,font=("Times new roman","12"))
    Modelo.place(x=270,y=140)

    etiquetaAño = tkinter.Label(ventanaIncluirTransporte,text="Escriba el año del transporte:",
                                font=("Times new roman","12")).place(x=10,y=180)
    Año = tkinter.Entry(ventanaIncluirTransporte,textvariable = Año,font=("Times new roman","12"))
    Año.place(x=270,y=180)

    etiquetaEmpresa = tkinter.Label(ventanaIncluirTransporte,text="Escriba el nombre de la empresa:",
                                    font=("Times new roman","12")).place(x=10,y=220)
    Empresa = tkinter.Entry(ventanaIncluirTransporte,textvariable = Empresa,font=("Times new roman","12"))
    Empresa.place(x=270,y=220)

    etiquetaVIP = tkinter.Label(ventanaIncluirTransporte,text="Cantidad de asientos clase VIP:",
                                font=("Times new roman","12")).place(x=10,y=260)
    AsientosVIP = tkinter.Entry(ventanaIncluirTransporte,textvariable = AsientosVIP,font=("Times new roman","12"))
    AsientosVIP.place(x=270,y=260)

    etiquetaNor = tkinter.Label(ventanaIncluirTransporte,text="Cantidad de asientos clase normal:",
                                font=("Times new roman","12")).place(x=10,y=300)
    AsientosNor = tkinter.Entry(ventanaIncluirTransporte,textvariable = AsientosNor,font=("Times new roman","12"))
    AsientosNor.place(x=270,y=300)

    etiquetaEco = tkinter.Label(ventanaIncluirTransporte,text="Cantidad de asientos clase económica:",
                                font=("Times new roman","12")).place(x=10,y=340)
    AsientosEco = tkinter.Entry(ventanaIncluirTransporte,textvariable = AsientosEco,font=("Times new roman","12"))
    AsientosEco.place(x=270,y=340)

    boton = tkinter.Button(ventanaIncluirTransporte, text = "Agregar transporte",font=("Times new roman","12"),
                               command= lambda:agregarTransporte(Placa.get(),Tipo.get(),Marca.get(),Modelo.get(),Año.get(),Empresa.get(),
                                                                 AsientosVIP.get(),AsientosNor.get(),AsientosEco.get())).place(x=200,y=380)
    

def agregarTransporte(Placa,Tipo,Marca,Modelo,Año,Empresa,AsientosVIP,AsientosNor,AsientosEco):
    Archivo = open("Información del transporte.txt","a")
    Archivo2 = open("Información del transporte.txt")
    Comprobar = Archivo2.readlines()
    if ("Placa del transporte:"+Placa+"\n") in Comprobar:
        answer = messagebox.showerror("Error", "La placa ya existe")
    else:
        Archivo.write("Placa del transporte:"+Placa+"\n")
        Archivo.write("Tipo de transporte:"+Tipo+"\n")
        Archivo.write("Marca del transporte:"+Marca+"\n")
        Archivo.write("Modelo del transporte:"+Modelo+"\n")
        Archivo.write("Año del transporte:"+Año+"\n")
        Archivo.write("Empresa del transporte:"+Empresa+"\n")
        Archivo.write("Cantidad de asientos clase VIP:"+AsientosVIP+"\n")
        Archivo.write("Cantidad de asientos clase normal:"+AsientosNor+"\n")
        Archivo.write("Cantidad de asientos clase económica:"+AsientosEco+"\n")
        Archivo.write("......................................"+"\n")
        messagebox.showinfo(title = "Agregar Transporte",message = "El transporte ha sido agregado")

    ventanaIncluirTransporte.mainloop()
        
#----------------------------------------------------------------------------------------------------------------------------
def eliminarTransporte():
    ventanaEliminarTransporte = Tk()
    ventanaEliminarTransporte.geometry("500x400")
    ventanaEliminarTransporte.title("Eliminar transporte")
    ventanaEliminarTransporte.config(bg = "Turquoise")
    ventanaEliminarTransporte.iconbitmap("python.ico")
    etiquetaEliminar = tkinter.Label(ventanaEliminarTransporte ,text="Escriba la placa del transporte:",
                                            font=("Times new roman","12")).place(x=10,y=20)
    Placa = tkinter.Entry(ventanaEliminarTransporte,text="",font=("Times new roman","12"))
    Placa.place(x=300,y=20)

    boton = tkinter.Button(ventanaEliminarTransporte, text = "Eliminar transporte",font=("Times new roman","12"),
                        command= eliminarTransporte_aux).place(x=200,y=200)

def eliminarTransporte_aux():
    Almacen = open("Información del transporte.txt")
    Borrar = Almacen.readlines()
    if("Placa del transporte:"+Placa.get()+"\n")in Borrar:
        ContarLineas = Borrar.index("Placa del transporte:"+Placa.get()+"\n")
        Almacen2 = open("Información por viaje.txt")
        Linea = Almacen2.readlines()
        if("Placa del transporte:"+Borrar[ContarLineas][21:])in Linea:
            answer = messagebox.showerror("Error", "El transporte esta asociado a un viaje")
        else:
            BorrarLineas = EliminarTransporte_aux(Borrar,ContarLineas,0)
            Almacen.close()
            Abrir = open("Información del transporte.txt","w")
            Abrir.write(BorrarLineas)
            Abrir.close()
            answer = messagebox.showinfo("Eliminar transporte","El transporte ha sido eliminado")
    else:
        answer = messagebox.showerror("Error", "El transporte no existe")

def EliminarTransporte_aux(Borrar,ContarLineas,contador):
    if contador == 10:
        return TransformarString(Borrar)
    else:
        print(Borrar[ContarLineas].rstrip())
        Borrar.pop(ContarLineas)
        return EliminarTransporte_aux(Borrar,ContarLineas,contador+1)

def TransformarString(Borrar):
    if isinstance(Borrar,list):
        string = ""
        for linea in Borrar:
            string += linea
            return string
        else:
            print("")


    ventanaEliminarTransporte.mainloop()
#-----------------------------------------------------------------------------------------------------------------------------

def modificarTransporte():
    ventanaModificarTransporte = Tk()
    ventanaModificarTransporte.geometry("500x300")
    ventanaModificarTransporte.title("Modificar empresa")
    ventanaModificarTransporte.config(bg = "Turquoise")
    ventanaModificarTransporte.iconbitmap("python.ico")

    etiquetaPlaca = tkinter.Label(ventanaModificarTransporte,text="Escriba la placa del transporte:",
                                    font=("Times new roman","12")).place(x=140,y=60)
    Placa = tkinter.Entry(ventanaModificarTransporte,text = "",font=("Times new roman","12"))
    Placa.place(x=155,y=90)

    boton = tkinter.Button(ventanaModificarTransporte,text = "Modificar transporte",font=("Times new roman","12"),
                           command = lambda:ModificarTrans_aux(Placa.get()))
    boton.place(x=170,y=120)

def ModificarTrans_aux(Placa):
    Archivo = open("Información del transporte.txt")
    Leer = Archivo.readlines()
    if("Placa del transporte:"+Placa+ "\n") in Leer:
        Placa = str(Placa)
        Indice = Leer.index("Placa del transporte:"+Placa+ "\n")
        ModificarTrans2(Leer,Indice+1,1)
        Archivo.close()
    else:
        answer2 = messagebox.showerror("Error", "El transporte no existe")

        
def ModificarTrans2(leer,indice,contador):
    ModificarT = Tk()
    ModificarT.geometry("600x400")
    ModificarT.title("Modificar transporte")
    ModificarT.config(bg = "Turquoise")
    ModificarT.iconbitmap("python.ico")

    etiqueta = tkinter.Label(ModificarT,text="Tipo de transporte Buseta - Limosina:",font=("Times new roman","12"))
    etiqueta.place(x=10,y=20)
    entry=tkinter.Entry(ModificarT)
    entry.place(x=270,y=20)

    etiqueta2=tkinter.Label(ModificarT,text="Escriba la marca del transporte:",font=("Times new roman","12"))
    etiqueta2.place(x=10,y=60)
    entry2=tkinter.Entry(ModificarT)
    entry2.place(x=270,y=60)

    etiqueta3=tkinter.Label(ModificarT,text="Escriba el modelo del transporte:",font=("Times new roman","12"))
    etiqueta3.place(x=10,y=100)
    entry3=tkinter.Entry(ModificarT)
    entry3.place(x=270,y=100)

    etiqueta4=tkinter.Label(ModificarT,text="Escriba el año del transporte:",font=("Times new roman","12"))
    etiqueta4.place(x=10,y=140)
    entry4=tkinter.Entry(ModificarT)
    entry4.place(x=270,y=140)

    etiqueta5=tkinter.Label(ModificarT,text="Escriba el nombre de la empresa:",font=("Times new roman","12"))
    etiqueta5.place(x=10,y=180)
    entry5=tkinter.Entry(ModificarT)
    entry5.place(x=270,y=180)

    etiqueta6=tkinter.Label(ModificarT,text="Cantidad de asientos clase VIP:",font=("Times new roman","12"))
    etiqueta6.place(x=10,y=220)
    entry6=tkinter.Entry(ModificarT)
    entry6.place(x=270,y=220)

    etiqueta7=tkinter.Label(ModificarT,text="Cantidad de asientos clase normal:",font=("Times new roman","12"))
    etiqueta7.place(x=10,y=260)
    entry7=tkinter.Entry(ModificarT)
    entry7.place(x=270,y=260)

    etiqueta8=tkinter.Label(ModificarT,text="Cantidad de asientos clase economica:",font=("Times new roman","12"))
    etiqueta8.place(x=10,y=300)
    entry8=tkinter.Entry(ModificarT)
    entry8.place(x=270,y=300)

    def modificarTrans_aux():
        Tipo = entry.get()
        Marca = entry2.get()
        Modelo = entry3.get()
        Año = entry4.get()
        Empresa = entry5.get()
        AsientosVIP = entry6.get()
        AsientosNor = entry7.get()
        AsientosEco = entry8.get()
        return ModificarT3(Tipo,Marca,Modelo,Año,Empresa,AsientosVIP,AsientosNor,AsientosEco,leer,indice)

    boton=tkinter.Button(ModificarT,text="Modificar",command= modificarTrans_aux)
    boton.place(x=200,y=350)

def ModificarT3(Tipo,Marca,Modelo,Año,Empresa,AsientosVIP,AsientosNor,AsientosEco,leer,indice):
    Abrir = open("Información del transporte.txt","w")
    leer[indice]=("Tipo de transporte:"+Tipo+"\n")
    leer[indice+1]=("Marca del transporte:"+Marca+"\n")
    leer[indice+2]=("Modelo del transporte:"+Modelo+"\n")
    leer[indice+3]=("Año del transporte:"+Año+"\n")
    leer[indice+4]=("Empresa del transporte:"+Empresa+"\n")
    leer[indice+5]=("Cantidad de asientos clase VIP:"+AsientosVIP+"\n")
    leer[indice+6]=("Cantidad de asientos clase normal:"+AsientosNor+"\n")
    leer[indice+7]=("Cantidad de asientos clase económica:"+AsientosEco+"\n")
    Abrir.write(TransformarString_aux(leer))
    answer = messagebox.showinfo("Modificar transporte", "El transporte ha modificado")




#--------------------------------------------------------------------------------------------------------------------------
def mostrarTransportes():
    ventanaMostrarTransporte = Tk()
    ventanaMostrarTransporte.geometry("500x400")
    ventanaMostrarTransporte.title("Mostrar transportes")
    ventanaMostrarTransporte.iconbitmap("python.ico")
    Archivo = open("Información del transporte.txt")
    Abrir = Archivo.readlines()
    Mostrar = tkinter.Listbox(ventanaMostrarTransporte)
    Mostrar.pack(fill=X,expand=YES)
    contador = 0
    for informacion in Abrir:
        Mostrar.insert(contador,informacion)
        contador += 1
    boton = tkinter.Button(ventanaMostrarTransporte,text = "Mostrar empresas",font=("Times new roman","12"))
    boton.pack()
        

#----------------------------------------------------------------------------------------------------------------------------
def gestionViaje():
    ventana4 = Tk()
    ventana4.geometry("250x200")
    ventana4.title("Menú administrativo")
    ventana4.config(bg = "Turquoise")
    ventana4.iconbitmap("python.ico")

    menu3 = Menu(ventana4)
    op3 = Menu(menu3,tearoff = 0)
    op3.add_command(label = "1 - Incluir viaje",font=("Times new roman","12"),command = IncluirViaje)
    op3.add_command(label = "2 - Eliminar viaje",font=("Times new roman","12"),command = eliminarViaje)
    op3.add_command(label = "3 - Modificar viaje",font=("Times new roman","12"),command = modificarViaje)
    op3.add_command(label = "4 - Mostrar viajes",font=("Times new roman","12"),command = mostrarViajes)
    op3.add_command(label = "5 - Retornar",font=("Times new roman","12"),command = menuAdministrativo)
    menu3.add_cascade(label=" Gestión de viaje",font=("Times new roman","12"), menu = op3)
    ventana4.config(menu=menu3)
    ventana4.mainloop()

def IncluirViaje():
    ventanaIncluirViaje = Tk()
    ventanaIncluirViaje.geometry("600x600")
    ventanaIncluirViaje.title("Incluir viaje")
    ventanaIncluirViaje.config(bg = "Turquoise")
    ventanaIncluirViaje.iconbitmap("python.ico")
    
    ProvinciaSalida = tkinter.StringVar()
    CiudadSalida = tkinter.StringVar()
    FechaSalida = tkinter.StringVar()
    HoraSalida = tkinter.StringVar()
    ProvinciaLlegada = tkinter.StringVar()
    CiudadLlegada = tkinter.StringVar()
    FechaLlegada = tkinter.StringVar()
    HoraLlegada = tkinter.StringVar()
    Empresa = tkinter.StringVar()
    Transporte = tkinter.StringVar()
    MontoVIP = tkinter.StringVar()
    MontoNor = tkinter.StringVar()
    MontoEco = tkinter.StringVar()

    etiquetaPS = tkinter.Label(ventanaIncluirViaje,text="Escriba la provincia de salida:",
                                    font=("Times new roman","12")).place(x=10,y=20)
    ProvinciaSalida = tkinter.Entry(ventanaIncluirViaje,textvariable = ProvinciaSalida,font=("Times new roman","12"))
    ProvinciaSalida.place(x=270,y=20)

    etiquetaCS = tkinter.Label(ventanaIncluirViaje,text="Escriba la ciudad de salida:",
                                    font=("Times new roman","12")).place(x=10,y=60)
    CiudadSalida = tkinter.Entry(ventanaIncluirViaje,textvariable = CiudadSalida,font=("Times new roman","12"))
    CiudadSalida.place(x=270,y=60)

    etiquetaFS = tkinter.Label(ventanaIncluirViaje,text="Escriba la fecha de salida:",
                                    font=("Times new roman","12")).place(x=10,y=100)
    FechaSalida = tkinter.Entry(ventanaIncluirViaje,textvariable = FechaSalida,font=("Times new roman","12"))
    FechaSalida.place(x=270,y=100)

    etiquetaHS = tkinter.Label(ventanaIncluirViaje,text="Escriba la hora de salida:",
                                    font=("Times new roman","12")).place(x=10,y=140)
    HoraSalida = tkinter.Entry(ventanaIncluirViaje,textvariable = HoraSalida,font=("Times new roman","12"))
    HoraSalida.place(x=270,y=140)

    etiquetaPLl = tkinter.Label(ventanaIncluirViaje,text="Escriba la provincia de llegada:",
                                font=("Times new roman","12")).place(x=10,y=180)
    ProvinciaLlegada = tkinter.Entry(ventanaIncluirViaje,textvariable = ProvinciaLlegada,font=("Times new roman","12"))
    ProvinciaLlegada.place(x=270,y=180)

    etiquetaCLl = tkinter.Label(ventanaIncluirViaje,text="Escriba la ciudad de llegada:",
                                    font=("Times new roman","12")).place(x=10,y=220)
    CiudadLlegada = tkinter.Entry(ventanaIncluirViaje,textvariable = CiudadLlegada,font=("Times new roman","12"))
    CiudadLlegada.place(x=270,y=220)

    etiquetaFLl = tkinter.Label(ventanaIncluirViaje,text="Escriba la fecha de llegada:",
                                    font=("Times new roman","12")).place(x=10,y=260)
    FechaLlegada = tkinter.Entry(ventanaIncluirViaje,textvariable = FechaLlegada,font=("Times new roman","12"))
    FechaLlegada.place(x=270,y=260)

    etiquetaHLl = tkinter.Label(ventanaIncluirViaje,text="Escriba la hora de llegada:",
                                    font=("Times new roman","12")).place(x=10,y=300)
    HoraLlegada = tkinter.Entry(ventanaIncluirViaje,textvariable = HoraLlegada,font=("Times new roman","12"))
    HoraLlegada.place(x=270,y=300)

    etiquetaEmpresa = tkinter.Label(ventanaIncluirViaje,text="Escriba el nombre de la empresa:",
                                    font=("Times new roman","12")).place(x=10,y=340)
    Empresa = tkinter.Entry(ventanaIncluirViaje,textvariable = Empresa,font=("Times new roman","12"))
    Empresa.place(x=270,y=340)

    etiquetaTransporte = tkinter.Label(ventanaIncluirViaje,text="Escriba la placa del transporte:",
                                    font=("Times new roman","12")).place(x=10,y=380)
    Transporte = tkinter.Entry(ventanaIncluirViaje,textvariable = Transporte,font=("Times new roman","12"))
    Transporte.place(x=270,y=380)

    etiquetaMVIP = tkinter.Label(ventanaIncluirViaje,text="Monto de asiento VIP:",
                                font=("Times new roman","12")).place(x=10,y=420)
    MontoVIP = tkinter.Entry(ventanaIncluirViaje,textvariable = MontoVIP,font=("Times new roman","12"))
    MontoVIP.place(x=270,y=420)

    etiquetaMNor = tkinter.Label(ventanaIncluirViaje,text="Monto de asiento normal:",
                                    font=("Times new roman","12")).place(x=10,y=460)
    MontoNor = tkinter.Entry(ventanaIncluirViaje,textvariable = MontoNor,font=("Times new roman","12"))
    MontoNor.place(x=270,y=460)

    etiquetaMEco = tkinter.Label(ventanaIncluirViaje,text="Monto de asiento económico:",
                                font=("Times new roman","12")).place(x=10,y=500)
    MontoEco = tkinter.Entry(ventanaIncluirViaje,textvariable = MontoEco,font=("Times new roman","12"))
    MontoEco.place(x=270,y=500)

    boton = tkinter.Button(ventanaIncluirViaje, text = "Agregar viaje",font=("Times new roman","12"),
                    command= lambda:agregarViaje(ProvinciaSalida.get(),CiudadSalida.get(),FechaSalida.get(),HoraSalida.get(),
                                                ProvinciaLlegada.get(),CiudadLlegada.get(),FechaLlegada.get(),HoraLlegada.get(),Empresa.get(),
                                                Transporte.get(),MontoVIP.get(),MontoNor.get(),MontoEco.get())).place(x=200,y=550)

def agregarViaje(ProvinciaSalida,CiudadSalida,FechaSalida,HoraSalida,ProvinciaLlegada,CiudadLlegada,
                 FechaLlegada,HoraLlegada,Empresa,Transporte,MontoVIP,MontoNor,MontoEco):
    Archivo = "Información por viaje.txt"
    Archivo2 = open(Archivo,"a")
    Archivo3 = open(Archivo)
    Archivo3 = Archivo3.readlines()
    NumeroViaje = numeroAutomatico()
    Archivo.write("Número de viaje:"+str(NumeroViaje)+"\n")
    Archivo.write("Provincia de salida:"+ProvinciaSalida+"\n")
    Archivo.write("Ciudad de salida:"+CiudadSalida+"\n")
    Archivo.write("Fecha de salida:"+FechaSalida+"\n")
    Archivo.write("Hora de salida:"+HoraSalida+"\n")
    Archivo.write("Provincia de llegada:"+ProvinciaLlegada+"\n")
    Archivo.write("Ciudad de llegada:"+CiudadLlegada+"\n")
    Archivo.write("Fecha de llegada:"+FechaLlegada+"\n")
    Archivo.write("Hora de llegada:"+HoraLlegada+"\n")
    Archivo.write("Nombre de la empresa:"+Empresa+"\n")
    Archivo.write("Placa del transporte:"+Transporte+"\n")
    Archivo.write("Monto de asiento clase VIP:"+MontoVIP+"\n")
    Archivo.write("Monto de asiento clase normal:"+MontoNor+"\n")
    Archivo.write("Monto de asiento clase económica:"+MontoEco+"\n")
    Archivo.write("......................................"+"\n")
    messagebox.showinfo(title = "Agregar Viaje",message = "El viaje ha sido agregado")

def numeroAutomatico():
    Archivo = "Información por viaje.txt"
    Crear = open (Archivo,'a')
    Agenda = open (Archivo,'r')
    contador = 0
    for linea in Agenda:
        contador += 1
    Agenda.close()
    return str(contador//15+1)

    boton = tkinter.Button(ventanaIncluirViaje, text = "Agregar viaje",font=("Times new roman","12"),
                    command= lambda:agregarViaje(ProvinciaSalida.get(),CiudadSalida.get(),FechaSalida.get(),HoraSalida.get(),
                                                ProvinciaLlegada.get(),CiudadLlegada.get(),FechaLlegada.get(),HoraLlegada.get(),Empresa.get(),
                                                Transporte.get(),MontoVIP.get(),MontoNor.get(),MontoEco.get())).place(x=200,y=550)
    ventanaIncluirViaje.mainloop()


def eliminarViaje():
    ventanaEliminarViaje = Tk()
    ventanaEliminarViaje.geometry("500x400")
    ventanaEliminarViaje.title("Eliminar transporte")
    ventanaEliminarViaje.config(bg = "Turquoise")
    ventanaEliminarViaje.iconbitmap("python.ico")

    etiquetaEliminar = tkinter.Label(ventanaEliminarViaje,text="Escriba el numero del viaje:",
                                            font=("Times new roman","12")).place(x=10,y=20)
    NumeroViaje = tkinter.Entry(ventanaEliminarViaje,text="",font=("Times new roman","12"))
    NumeroViaje.place(x=300,y=20)

    boton = tkinter.Button(ventanaEliminarViaje, text = "Eliminar viaje",font=("Times new roman","12"),
                        command= eliminarViaje_aux).place(x=200,y=200)

def eliminarViaje_aux():
    Almacen = open("Información por viaje.txt")
    Borrar = Almacen.readlines()
    if("Número de viaje:"+NumeroViaje.get()+ "\n")in Borrar:
        ContarLineas = Borrar.index("Número de viaje:"+NumeroViaje.get()+ "\n")
        BorrarLineas = EliminarViaje_aux(Borrar,ContarLineas,0)
        Almacen.close()
        Abrir = open("Información por viaje.txt","w")
        Abrir.write(BorrarLineas)
        Abrir.close()
        messagebox.showinfo("Eliminar viaje","El viaje ha sido eliminado")
    else:
        messagebox.showerror("Error","El viaje no existe")

def EliminarViaje_aux(Borrar,ContarLineas,contador):
    if contador == 15:
        return TransformarString(Borrar)
    else:
        print(Borrar[ContarLineas].rstrip())
        Borrar.pop(ContarLineas)
        return EliminarViaje_aux(Borrar,ContarLineas,contador+1)

        
    ventanaEliminarViaje.mainloop()


#------------------------------------------------------------------------------------------------------------------------
def modificarViaje():
    ventanaModificarViaje = Tk()
    ventanaModificarViaje.geometry("500x400")
    ventanaModificarViaje.title("Modificar viaje")
    ventanaModificarViaje.config(bg = "Turquoise")
    ventanaModificarViaje.iconbitmap("python.ico")

    etiquetaNumero = tkinter.Label(ventanaModificarViaje,text="Escriba el número del viaje:",
                                    font=("Times new roman","12")).pack()
    NumeroViaje = tkinter.Entry(ventanaModificarViaje,text = "",font=("Times new roman","12"))
    NumeroViaje.pack()

    boton = tkinter.Button(ventanaModificarViaje,text = "Modificar viaje",font=("Times new roman","12"),
                           command = lambda:ModificarViaje_aux(NumeroViaje.get()))
    boton.pack()

def ModificarViaje_aux(NumeroViaje):
    Archivo = open("Información por viaje.txt")
    Leer = Archivo.readlines()
    if("Número de viaje:"+NumeroViaje+ "\n") in Leer:
        Numero = str("Número de viaje:"+NumeroViaje+ "\n")
        Indice = Leer.index("Número de viaje:"+NumeroViaje+ "\n")
        ModificarViaje2(Leer,Indice+1,1)
        Archivo.close()
    else:
        answer2 = messagebox.showerror("Error", "El viaje no existe")

        
def ModificarViaje2(leer,indice,contador):
    ModificarV = Tk()
    ModificarV.geometry("600x600")
    ModificarV.title("Modificar viaje")
    ModificarV.config(bg = "Turquoise")
    ModificarV.iconbitmap("python.ico")

    etiqueta1 = tkinter.Label(ModificarV,text="Escriba la provincia de salida:",font=("Times new roman","12"))
    etiqueta1.place(x=10,y=20)
    entry1=tkinter.Entry(ModificarV)
    entry1.place(x=270,y=20)

    etiqueta2=tkinter.Label(ModificarV,text="Escriba la ciudad de salida:",font=("Times new roman","12"))
    etiqueta2.place(x=10,y=60)
    entry2=tkinter.Entry(ModificarV)
    entry2.place(x=270,y=60)

    etiqueta3=tkinter.Label(ModificarV,text="Escriba la fecha de salida:",font=("Times new roman","12"))
    etiqueta3.place(x=10,y=100)
    entry3=tkinter.Entry(ModificarV)
    entry3.place(x=270,y=100)

    etiqueta4=tkinter.Label(ModificarV,text="Escriba la hora de salida:",font=("Times new roman","12"))
    etiqueta4.place(x=10,y=140)
    entry4=tkinter.Entry(ModificarV)
    entry4.place(x=270,y=140)

    etiqueta5=tkinter.Label(ModificarV,text="Escriba la provincia de llegada:",font=("Times new roman","12"))
    etiqueta5.place(x=10,y=180)
    entry5=tkinter.Entry(ModificarV)
    entry5.place(x=270,y=180)

    etiqueta6=tkinter.Label(ModificarV,text="Escriba la ciudad de llegada:",font=("Times new roman","12"))
    etiqueta6.place(x=10,y=220)
    entry6=tkinter.Entry(ModificarV)
    entry6.place(x=270,y=220)

    etiqueta7=tkinter.Label(ModificarV,text="Escriba la fecha de llegada:",font=("Times new roman","12"))
    etiqueta7.place(x=10,y=260)
    entry7=tkinter.Entry(ModificarV)
    entry7.place(x=270,y=260)

    etiqueta8=tkinter.Label(ModificarV,text="Escriba la hora de llegada:",font=("Times new roman","12"))
    etiqueta8.place(x=10,y=300)
    entry8=tkinter.Entry(ModificarV)
    entry8.place(x=270,y=300)

    etiqueta9=tkinter.Label(ModificarV,text="Escriba el nombre de la empresa:",font=("Times new roman","12"))
    etiqueta9.place(x=10,y=340)
    entry9=tkinter.Entry(ModificarV)
    entry9.place(x=270,y=340)

    etiqueta10=tkinter.Label(ModificarV,text="Escriba la placa del transporte:",font=("Times new roman","12"))
    etiqueta10.place(x=10,y=380)
    entry10=tkinter.Entry(ModificarV)
    entry10.place(x=270,y=380)

    etiqueta11=tkinter.Label(ModificarV,text="Monto de asiento clase VIP:",font=("Times new roman","12"))
    etiqueta11.place(x=10,y=420)
    entry11=tkinter.Entry(ModificarV)
    entry11.place(x=270,y=420)

    etiqueta12=tkinter.Label(ModificarV,text="Monto de asiento clase normal:",font=("Times new roman","12"))
    etiqueta12.place(x=10,y=460)
    entry12=tkinter.Entry(ModificarV)
    entry12.place(x=270,y=460)

    etiqueta13=tkinter.Label(ModificarV,text="Monto de asiento clase económica:",font=("Times new roman","12"))
    etiqueta13.place(x=10,y=500)
    entry13=tkinter.Entry(ModificarV)
    entry13.place(x=270,y=500)

    def modificarVi_aux():
        ProvinciaSalida = entry1.get()
        CiudadSalida = entry2.get()
        FechaSalida = entry3.get()
        HoraSalida = entry4.get()
        ProvinciaLlegada = entry5.get()
        CiudadLlegada = entry6.get()
        FechaLlegada = entry7.get()
        HoraLlegada = entry8.get()
        Empresa = entry9.get()
        Transporte = entry10.get()
        MontoVIP = entry11.get()
        MontoNor = entry12.get()
        MontoEco = entry13.get()
        return ModificarV3(ProvinciaSalida,CiudadSalida,FechaSalida,HoraSalida,ProvinciaLlegada,CiudadLlegada,
                           FechaLlegada,HoraLlegada,Empresa,Transporte,MontoVIP,MontoNor,MontoEco,leer,indice)

    boton=tkinter.Button(ModificarV,text="Modificar",command= modificarVi_aux).place(x=200,y=550)

def ModificarV3(ProvinciaSalida,CiudadSalida,FechaSalida,HoraSalida,ProvinciaLlegada,CiudadLlegada,
                FechaLlegada,HoraLlegada,Empresa,Transporte,MontoVIP,MontoNor,MontoEco,leer,indice):
    Abrir = open("Información por viaje.txt","w")
    leer[indice]=("Provincia de salida:"+ProvinciaSalida+"\n")
    leer[indice+1]=("Ciudad de salida:"+CiudadSalida+"\n")
    leer[indice+2]=("Fecha de salida:"+FechaSalida+"\n")
    leer[indice+3]=("Hora de salida:"+HoraSalida+"\n")
    leer[indice+4]=("Provincia de llegada:"+ProvinciaLlegada+"\n")
    leer[indice+5]=("Ciudad de llegada:"+CiudadLlegada+"\n")
    leer[indice+6]=("Fecha de llegada:"+FechaLlegada+"\n")
    leer[indice+7]=("Hora de llegada:"+HoraLlegada+"\n")
    leer[indice+8]=("Nombre de la empresa:"+Empresa+"\n")
    leer[indice+9]=("Placa del transporte:"+Transporte+"\n")
    leer[indice+10]=("Monto de asiento clase VIP:"+MontoVIP+"\n")
    leer[indice+11]=("Monto de asiento clase normal:"+MontoNor+"\n")
    leer[indice+12]=("Monto de asiento clase económica:"+MontoEco+"\n")
    Abrir.write(TransformarString_aux(leer))
    answer = messagebox.showinfo("Modificar viaje", "El viaje ha modificado")


#--------------------------------------------------------------------------------------------------------------------------
def mostrarViajes():
    ventanaMostrarViaje = Tk()
    ventanaMostrarViaje.geometry("500x400")
    ventanaMostrarViaje.title("Mostrar transportes")
    ventanaMostrarViaje.iconbitmap("python.ico")
    Archivo = open("Información por viaje.txt")
    Abrir = Archivo.readlines()
    Mostrar = tkinter.Listbox(ventanaMostrarViaje)
    Mostrar.pack(fill=X,expand=YES)
    contador = 0
    for informacion in Abrir:
        Mostrar.insert(contador,informacion)
        contador += 1
    boton = tkinter.Button(ventanaMostrarViaje,text = "Mostrar empresas",font=("Times new roman","12"))
    boton.pack()
    
    

def consultaHistorial():
    ventana5 = Tk()
    ventana5.geometry("250x200")
    ventana5.title("Menú administrativo")
    ventana5.config(bg = "Turquoise")
    ventana5.iconbitmap("python.ico")
    menu4 = Menu(ventana5)
    op4 = Menu(menu4,tearoff = 0)
    op4.add_command(label = "1 - Rango de fecha de salida",font=("Times new roman","12"))
    op4.add_command(label = "2 - Rango de fecha de llegada",font=("Times new roman","12"))
    op4.add_command(label = "3 - Rango de fecha de la reservacion",font=("Times new roman","12"))
    op4.add_command(label = "4 - Lugar de salida",font=("Times new roman","12"))
    op4.add_command(label = "5 - Lugar de llegada",font=("Times new roman","12"))
    op4.add_command(label = "6 - Salir",font=("Times new roman","12"),command = menuAdministrativo)
    menu4.add_cascade(label=" Consultar historial de reservaciones",font=("Times new roman","12"), menu = op4)
    ventana5.config(menu=menu4)
    ventana5.mainloop()

def estadisticas():
    ventana6 = Tk()
    ventana6.geometry("250x200")
    ventana6.title("Menú administrativo")
    ventana6.config(bg = "Turquoise")
    ventana6.iconbitmap("python.ico")
    menu5 = Menu(ventana6)  
        
    op5 = Menu(menu5,tearoff = 0)
    menu5.add_cascade(label=" Estadísticas de viaje",font=("Times new roman","12"), menu = op5)
    ventana6.config(menu=menu5)
    ventana6.mainloop()
    return menuAdministrativo()

def menuGeneral():
    ventana7 = Tk()
    ventana7.geometry("250x200")
    ventana7.config(bg = "Turquoise")
    ventana7.title("Menu General")
    ventana7.iconbitmap("python.ico")
    
    menu6 = Menu(ventana7)
    ventana7.config(menu=menu6)
    
    op6 = Menu(menu6,tearoff = 0)
    op6.add_command(label = "1 - Consulta de viajes",font=("Times new roman","12"),command = consultaViajes)
    op6.add_command(label = "2 - Reservación de viaje",font=("Times new roman","12"),comman = reservacion)
    op6.add_command(label = "3 - Cancelación de viaje",font=("Times new roman","12"), command = cancelacion)
    op6.add_command(label = "4 - Salir de menú general",font=("Times new roman","12"),command = ventanaPrincipal)
    menu6.add_cascade(label="2 - Opciones de usuario general", font=("Times new roman","12"), menu = op6)

def consultaViajes():
    ventana8 = Tk()
    ventana8.geometry("250x200")
    ventana8.title("Menú general")
    ventana8.config(bg = "Turquoise")
    ventana8.iconbitmap("python.ico")
    menu7 = Menu(ventana8)
    ventana8.config(menu=menu7)   
    op7 = Menu(menu7,tearoff = 0)
    op7.add_command(label = "1 - Empresa",font=("Times new roman","12"))
    op7.add_command(label = "2 - Lugar de salida",font=("Times new roman","12"))
    op7.add_command(label = "3 - Lugar de llegada",font=("Times new roman","12"))
    op7.add_command(label = "4 - Rango de fecha de salida",font=("Times new roman","12"))
    op7.add_command(label = "5 - Rango de fecha de llegada",font=("Times new roman","12"))
    op7.add_command(label = "6 - Salir",font=("Times new roman","12"),command = menuGeneral)
    menu7.add_cascade(label=" Consulta de viajes",font=("Times new roman","12"), menu = op7)
    ventana8.config(menu=menu7)
    ventana8.mainloop()

def reservacion():
    ventana9 = Tk()
    ventana9.geometry("250x200")
    ventana9.title("Menú general")
    ventana9.config(bg = "Turquoise")
    ventana9.iconbitmap("python.ico")
    menu8 = Menu(ventana9)  
        
    op8 = Menu(menu8,tearoff = 0)
        
    ventana9.config(menu=menu8)


    def Reservacion():
        from datetime import datetime 
        Archivo2 = open("Información de reservación.txt","a") 
        Archivo2.close()
        print("\n\t\tInformación de reservación")
        Archivo3 = open("Información por viaje.txt")
        Informacion = Archivo3.read()
        print("\n"+Informacion)
        Abrir = open("Información por viaje.txt")
        Archivo3 = Abrir.readlines()
        Viaje = input("\n\tDígite el número del viaje:")
        Archivo4 = ubicarIndice(Archivo3,"Número de viaje:"+Viaje+"\n",0)
        Empresa = Archivo3[Archivo4+5][21:-1]
        Transporte = Archivo3[Archivo4+6][21:-1]
        LugarSalida = Archivo3[Archivo4+1][17:-1]
        FechaYHoraSalida = Archivo3[Archivo4+2][23:-1]
        LugarLLegada = Archivo3[Archivo4+3][18:-1]
        FechaYHoraLLegada = Archivo3[Archivo4+4][24:-1]
        Nombre = input("\n\tEscriba su nombre:")
        CantidadVIP = input("\n\tCantidad de espacios a reservar VIP:")
        Placa = Archivo3[Archivo4+6][21:-1]
        Archivo5 = open("Información del transporte.txt")
        Archivo5 = Archivo5.readlines()
        Indice = Archivo5.index("Placa del transporte:"+Placa+"\n")
        VIPdisponible = Archivo5[Indice+5][31:-1]
        if int(VIPdisponible) - int(CantidadVIP)>= 0:
            CantidadNormal = input("\n\tCantidad de espacios a reservar normal:")
            NormalDisponible = Archivo5[Indice+6][34:-1]
            if int(NormalDisponible) - int(CantidadNormal)>= 0:
                CantidadEconomico = input("\n\tCantidad de espacios a reservar económicos:")
                EconomicoDisponible = Archivo5[Indice+7][37:-1]
                if int(EconomicoDisponible) - int(CantidadEconomico)>= 0:
                    Monto = int(CantidadVIP)*(int(Archivo3[Archivo4+7][27:-1]))
                    Monto2 = int(CantidadNormal)*(int(Archivo3[Archivo4+8][30:-1]))
                    Monto3 = int(CantidadEconomico)*(int(Archivo3[Archivo4+9][33:-1]))
                    Archivo = "Información de reservación.txt"
                    Archivo2 = open(Archivo)
                    lineas = Archivo2.readlines()
                    Identificador = identificador(lineas,0)
                    FechaHora = datetime.now()
                    Archivo2 = open("Información de reservación.txt","a") 
                    Archivo2.write("Numero del viaje:"+Viaje+"\n")
                    Archivo2.write("Nombre de persona que reserva:"+Nombre+"\n")
                    Archivo2.write("Empresa:"+Empresa+"\n")
                    Archivo2.write("Transporte:"+Transporte+"\n")
                    Archivo2.write("Lugar de salida:"+LugarSalida+"\n")
                    Archivo2.write("Fecha y hora de salida:"+FechaYHoraSalida+"\n")
                    Archivo2.write("Lugar de llegada:"+LugarLLegada+"\n")
                    Archivo2.write("Fecha y hora de llegada:"+FechaYHoraLLegada+"\n")
                    Archivo2.write("Cantidad de espacios VIP reservados:"+CantidadVIP+"\n")
                    Archivo2.write("Cantidad de espacios normales reservados:"+CantidadNormal+"\n")
                    Archivo2.write("Cantidad de espacios economicos reservados:"+CantidadEconomico+"\n")
                    Archivo2.write("Fecha y hora de la reservacion:"+str(FechaHora)+"\n")
                    Archivo2.write("Monto de reservacion:"+str(Monto+Monto2+Monto3)+"\n")
                    Archivo2.write("Identificador:"+str(Identificador)+"\n")
                    Archivo2.write("......................................................."+"\n")
                    Archivo2.close()
                    
        
                def ubicarIndice(listas,buscar,contador):
                    if listas == []:
                        return False
                    elif buscar in listas[0]:
                        return contador
                    else:
                        return ubicarIndice(listas[1:],buscar,contador+1)
                        
                def identificador(lineas,contador):
                    if lineas == []:
                        return contador//14+1
                    else:
                        return identificador(lineas[1:],contador+1)
                    ventana9.mainloop()
        

def cancelacion():
    ventana10 = Tk()
    ventana10.geometry("250x200")
    ventana10.title("Menú general")
    ventana10.config(bg = "Turquoise")
    ventana10.iconbitmap("python.ico")
    menu9 = Menu(ventana10)  
    op9 = Menu(menu9,tearoff = 0)
    ventana10.config(menu=menu9)
    ventana10.mainloop()
    


ventanaPrincipal()
