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

#-------------------------------------------------------------------------------------------------------------------------------    
"""
Nombre:menuAdministrativo
Funcionalidad: crea la ventana que posee la barra de menú administrativo
"""
def menuAdministrativo():
    abrirVentana = Tk()
    abrirVentana.geometry("300x200")
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
    

#-----------------------------------------------------------------------------------------------------------------------------    
"""
Nombre: clave
Funcionalidad: crea la ventana que solicita la clave de acceso al menú administrativo
"""
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
"""
Nombre:leerArchivo
Funcionalidad: abre el archivo de clave de acceso y verifica que la clave se encuentre en el.
"""
def leerArchivo():
    Archivo = open("clave de acceso.txt")
    Lineas = Archivo.readlines()
    Archivo.close()
    editLines = []
    for linea in Lineas:
        linea = linea.replace("\n","")
        editLines += [linea]
    return editLines

#------------------------------------------------------------------------------------------------------------------------------    
"""
Nombre:gestionEmpresa
Funcionalidad: crea la ventana que posee el menú de gestión de empresa
"""
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
#----------------------------------------------------------------------------------------------------------------------------
"""
Nombre:IncluirEmpresa
Entradas: cedula, nombre,direccion, provincia,señas
Funcionalidad: solicita los datos para agregar la empresa
"""
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

"""
Nombre:agregarEmpresa
Entradas: cedula, nombre,direccion, provincia,señas
Funcionalidad: guarda los datos en el archivo de texto
"""
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
"""
Nombre:eliminarEmpresa
Entradas: numero de cedula
Funcionalidad:crea la ventana para eliminar la empresa y solicita el numero de cedula
"""
def eliminarEmpresa():
    ventanaEliminarEmpresa = Tk()
    ventanaEliminarEmpresa.geometry("420x150")
    ventanaEliminarEmpresa.title("Eliminar empresa")
    ventanaEliminarEmpresa.config(bg = "Turquoise")
    ventanaEliminarEmpresa.iconbitmap("python.ico")

    etiquetaEliminar = tkinter.Label(ventanaEliminarEmpresa,text="Dígite el número de cédula jurídica:",
                                        font=("Times new roman","12")).place(x=10,y=20)
    Cedula = tkinter.Entry(ventanaEliminarEmpresa,text="",font=("Times new roman","12"))
    Cedula.place(x=230,y=20)

    def eliminarE():
        return eliminarEmpresa_aux(Cedula.get())

    boton = tkinter.Button(ventanaEliminarEmpresa, text = "Eliminar empresa",font=("Times new roman","12"),
                        command= eliminarE).place(x=230,y=50)

"""
Nombre:eliminarEmpresa_aux
Entradas: Cedula
Funcionalidad: verifica que la cedula se encuentre en el archivo de texto
"""
def eliminarEmpresa_aux(Cedula):
    Almacen = open("Información de la empresa.txt")
    Borrar = Almacen.readlines()
    if("Cédula júridica:"+Cedula+ "\n")in Borrar:
        ContarLineas = Borrar.index("Cédula júridica:"+Cedula+ "\n")
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

"""
Nombre:EliminarEmpresa_aux
Entradas:Borrar,ContarLineas,contador
Funcionalidad: elimina las lineas del archivo de texto
"""
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
"""
Nombre:modificarEmpresa
Entradas: numero de cedula
Funcionalidad: crea la ventana de modificar empresa y solicita el numero de cedula
"""
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
"""
Nombre:Modificar_aux
Entradas: Cedula
Funcionalidad: busca la cedula juridica en el archivo de texto
"""
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

"""
Nombre:Modificar2
Entradas:leer,indice,contador
Funcionalidad: solicita los nuevos datos de la empresa
"""
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

"""
Nombre:Modificar3
Entradas:Nombre,Direccion,Provincia,Señas,leer,indice
Funcionalidad: escribe los nuevos datos en el archivo de texto
"""
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
"""
Nombre:mostrarEmpresas
Funcionalidad: crea la ventana que muestra la lista de las empresas
"""
def mostrarEmpresas():
    ventanaMostrarEmpresa = Tk()
    ventanaMostrarEmpresa.geometry("500x350")
    ventanaMostrarEmpresa.title("Mostrar empresas")
    ventanaMostrarEmpresa.config(bg = "Turquoise")
    ventanaMostrarEmpresa.iconbitmap("python.ico")
    Archivo = open("Información de la empresa.txt")
    Abrir = Archivo.readlines()
    Mostrar = tkinter.Listbox(ventanaMostrarEmpresa,width = 40,height = 15)
    Mostrar.place(x=10,y=20)
    contador = 0
    for informacion in Abrir:
        Mostrar.insert(contador,informacion)
        contador += 1
    boton = tkinter.Button(ventanaMostrarEmpresa,text = "Salir",font=("Times new roman","12"))
    boton.place(x=350,y=150)

