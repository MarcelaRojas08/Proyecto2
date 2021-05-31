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
    menuPrincipal.add_command(label = "1 - Opciones administrativas",font =("Times new roman","12","italic","bold"),command = menuAdministrativo)
    menuPrincipal.add_command(label = "2 - Opciones de usuario normal",font =("Times new roman","12","italic","bold"),command = menuGeneral)
    menuPrincipal.add_command(label = "3 - Salir",font =("Times new roman","12","italic","bold"),command = ventana.destroy)

    menu.add_cascade(label="Menú principal", menu = menuPrincipal)#diseño del menú principal
    
    

def menuAdministrativo():
    abrirVentana = Tk()
    abrirVentana.geometry("600x300")
    abrirVentana.title("Menú administrativo")
    abrirVentana.config(bg = "skyblue")
    abrirVentana.iconbitmap("python.ico")
    etiqueta=tkinter.Label(abrirVentana,text="Escriba la clave de acceso",bg = "white",font =("Times new roman","14","italic","bold"))
    etiqueta.place(x=180,y=60)
    entrada = tkinter.Entry(abrirVentana)
    entrada.place(x=225,y=90)
    
    
    def clave():
        acceso=entrada.get()
        if(acceso == "acceso"):
            
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

    boton = tkinter.Button(abrirVentana,text = "Ingresar",font=("Times new roman","12"),command = clave)
    boton.place(x=260,y=120)
    
def gestionEmpresa():
    ventana2 = Tk()
    ventana2.geometry("250x200")
    ventana2.title("Menú administrativo")
    ventana2.config(bg = "Turquoise")
    ventana2.iconbitmap("python.ico")


    def IncluirEmpresa():
        ventanaIncluirEmpresa = tkinter.Tk()
        ventanaIncluirEmpresa.geometry("600x300")
        ventanaIncluirEmpresa.title("Incluir empresa")
        ventanaIncluirEmpresa.config(bg = "Turquoise")
        ventanaIncluirEmpresa.iconbitmap("python.ico")
        Cedula = tkinter.StringVar()
        Nombre = tkinter.StringVar()
        Provincia = tkinter.StringVar()
        Señas = tkinter.StringVar()

        etiquetaCedula = tkinter.Label(ventanaIncluirEmpresa,text="Dígite el número de cédula jurídica:",font=("Times new roman","12")).place(x=10,y=20)
        Cedula = tkinter.Entry(ventanaIncluirEmpresa,textvariable = Cedula,font=("Times new roman","12"))
        Cedula.place(x=250,y=20)

        etiquetaNombre = tkinter.Label(ventanaIncluirEmpresa,text="Escriba el nombre de la empresa:",font=("Times new roman","12")).place(x=10,y=60)
        Nombre = tkinter.Entry(ventanaIncluirEmpresa,textvariable = Nombre,font=("Times new roman","12"))
        Nombre.place(x=250,y=60)

        etiquetaProvincia = tkinter.Label(ventanaIncluirEmpresa,text="Escriba la provincia de la empresa:",font=("Times new roman","12")).place(x=10,y=100)
        Provincia = tkinter.Entry(ventanaIncluirEmpresa,textvariable = Provincia,font=("Times new roman","12"))
        Provincia.place(x=250,y=100)

        etiquetaSeñas = tkinter.Label(ventanaIncluirEmpresa,text="Escriba las señas exactas de la empresa:",font=("Times new roman","12")).place(x=10,y=140)
        Señas = tkinter.Entry(ventanaIncluirEmpresa,textvariable = Señas,font=("Times new roman","12"))
        Señas.place(x=270,y=140)

        def agregarEmpresa(Cedula,Nombre,Provincia,Señas):
            Archivo = open("Información de la empresa.txt","a")
            if len(Cedula) == 10:
                Archivo2 = open("Información de la empresa.txt")
                Comprobar = Archivo2.readlines()
                if("Cédula júridica:"+Cedula+"\n") in Comprobar:
                    answer = messagebox.showerror("Error", "La cedula juridica ya existe")
                else:
                    Archivo.write("Cédula júridica:"+Cedula+"\n")
                    Archivo.write("Nombre de la empresa:"+Nombre+"\n")
                    Archivo.write("Provincia de la empresa:"+Provincia+"\n")
                    Archivo.write("Señas exactas de la empresa:"+Señas+"\n")
                    Archivo.write(".............................................."+"\n")
                    Archivo.close()
                    messagebox.showinfo(title = "Agregar Empresa",message = "La empresa ha sido agregada")
            else:
                answer2 = messagebox.showerror("Error", "La cedula juridica debe tener 10 digitos")

        boton = tkinter.Button(ventanaIncluirEmpresa, text = "Agregar empresa",font=("Times new roman","12"),
                       command= lambda:agregarEmpresa(Cedula.get(),Nombre.get(),Provincia.get(),Señas.get())).place(x=200,y=200)
        ventanaIncluirEmpresa.mainloop()

        
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
            if contador == 5:
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

        boton = tkinter.Button(ventanaEliminarEmpresa, text = "Eliminar empresa",font=("Times new roman","12"),
                           command= eliminarEmpresa_aux).place(x=200,y=200)
        ventanaEliminarEmpresa.mainloop()

    def modificarEmpresa():
        ventanaModificarEmpresa = Tk()
        ventanaModificarEmpresa.geometry("500x300")
        ventanaModificarEmpresa.title("Modificar empresa")
        ventanaModificarEmpresa.config(bg = "Turquoise")
        ventanaModificarEmpresa.iconbitmap("python.ico")

        etiquetaModificar = tkinter.Label(ventanaEliminarEmpresa,text="Dígite el número de cédula jurídica:",
                                             font=("Times new roman","12")).place(x=10,y=20)
        Modificar = tkinter.Entry(ventanaModificarEmpresa,text="",font=("Times new roman","12"))
        Modificar.pack()

        if ("Cédula júridica:"+Cedula+ "\n") in empresa:
            Indice = empresa.index("Cédula júridica:"+Cedula+"\n")
            Empresa2_aux(empresa,Indice,0)
            EmpresaNueva = Empresa3_aux(empresa,Indice+1,0)
            Abrir = open("Información de la empresa.txt","w")
            Abrir.write(TransformarString_aux(EmpresaNueva))
            Abrir.close()


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

        
      

    menu1 = Menu(ventana2)
    op2 = Menu(menu1,tearoff = 0)
    op2.add_command(label = "1 - Incluir empresa",font=("Times new roman","12"),command = IncluirEmpresa)
    op2.add_command(label = "2 - Eliminar empresa",font=("Times new roman","12"),command = eliminarEmpresa)
    op2.add_command(label = "3 - Modificar empresa",font=("Times new roman","12"),command = lambda:modificarEmpresa)
    op2.add_command(label = "4 - Mostrar empresas",font=("Times new roman","12"),command = mostrarEmpresas)
    op2.add_command(label = "5 - Retornar",font=("Times new roman","12"),command = lambda:menuAdministrativo)
    menu1.add_cascade(label=" Gestión de empresa",font=("Times new roman","12"), menu = op2)
    ventana2.config(menu=menu1)
    ventana2.mainloop()

                
