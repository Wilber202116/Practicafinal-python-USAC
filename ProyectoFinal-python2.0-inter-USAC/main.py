from tkinter import *
import tkinter as tk
from tkinter import messagebox, filedialog
import re
from person import Person
import database
from PIL import Image, ImageTk
import ast

#funcion que reaparece la ventana iniciar sesion por si alguien da en la X de la ventana
#def seReaparece():
#    root.deiconify()

#verifica si el archivo de database.txt tiene datos
def databasecheck():
        archivo = open("database.txt", "r")
        contenido = archivo.read()
        #print(contenido)
        if contenido == "":
            archivo.close()
            personas = database.personas
            return personas
        if contenido:
            #----- Va a leer el archivo y pasarlo nuevamente a lista-------
            cadena = ast.literal_eval(contenido)
            archivo.close()
            #--- Hay que crear un nuevo codigo que vaya viendo el contenido de la nueva lista y lo convierta ---
            #--- de nuevo en un objeto, en la lista personas ---
            database.personas.clear()

            for i in cadena:
                #print(i)
                newperson = Person(i[0],i[1],i[2],i[3],i[4],i[5])
                database.personas.append(newperson)  

            #for persona in database.personas:
             #   if persona.getnombre() == "wil":
              #      print(persona)
            #for j in database.personas:
            #    print(j)
            personas = database.personas
            #print(personas)
            return personas

def contra_largo(text):
    return len(text) <=8

def solo_numeros(text):
    return text.isdigit()

#esto evita que coloquen incorrectamente el correo eletronico en el inicio
def correo_para():
    correo = entryCorreo.get()
    
    patron = r"^[a-zA-z0-9-_+-]+@[a-zA-Z0-9+-]+\.[a-zA-Z0-9-.]+$"
    if re.match(patron, correo):
        return correo
    else:
        messagebox.showerror("Error", "Correo no valido")