#-----------------------------------------------------------------------------------------------------------------------------        
"""
Nombre:gestionTransporte
Funcionalidad: crea la ventana que muestra el menú de gestion de transporte
"""
                
def gestionTransporte():
    ventana3 = Tk()
    ventana3.geometry("250x200")
    ventana3.title("Menú administrativo")
    ventana3.config(bg = "Purple")
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
"""
Nombre:IncluirTransporte
Entradas: placa,tipo,marca,modelo,año,empresa,asientos vip, asientos normales,asientos economicos
Funcionalidad: solicita los datos para agregar el transporte
"""
def IncluirTransporte():
    ventanaIncluirTransporte = Tk()
    ventanaIncluirTransporte.geometry("800x500")
    ventanaIncluirTransporte.title("Incluir transporte")
    ventanaIncluirTransporte.config(bg = "Purple")
    ventanaIncluirTransporte.iconbitmap("python.ico")

    Archivo = open("Información de la empresa.txt")
    Abrir = Archivo.readlines()
    Mostrar = tkinter.Listbox(ventanaIncluirTransporte,width = 40)
    Mostrar.place(x=500,y = 220)
    contador = 0
    for informacion in Abrir:
        Mostrar.insert(contador,informacion)
        contador += 1

    etiquetaPlaca = tkinter.Label(ventanaIncluirTransporte,text="Escriba la placa del transporte:",
                                    font=("Times new roman","12")).place(x=10,y=20)
    Placa = tkinter.Entry(ventanaIncluirTransporte,text = "",font=("Times new roman","12"))
    Placa.place(x=270,y=20)

    etiquetaTipo = tkinter.Label(ventanaIncluirTransporte,text="Tipo de transporte Buseta - Limosina:",
                                    font=("Times new roman","12")).place(x=10,y=60)
    Tipo = tkinter.Entry(ventanaIncluirTransporte,text = "",font=("Times new roman","12"))
    Tipo.place(x=270,y=60)

    etiquetaMarca = tkinter.Label(ventanaIncluirTransporte,text="Escriba la marca del transporte:",
                                      font=("Times new roman","12")).place(x=10,y=100)
    Marca = tkinter.Entry(ventanaIncluirTransporte,text = "",font=("Times new roman","12"))
    Marca.place(x=270,y=100)

    etiquetaModelo = tkinter.Label(ventanaIncluirTransporte,text="Escriba el modelo del transporte:",
                                    font=("Times new roman","12")).place(x=10,y=140)
    Modelo = tkinter.Entry(ventanaIncluirTransporte,text = "",font=("Times new roman","12"))
    Modelo.place(x=270,y=140)

    etiquetaAño = tkinter.Label(ventanaIncluirTransporte,text="Escriba el año del transporte:",
                                font=("Times new roman","12")).place(x=10,y=180)
    Año = tkinter.Entry(ventanaIncluirTransporte,text = "",font=("Times new roman","12"))
    Año.place(x=270,y=180)

    etiquetaEmpresa = tkinter.Label(ventanaIncluirTransporte,text="Escriba el nombre de la empresa:",
                                    font=("Times new roman","12")).place(x=10,y=220)
    Empresa = tkinter.Entry(ventanaIncluirTransporte,text = "",font=("Times new roman","12"))
    Empresa.place(x=270,y=220)

    etiquetaVIP = tkinter.Label(ventanaIncluirTransporte,text="Cantidad de asientos clase VIP:",
                                font=("Times new roman","12")).place(x=10,y=260)
    AsientosVIP = tkinter.Entry(ventanaIncluirTransporte,text = "",font=("Times new roman","12"))
    AsientosVIP.place(x=270,y=260)

    etiquetaNor = tkinter.Label(ventanaIncluirTransporte,text="Cantidad de asientos clase normal:",
                                font=("Times new roman","12")).place(x=10,y=300)
    AsientosNor = tkinter.Entry(ventanaIncluirTransporte,text = "",font=("Times new roman","12"))
    AsientosNor.place(x=270,y=300)

    etiquetaEco = tkinter.Label(ventanaIncluirTransporte,text="Cantidad de asientos clase económica:",
                                font=("Times new roman","12")).place(x=10,y=340)
    AsientosEco = tkinter.Entry(ventanaIncluirTransporte,text = "",font=("Times new roman","12"))
    AsientosEco.place(x=270,y=340)

    def agregarT():
        return agregarTransporte(Placa.get(),Tipo.get(),Marca.get(),Modelo.get(),Año.get(),Empresa.get(),
                 AsientosVIP.get(),AsientosNor.get(),AsientosEco.get())

    boton = tkinter.Button(ventanaIncluirTransporte, text = "Agregar transporte",font=("Times new roman","12"),
                               command= agregarT).place(x=200,y=380)
    
