import tkinter as tk
from tkinter import ttk, messagebox
import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from database.database import DatabaseConnection
import Sistema_Funcional.app.sistema_facturacion as sistema_facturacion

class CRUDProductos:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestión de Productos - Stack de Sabor")
        self.root.geometry("700x500")
        self.root.config(bg="#f5f5f5")
        self.root.resizable(False,False)

        self.db = DatabaseConnection(password="darko")
        self.db.conectar()

        self.var_nombre = tk.StringVar()
        self.var_categoria = tk.StringVar()
        self.var_precio = tk.StringVar()

        tk.Label(
            self.root,
            text="Gestión de Productos",
            bg="#1f2a44",
            fg="white",
            font=("Times New Roman", 20, "bold"),
            pady=10
        ).pack(fill="x")
        
        form_frame = tk.Frame(self.root, bg="#ffffff", bd = 1, relief="solid")
        form_frame.place(x=20, y=70, width=660, height=120)

        tk.Label(form_frame, text="Nombre:", bg="#ffffff", font=("Times New Roman", 13)).grid(row=0, column=0, padx=10, pady=10, sticky="w")
        tk.Entry(form_frame, textvariable=self.var_nombre, font=("Times New Roman", 13), width=25).grid(row=0, column=1, padx=10)

        tk.Label(form_frame, text="Categoría:", bg="#ffffff", font=("Times New Roman", 13)).grid(row=1, column=0, padx=10, pady=10, sticky="w")
        categorias = ["Comida", "Bebida", "Postre"]
        ttk.Combobox(form_frame, textvariable=self.var_categoria, values=categorias, state="readonly", width=22, font=("Times New Roman", 13)).grid(row=1, column=1, padx=10)

        tk.Label(form_frame, text="Precio:", bg="#ffffff", font=("Times New Roman", 13)).grid(row=0, column=2, padx=10, pady=10, sticky="w")
        tk.Entry(form_frame, textvariable=self.var_precio, font=("Times New Roman", 13), width=15).grid(row=0, column=3, padx=10)

        # --- Botones ---
        boton_frame = tk.Frame(self.root, bg="#f5f5f5")
        boton_frame.place(x=20, y=200, width=660, height=50)

        tk.Button(boton_frame, text="Agregar", bg="#1f2a44", fg="white", font=("Times New Roman", 12, "bold"), width=12, command=self.agregar_producto).grid(row=0, column=0, padx=5)
        tk.Button(boton_frame, text="Editar", bg="#1f2a44", fg="white", font=("Times New Roman", 12, "bold"), width=12, command=self.editar_producto).grid(row=0, column=1, padx=5)
        tk.Button(boton_frame, text="Eliminar", bg="#8b1d2c", fg="white", font=("Times New Roman", 12, "bold"), width=12, command=self.eliminar_producto).grid(row=0, column=2, padx=5)
        tk.Button(boton_frame, text="Refrescar", bg="#34495e", fg="white", font=("Times New Roman", 12, "bold"), width=12, command=self.mostrar_productos).grid(row=0, column=3, padx=5)

        # --- Tabla de productos ---
        self.tabla = ttk.Treeview(self.root, columns=("id", "nombre", "categoria", "precio"), show="headings")
        self.tabla.place(x=20, y=260, width=660, height=220)

        self.tabla.heading("id", text="ID")
        self.tabla.heading("nombre", text="Nombre")
        self.tabla.heading("categoria", text="Categoría")
        self.tabla.heading("precio", text="Precio")

        self.tabla.column("id", width=50, anchor="center")
        self.tabla.column("nombre", width=200)
        self.tabla.column("categoria", width=120, anchor="center")
        self.tabla.column("precio", width=100, anchor="center")

        self.tabla.bind("<ButtonRelease-1>", self.seleccionar_fila)

        self.mostrar_productos()

    def mostrar_productos(self):
        for item in self.tabla.get_children():
            self.tabla.delete(item)
        query = "SELECT * FROM productos ORDER BY id ASC"
        datos = self.db.obtener_datos(query)
        for p in datos:
            self.tabla.insert("","end", values=(p["id"], p["nombre"], p["categoria"], f"{p['precio']:.2f}"))    
    
    def agregar_productos(self):
        nombre = self.var_nombre.get().strip()
        categoria = self.var_categoria.get.strip()
        precio = self.var_precio.get.strip()

        if not nombre or not categoria or not precio:
            messagebox.showwarning("Campos vacíos", "Por favor completa todos los campos.")
            return
        
        try:
            precio = float(precio)
        except ValueError:
            messagebox.showerror("Error", "El precio debe ser un número válido.")
            return
        
        query = "INSERT TO productos (nombre, categoria, precio) VALUES (%s, %s, %s)"
        if self.db.ejecutar_consulta(query, (nombre, categoria, precio)):
            messagebox.showinfo("Éxito","Producto agregado correctamente.")
            self.mostrar_productos()
            self.limpiar_campos()
    
    def seleccionar_fila(self, event):
        item = self.tabla.focus()
        if item:
            valores = self.tabla.item(item, "values")
            self.var_nombre.set(valores[1])
            self.var_categoria.set(valores[2])
            self.var_precio.set(valores[3]).replace("$","").strip()
            self.id_seleccionado = valores[0]
    
    def editar_producto(self):
        if not hasattr(self, "id_seleccionado"):
            messagebox.showwarning("Atención", "Selecciona un producto primero.")
            return
        
        nombre = self.var_nombre.get().strip()
        categoria = self.var_categoria.get().strip()
        precio = self.var_precio.get().strip()

        if not nombre or not categoria or not precio:
            messagebox.showwarning("Campos vacíos", "Por favor completa todos los campos.")
            return

        try:
            precio = float(precio)
        except ValueError:
            messagebox.showerror("Error","El precio debe ser un número válido.")
            return

        query = "UPDATE productos SET nombre = %s, categoria = %s, precio = %s WHERE id = %s"
        if self.db.ejecutar_consulta(query, (nombre, categoria, precio, self.id_seleccionado)):
            messagebox.showinfo("Éxito", "Producto actualizado correctamente.")
            self.mostrar_productos()
            self.limpiar_campos()

    def eliminar_producto(self):
        if not hasattr(self, "id_seleccionado"):
            messagebox.showwarning("Atención", "Selecciona un producto primero")
            return
    
        if messagebox.askyesno("Confirmar", "¿Deseas eliminar este producto?"):
            query = "DELETE FROM productos WHERE id = %s"
            if self.db.ejecutar_consulta(query, (self.id_seleccionado,)):
                messagebox.showinfo("Eliminado","Producto eliminado correctamente.")
                self.mostrar_productos()
                self.limpiar_campos()
    
    def limpiar_campos(self):
        self.var_nombre.set("")
        self.var_categoria.set("")
        self.var_precio.set("")

    def __del__(self):
        if self.db:
            self.db.cerrar()

if __name__ == "__main__":
    root = tk.Tk()
    app = CRUDProductos(root)
    root.mainloop()