#ventana para registrar un nuevo usuario
def ventana_registro():
    ventana_registro = tk.Toplevel(root)
    #verifica el correo en el registro
    def correo_regis():
        correo1 = entrycorreo1.get()
    
        patron = r"^[a-zA-z0-9-_+-]+@[a-zA-Z0-9+-]+\.[a-zA-Z0-9-.]+$"
        if re.match(patron, correo1):
            return correo1
        else:
            messagebox.showerror("Error", "Correo registrado no valido")

    def seReapareceregistro():
        root.deiconify()
        ventana_registro.destroy()

    #ventana_registro = tk.Tk()
    ventana_registro.title("Registrarse")
    ventana_registro.geometry("310x350")
    ventana_registro.protocol("WM_DELETE_WINDOW", seReapareceregistro)
    root.withdraw()

    largo_valido = ventana_registro.register(contra_largo)
    solo_Numeros = ventana_registro.register(solo_numeros)

    Label(ventana_registro,text="Bienvenido al registro").grid(row=0, column=0, columnspan=4, pady=10,padx=10)
    Label(ventana_registro,text="Identificacion (DPI, etc...):").grid(row=1, column=0, sticky=E, columnspan=2, pady=10,padx=10)
    Label(ventana_registro,text="Nombre:").grid(row=2, column=0, sticky=E, columnspan=2, pady=10,padx=10)
    Label(ventana_registro,text="Apellido:").grid(row=3, column=0, sticky=E,  columnspan=2, pady=10,padx=10)
    Label(ventana_registro, text="edad").grid(row=4, sticky=E,  column=0, columnspan=2, pady=10,padx=10)
    Label(ventana_registro,text="Correo electronico:").grid(row=5, column=0, sticky=E,  columnspan=2, pady=10,padx=10)
    Label(ventana_registro,text="Contraseña:").grid(row=6, column=0, sticky=E,  columnspan=2, pady=10,padx=10)

    entryiden = Entry(ventana_registro, validate="key", validatecommand=(solo_Numeros, "%P"))
    entrynombre = Entry(ventana_registro)
    entryapellido = Entry(ventana_registro)
    entryedad = Entry(ventana_registro, validate="key",validatecommand=(solo_Numeros, "%P"))
    entrycorreo1 = Entry(ventana_registro)
    entrycontra1 = Entry(ventana_registro, show="*",validate="key", validatecommand=(largo_valido, "%P"))

    entryiden.grid(row=1, column=2, columnspan=2, pady=10,padx=10)
    entrynombre.grid(row=2, column=2, columnspan=2, pady=10,padx=10)
    entryapellido.grid(row=3, column=2, columnspan=2, pady=10,padx=10)
    entryedad.grid(row=4, column=2, columnspan=2, pady=10,padx=10)
    entrycorreo1.grid(row=5, column=2, columnspan=2, pady=10,padx=10)
    entrycontra1.grid(row=6, column=2, columnspan=2, pady=10,padx=10)

    #funcion del boton, donde tiene algunas validaciones dentro para registrar el nuevo usuario
    def registrar_cuenta():
        iden = int(entryiden.get())
        nombre = entrynombre.get()
        apellido = entryapellido.get()
        edad = int(entryedad.get())
        correo1 = correo_regis()
        contra1 = entrycontra1.get()
        #print(nuevaDatabase)
        mensaje, confirmacion = Person.registro_persona(str(iden), correo1, contra1, databasecheck())
        # antes de completar el registro de usuario, verifica su edad y la confirmacion en la linea
        #de codigo de arriba ↑
        if confirmacion == False and edad >= 18:
            print(correo1)
            print(contra1)
            #genera la instancia del nuevo objeto en el modulo database.py
            newPerson = Person(str(iden), nombre, apellido, correo1, contra1)
            database.personas.append(newPerson)
            #aqui empieza a añadir el nuevo usuario en database.txt al presionar el boton registrar
            updatebase = []
            for i in database.personas:
                provisional = [i.getiden(), i.getnombre(), i.getapellido(), i.getcorreo(), i.getcontra(), i.getfotografia()]
                updatebase.append(provisional)
            nuevabase = str(updatebase)
            archivo = open("database.txt","w+")
            archivo.write(nuevabase)
            contenido = archivo.read()
            print(contenido)
            archivo.close()
            
            messagebox.showinfo("Atencion", mensaje)
            root.deiconify()
            ventana_registro.destroy()
        if confirmacion == True:
            messagebox.showerror("Error", mensaje)
        elif edad<18:
            messagebox.showerror("Error", "Eres menor de edad, intentalo cuando llegues a la edad minima")


    Button(ventana_registro, text="Registrar cuenta", command=registrar_cuenta).grid(row=7, column=0, columnspan=4, pady=10,padx=10)

def control_inicio():
    
    global user_actual
    correo = correo_para()
    contraseña = entryContra.get()

    mensaje, persona = Person.iniciar_sesion(correo, contraseña, databasecheck())
    
    if persona:
        user_actual = persona
        ventana_inicio(user_actual)
        entryCorreo.delete(0, tk.END)
        entryContra.delete(0, tk.END)
        root.withdraw()
    else:
        messagebox.showerror("Error", mensaje)