"""
Nombre:agregarTransporte
Entradas: Placa,Tipo,Marca,Modelo,Año,Empresa,AsientosVIP,AsientosNor,AsientosEco
Funcionalidad: guarda los datos en el archivo de texto
"""
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

    
        
#----------------------------------------------------------------------------------------------------------------------------
"""
Nombre:eliminarTransporte
Entradas: placa del transporte
Funcionalidad:crea la ventana para eliminar el trasnporte y solicita la placa del transporte
"""
def eliminarTransporte():
    ventanaEliminarTransporte = Tk()
    ventanaEliminarTransporte.geometry("420x150")
    ventanaEliminarTransporte.title("Eliminar transporte")
    ventanaEliminarTransporte.config(bg = "Purple")
    ventanaEliminarTransporte.iconbitmap("python.ico")

    etiquetaEliminar = tkinter.Label(ventanaEliminarTransporte ,text="Escriba la placa del transporte:",
                                            font=("Times new roman","12")).place(x=10,y=20)
    Placa = tkinter.Entry(ventanaEliminarTransporte,text="",font=("Times new roman","12"))
    Placa.place(x=230,y=20)

    def eliminarT():
        return eliminarTransporte_aux(Placa.get())

    boton = tkinter.Button(ventanaEliminarTransporte, text = "Eliminar transporte",font=("Times new roman","12"),
                        command= eliminarT).place(x=230,y=50)

"""
Nombre:eliminarTransporte_aux
Entradas: Placa
Funcionalidad: verifica que la placa se encuentre en el archivo de texto
"""
def eliminarTransporte_aux(Placa):
    Almacen = open("Información del transporte.txt")
    Borrar = Almacen.readlines()
    if("Placa del transporte:"+Placa+"\n")in Borrar:
        ContarLineas = Borrar.index("Placa del transporte:"+Placa+"\n")
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

"""
Nombre:EliminarTransporte_aux
Entradas:Borrar,ContarLineas,contador
Funcionalidad: elimina las lineas del archivo de texto
"""
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
"""
Nombre:modificarTransporte
Entradas: placa del transporte
Funcionalidad: crea la ventana de modificar transporte y solicita la placa
"""
def modificarTransporte():
    ventanaModificarTransporte = Tk()
    ventanaModificarTransporte.geometry("500x300")
    ventanaModificarTransporte.title("Modificar empresa")
    ventanaModificarTransporte.config(bg = "Purple")
    ventanaModificarTransporte.iconbitmap("python.ico")

    etiquetaPlaca = tkinter.Label(ventanaModificarTransporte,text="Escriba la placa del transporte:",
                                    font=("Times new roman","12")).place(x=140,y=60)
    Placa = tkinter.Entry(ventanaModificarTransporte,text = "",font=("Times new roman","12"))
    Placa.place(x=155,y=90)

    boton = tkinter.Button(ventanaModificarTransporte,text = "Modificar transporte",font=("Times new roman","12"),
                           command = lambda:ModificarTrans_aux(Placa.get()))
    boton.place(x=170,y=120)

"""
Nombre:ModificarTrans_aux
Entradas: Placa
Funcionalidad: busca la placa en el archivo de texto
"""
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

"""
Nombre:ModificarTrans2
Entradas:leer,indice,contador
Funcionalidad: solicita los nuevos datos del transporte
"""       
def ModificarTrans2(leer,indice,contador):
    ModificarT = Tk()
    ModificarT.geometry("600x400")
    ModificarT.title("Modificar transporte")
    ModificarT.config(bg = "Purple")
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

"""
Nombre:ModificarT3
Entradas:Tipo,Marca,Modelo,Año,Empresa,AsientosVIP,AsientosNor,AsientosEco,leer,indice
Funcionalidad: escribe los nuevos datos en el archivo de texto
"""
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
"""
Nombre:mostrarTransportes
Funcionalidad: crea la ventana que muestra la lista de los transportes
"""
def mostrarTransportes():
    ventanaMostrarTransporte = Tk()
    ventanaMostrarTransporte.geometry("500x360")
    ventanaMostrarTransporte.title("Mostrar transportes")
    ventanaMostrarTransporte.config(bg = "Purple")
    ventanaMostrarTransporte.iconbitmap("python.ico")
    Archivo = open("Información del transporte.txt")
    Abrir = Archivo.readlines()
    Mostrar = tkinter.Listbox(ventanaMostrarTransporte,width = 40,height = 20)
    Mostrar.place(x=10,y=20)
    contador = 0
    for informacion in Abrir:
        Mostrar.insert(contador,informacion)
        contador += 1
    boton = tkinter.Button(ventanaMostrarTransporte,text = "Salir",font=("Times new roman","12"))
    boton.place(x=350,y=150)
        

