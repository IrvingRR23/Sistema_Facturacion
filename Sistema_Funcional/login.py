import tkinter as tk
from tkinter import messagebox
import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from database.database import DatabaseConnection
import Sistema_Funcional.app.sistema_facturacion as sistema_facturacion

class LoginApp:
    def __init__(self,root):
        self.root = root
        self.root.title("Inicio de Sesión - Stack de Sabor")
        self.root.geometry("420x320")
        self.root.config(bg="#f4f6f8")
        self.root.resizable(False,False)

        tk.Label(
            self.root,
            text="Stack de Sabor",
            font=("Times New Roman", 22, "bold"),
            fg="#1f2a44",
            bg="#f4f6f8"
        ).pack(pady=(25, 5))

        tk.Label(
            self.root,
            text="Inicia sesión para continuar",
            font=("Times New Roman", 12),
            bg="#f4f6f8",
            fg="#555"
        ).pack(pady=(0, 15))

        # Marco principal
        frame = tk.Frame(self.root, bg="#ffffff", bd=1, relief="solid")
        frame.pack(padx=20, pady=10, fill="both", expand=False)

        # Campos de entrada
        tk.Label(frame, text="Usuario:", font=("Times New Roman", 13), bg="#ffffff").grid(row=0, column=0, padx=15, pady=15, sticky="w")
        self.entry_user = tk.Entry(frame, font=("Times New Roman", 13), width=22, bd=1, relief="solid")
        self.entry_user.grid(row=0, column=1, padx=15, pady=15)

        tk.Label(frame, text="Contraseña:", font=("Times New Roman", 13), bg="#ffffff").grid(row=1, column=0, padx=15, pady=15, sticky="w")
        self.entry_pass = tk.Entry(frame, font=("Times New Roman", 13), width=22, bd=1, relief="solid", show="*")
        self.entry_pass.grid(row=1, column=1, padx=15, pady=15)

        # Botón de inicio de sesión
        self.btn_login = tk.Button(
            self.root,
            text="Iniciar sesión",
            font=("Times New Roman", 13, "bold"),
            bg="#1f2a44",
            fg="white",
            activebackground="#34495e",
            activeforeground="white",
            width=15,
            command=self.verificar_login
        )
        self.btn_login.pack(pady=(20, 10))

        # Permite usar ENTER
        self.entry_pass.bind("<Return>", lambda e: self.verificar_login())

    def verificar_login(self):
        usuario = self.entry_user.get().strip()
        password = self.entry_pass.get().strip()

        if not usuario or not password:
            messagebox.showwarning("Campos vacíos", "Por favor ingresa usuario y contraseña.")
            return

        try:
            db = DatabaseConnection(password="darko")  # tu contraseña de MySQL
            db.conectar()

            query = "SELECT * FROM usuarios WHERE usuario = %s AND password = %s"
            resultado = db.obtener_datos(query, (usuario, password))

            if resultado:
                user = resultado[0]
                messagebox.showinfo("Bienvenido", f"Acceso concedido: {user['nombre']} ({user['rol']})")
                self.root.destroy()
                self.abrir_sistema()
            else:
                messagebox.showerror("Error", "Usuario o contraseña incorrectos.")
            
            db.cerrar()

        except Exception as e:
            messagebox.showerror("Error", f"No se pudo conectar con la base de datos.\n{e}")

    def abrir_sistema(self):
        ventana_principal = tk.Tk()
        sistema_facturacion.SistemaFacturacion(ventana_principal)
        ventana_principal.mainloop()   

if __name__ == "__main__":
    root = tk.Tk()
    app = LoginApp(root)
    root.mainloop()