class Person:
    def __init__(self, identificacion: str, nombre:str, apellido:str, correo_electronico:str, contraseña:str, fotografia:str='imagen.jpg'):
        self.identificacion = identificacion
        self.nombre = nombre
        self.apellido = apellido
        self.correo = correo_electronico
        self.contraseña = contraseña
        self.fotografia = fotografia #lugar donde se encuentra la fotografia editar luego

    def getiden(self):
        iden = self.identificacion
        return iden

    def getnombre(self):
        nombre = self.nombre
        return nombre
    
    def getapellido(self):
        apellido = self.apellido
        return apellido
    
    def getcorreo(self):
        correo = self.correo
        return correo
    
    def getcontra(self):
        contra = self.contraseña
        return contra
    
    def getfotografia(self):
        foto = self.fotografia
        return foto

    def setiden(self,iden):
        self.identificacion = iden
    
    def setnombre(self, nombre):
        self.nombre = nombre

    def setapellido(self, apellido):
        self.apellido = apellido
    
    def setcorreo(self, correo):
        self.correo = correo

    def setcontra(self, contra):
        self.contraseña = contra

    def setfotografia(self, ruta):
        self.fotografia = ruta

    @staticmethod
    def iniciar_sesion(correo:str, contraseña:str, personas):
        print(correo)
        print(contraseña)
        for persona in personas:
            if persona.correo == correo and persona.contraseña == contraseña:
                print(persona)
                return "Inicio de sesion exitoso", persona
        return "correo y/o contraseña incorrectos", None
    
    @staticmethod
    def registro_persona(identificacion: str, correo_electronico:str, contraseña:str, updatebase):
        print(identificacion)
        print(correo_electronico)
        print(contraseña)
        for persona in updatebase:
            if persona.identificacion == identificacion or persona.correo == correo_electronico or correo_electronico == None or persona.contraseña == contraseña:
                return "Las credenciales ya se encuentran en la base de datos", True
        return "Registro exitoso", False
    
    def __str__(self):
        return f"{self.getiden()}, {self.getnombre()}, {self.getapellido()}, {self.getcorreo()}, {self.getcontra()}, {self.getfotografia()}"