#----------------------------------------------------------------------------------------------------------------------------
"""
Nombre:gestionViaje
Funcionalidad: crea la ventana que muestra el menú de gestion de viaje
"""
def gestionViaje():
    ventana4 = Tk()
    ventana4.geometry("250x200")
    ventana4.title("Menú administrativo")
    ventana4.config(bg = "Pink")
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
#----------------------------------------------------------------------------------------------------------------------------
"""
Nombre:IncluirViaje
Entradas: Provincia de Salida,Ciudad de Salida,Fecha de Salida,Hora de Salida,Provincia de Llegada,
         Ciudad de Llegada,Fecha de Llegada,Hora de Llegada,Empresa,Transporte,Monto VIP,Monto Nor,Monto Eco
Funcionalidad: solicita los datos para agregar el viaje
"""
def IncluirViaje():
    ventanaIncluirViaje = Tk()
    ventanaIncluirViaje.geometry("800x600")
    ventanaIncluirViaje.title("Incluir viaje")
    ventanaIncluirViaje.config(bg = "Pink")
    ventanaIncluirViaje.iconbitmap("python.ico")



    Archivo = open("Información del transporte.txt")
    Abrir = Archivo.readlines()
    Mostrar = tkinter.Listbox(ventanaIncluirViaje,width = 40,height = 20)
    Mostrar.place(x=500,y=210)
    contador = 0
    for informacion in Abrir:
        Mostrar.insert(contador,informacion)
        contador += 1
    

    etiquetaPS = tkinter.Label(ventanaIncluirViaje,text="Escriba la provincia de salida:",
                                    font=("Times new roman","12")).place(x=10,y=20)
    ProvinciaSalida = tkinter.Entry(ventanaIncluirViaje,text = "",font=("Times new roman","12"))
    ProvinciaSalida.place(x=270,y=20)

    etiquetaCS = tkinter.Label(ventanaIncluirViaje,text="Escriba la ciudad de salida:",
                                    font=("Times new roman","12")).place(x=10,y=60)
    CiudadSalida = tkinter.Entry(ventanaIncluirViaje,text = "",font=("Times new roman","12"))
    CiudadSalida.place(x=270,y=60)

    etiquetaFS = tkinter.Label(ventanaIncluirViaje,text="Escriba la fecha de salida:",
                                    font=("Times new roman","12")).place(x=10,y=100)
    FechaSalida = tkinter.Entry(ventanaIncluirViaje,text = "",font=("Times new roman","12"))
    FechaSalida.place(x=270,y=100)

    etiquetaHS = tkinter.Label(ventanaIncluirViaje,text="Escriba la hora de salida:",
                                    font=("Times new roman","12")).place(x=10,y=140)
    HoraSalida = tkinter.Entry(ventanaIncluirViaje,text = "",font=("Times new roman","12"))
    HoraSalida.place(x=270,y=140)

    etiquetaPLl = tkinter.Label(ventanaIncluirViaje,text="Escriba la provincia de llegada:",
                                font=("Times new roman","12")).place(x=10,y=180)
    ProvinciaLlegada = tkinter.Entry(ventanaIncluirViaje,text = "",font=("Times new roman","12"))
    ProvinciaLlegada.place(x=270,y=180)

    etiquetaCLl = tkinter.Label(ventanaIncluirViaje,text="Escriba la ciudad de llegada:",
                                    font=("Times new roman","12")).place(x=10,y=220)
    CiudadLlegada = tkinter.Entry(ventanaIncluirViaje,text = "",font=("Times new roman","12"))
    CiudadLlegada.place(x=270,y=220)

    etiquetaFLl = tkinter.Label(ventanaIncluirViaje,text="Escriba la fecha de llegada:",
                                    font=("Times new roman","12")).place(x=10,y=260)
    FechaLlegada = tkinter.Entry(ventanaIncluirViaje,text = "",font=("Times new roman","12"))
    FechaLlegada.place(x=270,y=260)

    etiquetaHLl = tkinter.Label(ventanaIncluirViaje,text="Escriba la hora de llegada:",
                                    font=("Times new roman","12")).place(x=10,y=300)
    HoraLlegada = tkinter.Entry(ventanaIncluirViaje,text = "",font=("Times new roman","12"))
    HoraLlegada.place(x=270,y=300)

    etiquetaEmpresa = tkinter.Label(ventanaIncluirViaje,text="Escriba el nombre de la empresa:",
                                    font=("Times new roman","12")).place(x=10,y=340)
    Empresa = tkinter.Entry(ventanaIncluirViaje,text = "",font=("Times new roman","12"))
    Empresa.place(x=270,y=340)

    etiquetaTransporte = tkinter.Label(ventanaIncluirViaje,text="Escriba la placa del transporte:",
                                    font=("Times new roman","12")).place(x=10,y=380)
    Transporte = tkinter.Entry(ventanaIncluirViaje,text = "",font=("Times new roman","12"))
    Transporte.place(x=270,y=380)

    etiquetaMVIP = tkinter.Label(ventanaIncluirViaje,text="Monto de asiento VIP:",
                                font=("Times new roman","12")).place(x=10,y=420)
    MontoVIP = tkinter.Entry(ventanaIncluirViaje,text = "",font=("Times new roman","12"))
    MontoVIP.place(x=270,y=420)

    etiquetaMNor = tkinter.Label(ventanaIncluirViaje,text="Monto de asiento normal:",
                                    font=("Times new roman","12")).place(x=10,y=460)
    MontoNor = tkinter.Entry(ventanaIncluirViaje,text = "",font=("Times new roman","12"))
    MontoNor.place(x=270,y=460)

    etiquetaMEco = tkinter.Label(ventanaIncluirViaje,text="Monto de asiento económico:",
                                font=("Times new roman","12")).place(x=10,y=500)
    MontoEco = tkinter.Entry(ventanaIncluirViaje,text = "",font=("Times new roman","12"))
    MontoEco.place(x=270,y=500)

    def agregarV():
        return agregarViaje(ProvinciaSalida.get(),CiudadSalida.get(),FechaSalida.get(),HoraSalida.get(),
                            ProvinciaLlegada.get(),CiudadLlegada.get(),FechaLlegada.get(),HoraLlegada.get(),
                            Empresa.get(),Transporte.get(),MontoVIP.get(),MontoNor.get(),MontoEco.get())

    boton = tkinter.Button(ventanaIncluirViaje, text = "Agregar viaje",font=("Times new roman","12"),
                    command= agregarV).place(x=210,y=540)

