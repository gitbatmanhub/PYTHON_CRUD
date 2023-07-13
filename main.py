import tkinter as tk
import MySQLdb
from tkinter import messagebox

class GestorBaseDatos:
    def __init__(self):
        self.conexion = None
        self.cursor = None

    def conectar(self):
        self.conexion = MySQLdb.connect(host="localhost", user="root", passwd="admin1223", db="python")
        self.cursor = self.conexion.cursor()

    def desconectar(self):
        if self.cursor:
            self.cursor.close()
        if self.conexion:
            self.conexion.close()

    def ejecutar_consulta(self, consulta, parametros=None):
        if parametros is None:
            self.cursor.execute(consulta)
        else:
            self.cursor.execute(consulta, parametros)
        return self.cursor.fetchall()

#Centrar Ventana
def centrar_ventana(ventana):
    ventana.update_idletasks()
    ancho_ventana = ventana.winfo_width()
    alto_ventana = ventana.winfo_height()
    x_pos = (ventana.winfo_screenwidth() // 2) - (ancho_ventana // 2)
    y_pos = (ventana.winfo_screenheight() // 2) - (alto_ventana // 2)
    ventana.geometry(f"+{x_pos}+{y_pos}")

# Crear una clase para la ventana de inicio de sesión
class VentanaLogin(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Inicio de sesión")
        self.geometry("400x400")
        self.gestor_db = GestorBaseDatos()
        self.gestor_db.conectar()
        centrar_ventana(self)

        # Crear widgets para el inicio de sesión
        self.etiqueta_usuario = tk.Label(self, text="Usuario:")
        self.cuadro_usuario = tk.Entry(self)
        self.etiqueta_contraseña = tk.Label(self, text="Contraseña:")
        self.cuadro_contraseña = tk.Entry(self, show="*")
        self.boton_iniciar_sesion = tk.Button(self, text="Iniciar sesión", command=self.iniciar_sesion)
        self.boton_salir = tk.Button(self, text="Salir", command=self.destroy)

        # Ubicar los widgets en la ventana
        self.etiqueta_usuario.pack()
        self.cuadro_usuario.pack()
        self.etiqueta_contraseña.pack()
        self.cuadro_contraseña.pack()
        self.boton_iniciar_sesion.pack()
        self.boton_salir.pack()

    # Definir función de inicio de sesión
    def iniciar_sesion(self):
        usuario = self.cuadro_usuario.get()
        contraseña = self.cuadro_contraseña.get()
        if usuario == "" or contraseña == "":
            self.mostrar_mensaje_error("Ingresa las credenciales pedazo de imbecil")
        else:
            # Ejecutar consulta para verificar usuario y contraseña
            consulta = "SELECT tipoUsuario FROM usuario WHERE user = %s AND password = %s"
            resultado = self.gestor_db.ejecutar_consulta(consulta, (usuario, contraseña))
            
            if resultado:
                tipo_usuario = resultado[0][0]

                if tipo_usuario == 1:
                    self.mostrar_ventana_admin()
                elif tipo_usuario == 2:
                    self.mostrar_ventana_usuario()
                else:
                    self.mostrar_mensaje_error("Tipo de usuario desconocido")
            else:
                self.mostrar_mensaje_error("Usuario o contraseña incorrectos")

    # Función para mostrar ventana de administrador
    def mostrar_ventana_admin(self):
        self.withdraw()  # Ocultar ventana de inicio de sesión
        ventana_admin = tk.Toplevel()
        ventana_admin.geometry("400x400")
        ventana_admin.title("Ventana de administrador")

        #Agregar más widgets
        etiqueta_usuarios=tk.Label(ventana_admin, text="Usuarios:")
        etiqueta_usuarios.pack()

        consulta_usuarios="Select * from usuario"
        usuarios= self.gestor_db.ejecutar_consulta(consulta_usuarios)
        for usuario in usuarios:
            etiqueta_usuarios.configure(text=etiqueta_usuarios.cget("text")+ f"\n{usuario}")

        # Agregar los widgets necesarios para mostrar las ventas totales, ventas del día y ventas del mes
        boton_cerrar_sesion = tk.Button(ventana_admin, text="Cerrar sesión", command=self.mostrar_ventana_login)
        boton_cerrar_sesion.pack()
        centrar_ventana(ventana_admin)



    

    # Función para mostrar ventana de usuario
    def mostrar_ventana_usuario(self):
        self.withdraw()  # Ocultar ventana de inicio de sesión
        ventana_usuario = tk.Toplevel()
        ventana_usuario.geometry("400x400")
        ventana_usuario.title("Ventana de usuario")

        # Agregar los widgets necesarios para mostrar las compras del usuario
        boton_cerrar_sesion = tk.Button(ventana_usuario, text="Cerrar sesión", command=self.mostrar_ventana_login)
        boton_cerrar_sesion.pack()
        centrar_ventana(ventana_usuario)

    # Función para mostrar mensajes de error
    def mostrar_mensaje_error(self, mensaje):
        messagebox.showerror("Error", mensaje)

    # Función para mostrar la ventana de inicio de sesión nuevamente al cerrar sesión
    def mostrar_ventana_login(self):
        self.destroy()
        VentanaLogin().mainloop()

# Crear instancia de la ventana de inicio de sesión
ventana_login = VentanaLogin()

# Iniciar el bucle de eventos
ventana_login.mainloop()