def gestionTransporte():
    ventana3 = Tk()
    ventana3.geometry("250x200")
    ventana3.title("Menú administrativo")
    ventana3.config(bg = "Turquoise")
    ventana3.iconbitmap("python.ico")
   

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

        boton = tkinter.Button(ventanaIncluirTransporte, text = "Agregar transporte",font=("Times new roman","12"),
                       command= lambda:agregarTransporte(Placa.get(),Tipo.get(),Marca.get(),Modelo.get(),Año.get(),Empresa.get(),
                                                         AsientosVIP.get(),AsientosNor.get(),AsientosEco.get())).place(x=200,y=380)
        ventanaIncluirTransporte.mainloop()

    
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


        boton = tkinter.Button(ventanaEliminarTransporte, text = "Eliminar transporte",font=("Times new roman","12"),
                        command= eliminarTransporte_aux).place(x=200,y=200)
        ventanaEliminarTransporte.mainloop()

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
        


    menu2 = Menu(ventana3)
    op2 = Menu(menu2,tearoff = 0)
    op2.add_command(label = "1 - Incluir transporte",font=("Times new roman","12"),command =IncluirTransporte)
    op2.add_command(label = "2 - Eliminar transporte",font=("Times new roman","12"),command = eliminarTransporte)
    op2.add_command(label = "3 - Modificar transporte",font=("Times new roman","12"))
    op2.add_command(label = "4 - Mostrar transportes",font=("Times new roman","12"),command = mostrarTransportes)
    op2.add_command(label = "5 - Retornar",font=("Times new roman","12"),command = menuAdministrativo)
    menu2.add_cascade(label=" Gestión de transporte por empresa",font=("Times new roman","12"), menu = op2)
    ventana3.config(menu=menu2)
    ventana3.mainloop()

    

def gestionViaje():
    ventana4 = Tk()
    ventana4.geometry("250x200")
    ventana4.title("Menú administrativo")
    ventana4.config(bg = "Turquoise")
    ventana4.iconbitmap("python.ico")

    def IncluirViaje():
        ventanaIncluirViaje = Tk()
        ventanaIncluirViaje.geometry("600x600")
        ventanaIncluirViaje.title("Incluir viaje")
        ventanaIncluirViaje.config(bg = "Turquoise")
        ventanaIncluirViaje.iconbitmap("python.ico")
        NumeroViaje = tkinter.StringVar()
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

        def agregarViaje(NumeroViaje,ProvinciaSalida,CiudadSalida,FechaSalida,HoraSalida,ProvinciaLlegada,CiudadLlegada,
                         FechaLlegada,HoraLlegada,Empresa,Transporte,MontoVIP,MontoNor,MontoEco):
            Archivo = open("Información por viaje.txt","a")
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

        boton = tkinter.Button(ventanaIncluirViaje, text = "Agregar viaje",font=("Times new roman","12"),
                       command= lambda:agregarViaje(NumeroViaje.get(),ProvinciaSalida.get(),CiudadSalida.get(),FechaSalida.get(),HoraSalida.get(),
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

        def TransformarString(Borrar):
            if isinstance(Borrar,list):
                string = ""
                for linea in Borrar:
                    string += linea
                return string
            else:
                print("")


        boton = tkinter.Button(ventanaEliminarViaje, text = "Eliminar viaje",font=("Times new roman","12"),
                        command= eliminarViaje_aux).place(x=200,y=200)
        ventanaEliminarViaje.mainloop()


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
    
    menu3 = Menu(ventana4)
    op3 = Menu(menu3,tearoff = 0)
    op3.add_command(label = "1 - Incluir viaje",font=("Times new roman","12"),command = IncluirViaje)
    op3.add_command(label = "2 - Eliminar viaje",font=("Times new roman","12"),command = eliminarViaje)
    op3.add_command(label = "3 - Modificar viaje",font=("Times new roman","12"))
    op3.add_command(label = "4 - Mostrar viajes",font=("Times new roman","12"),command = mostrarViajes)
    op3.add_command(label = "5 - Retornar",font=("Times new roman","12"),command = menuAdministrativo)
    menu3.add_cascade(label=" Gestión de viaje",font=("Times new roman","12"), menu = op3)
    ventana4.config(menu=menu3)
    ventana4.mainloop()

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