def agregarViaje(ProvinciaSalida,CiudadSalida,FechaSalida,HoraSalida,ProvinciaLlegada,CiudadLlegada,FechaLlegada,HoraLlegada,
                 Empresa,Transporte,MontoVIP,MontoNor,MontoEco):
    Archivo = "Información por viaje.txt"
    Archivo2 = open(Archivo,"a")
    NumeroViaje = numeroAutomatico()
    Archivo2.write("Número de viaje:"+NumeroViaje+"\n")
    Archivo2.write("Provincia de salida:"+ProvinciaSalida+"\n")
    Archivo2.write("Ciudad de salida:"+CiudadSalida+"\n")
    Archivo2.write("Fecha de salida:"+FechaSalida+"\n")
    Archivo2.write("Hora de salida:"+HoraSalida+"\n")
    Archivo2.write("Provincia de llegada:"+ProvinciaLlegada+"\n")
    Archivo2.write("Ciudad de llegada:"+CiudadLlegada+"\n")
    Archivo2.write("Fecha de llegada:"+FechaLlegada+"\n")
    Archivo2.write("Hora de llegada:"+HoraLlegada+"\n")
    Archivo2.write("Nombre de la empresa:"+Empresa+"\n")
    Archivo2.write("Placa del transporte:"+Transporte+"\n")
    Archivo2.write("Monto de asiento clase VIP:"+MontoVIP+"\n")
    Archivo2.write("Monto de asiento clase normal:"+MontoNor+"\n")
    Archivo2.write("Monto de asiento clase económica:"+MontoEco+"\n")
    Archivo2.write("......................................"+"\n")
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

    
    ventanaIncluirViaje.mainloop()

#----------------------------------------------------------------------------------------------------------------------------
"""
Nombre:eliminarViaje
Entradas: numero de viaje
Funcionalidad:crea la ventana para eliminar el viaje y solicita el numero del viaje
"""
def eliminarViaje():
    ventanaEliminarViaje = Tk()
    ventanaEliminarViaje.geometry("420x150")
    ventanaEliminarViaje.title("Eliminar transporte")
    ventanaEliminarViaje.config(bg = "Pink")
    ventanaEliminarViaje.iconbitmap("python.ico")

    etiquetaEliminar = tkinter.Label(ventanaEliminarViaje,text="Escriba el numero del viaje:",
                                            font=("Times new roman","12")).place(x=10,y=20)
    NumeroViaje = tkinter.Entry(ventanaEliminarViaje,text="",font=("Times new roman","12"))
    NumeroViaje.place(x=230,y=20)

    def eliminarV():
        return eliminarViaje_aux(NumeroViaje.get())

    boton = tkinter.Button(ventanaEliminarViaje, text = "Eliminar viaje",font=("Times new roman","12"),
                        command= eliminarV).place(x=230,y=50)