def ventana_inicio(user_actual):

    

    ventana_inicio = tk.Toplevel(root)
    ventana_inicio.title("Perfil")
    ventana_inicio.geometry("380x250")
    def seReapareceinicio():
        root.deiconify()
        ventana_inicio.destroy()
    ventana_inicio.protocol("WM_DELETE_WINDOW", seReapareceinicio)

    img_original = Image.open(user_actual.fotografia)
    img = img_original.resize((120,90), Image.Resampling.LANCZOS)
    global img_tk
    img_tk = ImageTk.PhotoImage(img)

    def cerrar_sesion():
        root.deiconify()
        ventana_inicio.destroy()

    def cambiar_foto():
        ruta = filedialog.askopenfilename(filetypes=[("Archivos", "*.jpg .png .JPG .PNG .gif")])
        user_actual.fotografia = ruta
        nuevalista =[]
        
        for j in databasecheck():
            provisional = [j.getiden(),j.getnombre(),j.getapellido(),j.getcorreo(),j.getcontra(),j.getfotografia()]
            nuevalista.append(provisional)
        
        for i in nuevalista:
            if i[3] == user_actual.correo:
                i[5] = user_actual.fotografia
        
        a = str(nuevalista)
        print(a)
        archivo = open("database.txt", "w")
        archivo.write(a)
        archivo.close()
        
        if ruta:
            img2 = Image.open(user_actual.fotografia)
            img1 = img2.resize((120,90), Image.Resampling.LANCZOS)
            img_cambiada = ImageTk.PhotoImage(img1)
            imagen.configure(image=img_cambiada)
            imagen.image = img_cambiada

    
    if user_actual:
        Label(ventana_inicio,text="Perfil").grid(row=0, column=0, columnspan=6, pady=10,padx=10)
        Label(ventana_inicio,text=f"Identificacion (DPI, etc...): {user_actual.identificacion}").grid(row=1, column=0, sticky=W, columnspan=2, pady=10,padx=10)
        Label(ventana_inicio,text=f"Nombre: {user_actual.nombre}").grid(row=2, column=0, sticky=W, columnspan=2, pady=10,padx=10)
        Label(ventana_inicio,text=f"Apellido: {user_actual.apellido}").grid(row=3, column=0, sticky=W,  columnspan=2, pady=10,padx=10)
        Label(ventana_inicio,text=f"Correo electronico: {user_actual.correo}").grid(row=4, column=0, sticky=W,  columnspan=2, pady=10,padx=10)
        imagen = tk.Label(ventana_inicio, image=img_tk)
        imagen.image = img_tk
        imagen.grid(row=1, column=3, columnspan=3, rowspan=4, pady=10,padx=10)
        Button(ventana_inicio, text="Cambiar foto", command=cambiar_foto).grid(row=4, column=3, columnspan=4, pady=10,padx=10)
    Button(ventana_inicio, text="Cerrar sesion", command=cerrar_sesion).grid(row=5, column=0,  columnspan=4, pady=10,padx=10)
        


root = tk.Tk()
root.title("Iniciar sesion")
root.geometry("310x180")

largo_valido = root.register(contra_largo)

nuevaDatabase = []
'''
for i in database.personas:
    nuevaDatabase.append(i.getiden())
    nuevaDatabase.append(i.getnombre())
    nuevaDatabase.append(i.getapellido())
    nuevaDatabase.append(i.getcorreo())
    nuevaDatabase.append(i.getcontra())
    nuevaDatabase.append(i.getfotografia())

for i in database.personas:
    a = f"{i.getiden()}, {i.getnombre()}, {i.getapellido()}, {i.getcorreo()}, {i.getcontra()}, {i.getfotografia()}"
    nuevaDatabase.append(a)
base = str(nuevaDatabase)
updatebase = base.split()
    
base = ",".join(map(str, nuevaDatabase))
#print(type(base))
#updatebase = ast.literal_eval(base)
updatebase = base.split(",")
'''
#for i in database.personas:
#    a = [i.getiden(), i.getnombre(),i.getapellido(),i.getcorreo(),i.getcontra(),i.getfotografia()]
#    nuevaDatabase.append(a)

#print(nuevaDatabase)

Label(root, text="Bienvenido al inicio de sesion", font=("arial", 12)).grid(row=0, column=0, columnspan=4, pady=10,padx=10)
Label(root, text="Correo electronico", font=("arial", 12)).grid(row=1, column=0, sticky=W, columnspan=2, pady=10,padx=10)
Label(root, text="Contraseña", font=("arial", 12)).grid(row=2, column=0, sticky=W, columnspan=2, pady=10,padx=10)

entryCorreo = Entry(root)
entryCorreo.grid(row=1, column=2, columnspan=2, pady=10,padx=10)
entryContra = Entry(root, show="*",validate="key", validatecommand=(largo_valido, "%P"))
entryContra.grid(row=2, column=2, columnspan=2, pady=10, padx=10)

btnlogin = Button(root, text="Continuar", command=control_inicio)
btnlogin.grid(row=3, column=2, columnspan=2, pady=10, padx=10)

btnreg = Button(root, text="Registrarse", command=ventana_registro)
btnreg.grid(row=3, column=0, columnspan=2, pady=10, padx=10)



root.mainloop()