"""
Nombre:eliminarViaje_aux
Entradas: NumeroViaje
Funcionalidad: verifica que el numero se encuentre en el archivo de texto
"""
def eliminarViaje_aux(NumeroViaje):
    Almacen = open("Información por viaje.txt")
    Borrar = Almacen.readlines()
    if("Número de viaje:"+NumeroViaje+ "\n")in Borrar:
        ContarLineas = Borrar.index("Número de viaje:"+NumeroViaje+ "\n")
        BorrarLineas = EliminarViaje_aux(Borrar,ContarLineas,0)
        Almacen.close()
        Abrir = open("Información por viaje.txt","w")
        Abrir.write(BorrarLineas)
        Abrir.close()
        messagebox.showinfo("Eliminar viaje","El viaje ha sido eliminado")
    else:
        messagebox.showerror("Error","El viaje no existe")

"""
Nombre:EliminarViaje_aux
Entradas:Borrar,ContarLineas,contador
Funcionalidad: elimina las lineas del archivo de texto
"""
def EliminarViaje_aux(Borrar,ContarLineas,contador):
    if contador == 15:
        return TransformarString(Borrar)
    else:
        print(Borrar[ContarLineas].rstrip())
        Borrar.pop(ContarLineas)
        return EliminarViaje_aux(Borrar,ContarLineas,contador+1)

        
    ventanaEliminarViaje.mainloop()


#------------------------------------------------------------------------------------------------------------------------
"""
Nombre:modificarViaje
Entradas: numero del viaje
Funcionalidad: crea la ventana de modificar viaje y solicita el numero del viaje
"""
def modificarViaje():
    ventanaModificarViaje = Tk()
    ventanaModificarViaje.geometry("500x300")
    ventanaModificarViaje.title("Modificar viaje")
    ventanaModificarViaje.config(bg = "Pink")
    ventanaModificarViaje.iconbitmap("python.ico")

    etiquetaNumero = tkinter.Label(ventanaModificarViaje,text="Escriba el número del viaje:",
                                    font=("Times new roman","12")).place(x=155,y=60)
    NumeroViaje = tkinter.Entry(ventanaModificarViaje,text = "",font=("Times new roman","12"))
    NumeroViaje.place(x=160,y=90)

    boton = tkinter.Button(ventanaModificarViaje,text = "Modificar viaje",font=("Times new roman","12"),
                           command = lambda:ModificarViaje_aux(NumeroViaje.get()))
    boton.place(x=190,y=120)

"""
Nombre:ModificarViaje_aux
Entradas: NumeroViaje
Funcionalidad: busca el numero del viaje en el archivo de texto
"""
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

"""
Nombre:ModificarViaje2
Entradas:leer,indice,contador
Funcionalidad: solicita los nuevos datos del viaje
"""          
def ModificarViaje2(leer,indice,contador):
    ModificarV = Tk()
    ModificarV.geometry("600x600")
    ModificarV.title("Modificar viaje")
    ModificarV.config(bg = "Pink")
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

"""
Nombre:ModificarV3
Entradas:ProvinciaSalida,CiudadSalida,FechaSalida,HoraSalida,ProvinciaLlegada,CiudadLlegada,
        FechaLlegada,HoraLlegada,Empresa,Transporte,MontoVIP,MontoNor,MontoEco,leer,indice
Funcionalidad: escribe los nuevos datos en el archivo de texto
"""
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
"""
Nombre:mostrarViajes
Funcionalidad: crea la ventana que muestra la lista de los viajes
"""
def mostrarViajes():
    ventanaMostrarViaje = Tk()
    ventanaMostrarViaje.geometry("500x400")
    ventanaMostrarViaje.title("Mostrar transportes")
    ventanaMostrarViaje.config(bg = "Pink")
    ventanaMostrarViaje.iconbitmap("python.ico")
    Archivo = open("Información por viaje.txt")
    Abrir = Archivo.readlines()
    Mostrar = tkinter.Listbox(ventanaMostrarViaje,width = 40,height = 15)
    Mostrar.place(x=10,y=20)
    contador = 0
    for informacion in Abrir:
        Mostrar.insert(contador,informacion)
        contador += 1
    boton = tkinter.Button(ventanaMostrarViaje,text = "Mostrar viajes",font=("Times new roman","12"))
    boton.place(x=350,y=150)
    
    
#----------------------------------------------------------------------------------------------------------------------------
"""
Nombre:consultaHistorial
Funcionalidad: crea la ventana de consulta de historial que contiene el menú de consulta
"""
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
#--------------------------------------------------------------------------------------------------------------
"""
Nombre: estadisticas
Funcionalidad: crea la ventana de estadisticas
"""
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
#--------------------------------------------------------------------------------------------------------------------------
"""
Nombre:menuGeneral
Funcionalidad: crea la ventana que posee el menú general
"""
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
#--------------------------------------------------------------------------------------------------------------------------
"""
Nombre:consultaViajes
Funcionalidad: crea la ventana que contiene el menú de consulta de viajes
"""
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
#-------------------------------------------------------------------------------------------------------------------------------
"""
Nombre:reservacion
Entradas:Numero,Nombre,Cantidad VIP,Cantidad Nor,Cantidad Eco
Funcionalidad: crea la ventana de reservacion y solicita los datos para la reservacion
"""
def reservacion():
    ventanaReservacion = Tk()
    ventanaReservacion.geometry("600x500")
    ventanaReservacion.title("Reservación de viaje")
    ventanaReservacion.config(bg = "Aqua")
    ventanaReservacion.iconbitmap("python.ico")

    Archivo = open("Información por viaje.txt")
    Abrir = Archivo.readlines()
    Mostrar = tkinter.Listbox(ventanaReservacion,width = 50,height = 15)
    Mostrar.place(x=10,y=200)
    contador = 0
    for informacion in Abrir:
        Mostrar.insert(contador,informacion)
        contador += 1
    
    etiquetaNumero = tkinter.Label(ventanaReservacion,text="Digite el numero del viaje:",
                                    font=("Times new roman","12")).place(x=10,y=20)
    Numero = tkinter.Entry(ventanaReservacion,text = "",font=("Times new roman","12"))
    Numero.place(x=350,y=20)

    etiquetaNombre = tkinter.Label(ventanaReservacion,text="Escriba su nombre:",
                                    font=("Times new roman","12")).place(x=10,y=50)
    Nombre = tkinter.Entry(ventanaReservacion,text= "",font=("Times new roman","12"))
    Nombre.place(x=350,y=50)

    etiquetaCantidadVIP = tkinter.Label(ventanaReservacion,text="Cantidad de espacios a reservar VIP:",
                                font=("Times new roman","12")).place(x=10,y=80)
    CantidadVIP = tkinter.Entry(ventanaReservacion,text="",font=("Times new roman","12"))
    CantidadVIP.place(x=350,y=80)

    etiquetaCantidadNor = tkinter.Label(ventanaReservacion,text="Cantidad de espacios a reservar economicos:",
                                    font=("Times new roman","12")).place(x=10,y=110)
    CantidadNor = tkinter.Entry(ventanaReservacion,text = "",font=("Times new roman","12"))
    CantidadNor.place(x=350,y=110)

    etiquetaCantidadEco = tkinter.Label(ventanaReservacion,text="Cantidad de espacios a reservar economicos:",
                                font=("Times new roman","12")).place(x=10,y=140)
    CantidadEco = tkinter.Entry(ventanaReservacion,text = "",font=("Times new roman","12"))
    CantidadEco.place(x=350,y=140)

    def agregarR():
        return agregarReservacion(Numero.get(),Nombre.get(),CantidadVIP.get(),CantidadNor.get(),CantidadEco.get())

    boton = tkinter.Button(ventanaReservacion, text = "Agregar reservacion",font=("Times new roman","12"),
                    command= agregarR).place(x=380,y=250)
    
"""
Nombre:agregarReservacion
Entradas:Numero,Nombre,CantidadVIP,CantidadNor,CantidadEco
Funcionalidad: localiza los datos solicitados y guarda todo en el archivo de texto
"""
def agregarReservacion(Numero,Nombre,CantidadVIP,CantidadNor,CantidadEco):
    from datetime import datetime 
    Archivo2 = open("Información de reservación.txt","a") 
    Archivo2.close()
    Archivo3 = open("Información por viaje.txt")
    Informacion = Archivo3.read()
    Abrir = open("Información por viaje.txt")
    Archivo3 = Abrir.readlines()
    Archivo4 = ubicarIndice(Archivo3,"Número de viaje:"+Numero+"\n",0)
    Empresa = Archivo3[Archivo4+9][21:-1]
    Transporte = Archivo3[Archivo4+10][21:-1]
    LugarSalida = Archivo3[Archivo4+2][17:-1]
    FechaSalida = Archivo3[Archivo4+3][16:-1]
    HoraSalida = Archivo3[Archivo4+4][15:-1]
    LugarLlegada = Archivo3[Archivo4+6][18:-1]
    FechaLlegada = Archivo3[Archivo4+7][17:-1]
    HoraLlegada = Archivo3[Archivo4+8][16:-1]
    Placa = Archivo3[Archivo4+10][21:-1]
    Tipo = Archivo3[Archivo4+1][19:-1]
    Archivo5 = open("Información del transporte.txt")
    Archivo5 = Archivo5.readlines()
    Indice = Archivo5.index("Placa del transporte:"+Placa+"\n")
    VIPdisponible = Archivo5[Indice+6][31:-1]
    if int(VIPdisponible) - int(CantidadVIP)>= 0:
        NormalDisponible = Archivo5[Indice+7][34:-1]
        if int(NormalDisponible) - int(CantidadNor)>= 0:
            EconomicoDisponible = Archivo5[Indice+8][37:-1]
            if int(EconomicoDisponible) - int(CantidadEco)>= 0:
                Monto = int(CantidadVIP)*(int(Archivo3[Archivo4+11][27:-1]))
                Monto2 = int(CantidadNor)*(int(Archivo3[Archivo4+12][30:-1]))
                Monto3 = int(CantidadEco)*(int(Archivo3[Archivo4+13][33:-1]))
                Archivo = "Información de reservación.txt"
                Archivo2 = open(Archivo)
                lineas = Archivo2.readlines()
                Identificador = identificador(lineas,0)
                Archivo2 = open(Archivo,"a")
                FechaHora = datetime.now()
                
                Archivo2.write("Identificador:"+str(Identificador)+"\n")
                Archivo2.write("Número de viaje:"+str(Numero)+"\n")
                Archivo2.write("Nombre de persona que reserva:"+Nombre+"\n")
                Archivo2.write("Empresa:"+Empresa+"\n")
                Archivo2.write("Tipo de transporte:"+Tipo+"\n")
                Archivo2.write("Transporte:"+Transporte+"\n")
                Archivo2.write("Lugar de salida:"+LugarSalida+"\n")
                Archivo2.write("Fecha de salida:"+FechaSalida+"\n")
                Archivo2.write("Hora de salida:"+HoraSalida+"\n")
                Archivo2.write("Lugar de llegada:"+LugarLlegada+"\n")
                Archivo2.write("Fecha de llegada:"+FechaLlegada+"\n")
                Archivo2.write("Hora de llegada:"+HoraLlegada+"\n")
                Archivo2.write("Cantidad de espacios VIP reservados:"+CantidadVIP+"\n")
                Archivo2.write("Cantidad de espacios normales reservados:"+CantidadNor+"\n")
                Archivo2.write("Cantidad de espacios economicos reservados:"+CantidadEco+"\n")
                Archivo2.write("Fecha y hora de la reservacion:"+str(FechaHora)+"\n")
                Archivo2.write("Monto de reservacion:"+str(Monto+Monto2+Monto3)+"\n")
                Archivo2.write("......................................................."+"\n")
                answer = messagebox.showinfo("Reservar viaje", "El viaje ha sido reservado")

def ubicarIndice(listas,buscar,contador):
    if listas == []:
        return False
    elif buscar in listas[0]:
        return contador
    else:
        return ubicarIndice(listas[1:],buscar,contador+1)
                        
def identificador(lineas,contador):
    if lineas == []:
        return contador//16+1
    else:
        return identificador(lineas[1:],contador+1)

    
      
#----------------------------------------------------------------------------------------------------------------------
"""
Nombre:cancelacion
Entradas: numero de identificador
Funcionalidad: crea la ventana que solicita el numero de identificador
"""
def cancelacion():
    ventanaCancelacion = Tk()
    ventanaCancelacion.geometry("400x150")
    ventanaCancelacion.title("Cancelacion de viaje")
    ventanaCancelacion.config(bg = "Aqua")
    ventanaCancelacion.iconbitmap("python.ico")

    etiquetaCancelar = tkinter.Label(ventanaCancelacion,text="Digite el numero del identificador:",
                                    font=("Times new roman","12")).place(x=10,y=20)
    Cancelar = tkinter.Entry(ventanaCancelacion,text = "",font=("Times new roman","12"))
    Cancelar.place(x=220,y=20)

    def cancelacion1():
        return cancelarReservacion(Cancelar.get())

    boton = tkinter.Button(ventanaCancelacion, text = "Cancelar reservacion",font=("Times new roman","12"),
                    command= cancelacion1).place(x=230,y=50)
"""
Nombre:cancelarReservacion
Entradas:Cancelar
Funcionalidad: elimina la reservacion del archivo de texto
"""
def cancelarReservacion(Cancelar):
    Buscar = open("Información de reservación.txt")
    Archivo = Buscar.readlines()
    if("Identificador:"+Cancelar+"\n")in Archivo:
       Indice = ubicarIndice(Archivo,("Identificador:"+Cancelar+"\n"),0)
       Eliminar = eliminarListas(Archivo,Indice-18,0)
       Buscar.close()
       Abrir = open("Información de reservación.txt","w")
       Abrir.write(Eliminar)
       Abrir.close()
       

def eliminarListas(archivo,indice,contador):
    if contador > 17:
        return TransformarString_aux(archivo)
    else:
        archivo.pop(indice)
        return eliminarListas(archivo,indice,contador+1)





    ventanaCancelacion.mainloop()
    


ventanaPrincipal()
