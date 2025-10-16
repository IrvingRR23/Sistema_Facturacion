import tkinter as tk
from tkinter import ttk, messagebox
import sys, os

# Conexión a base de datos
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from database.database import DatabaseConnection

class CRUDProductos:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestión de Productos - Stack de Sabor")
        self.root.geometry("720x520")
        self.root.config(bg="#f5f5f5")
        self.root.resizable(False, False)

        # Conexión
        self.db = DatabaseConnection(password="darko")
        self.db.conectar()

        # Variables
        self.var_id = None
        self.var_nombre = tk.StringVar()
        self.var_categoria = tk.StringVar()
        self.var_precio = tk.StringVar()
        self.var_filtro = tk.StringVar(value="Todas")

        # TÍTULO
        tk.Label(
            self.root,
            text="Gestión de Productos",
            bg="#1f2a44",
            fg="white",
            font=("Times New Roman", 20, "bold"),
            pady=10
        ).pack(fill="x")

        # FORMULARIO
        form_frame = tk.Frame(self.root, bg="#ffffff", bd=1, relief="solid")
        form_frame.place(x=20, y=70, width=680, height=120)

        tk.Label(form_frame, text="Nombre:", bg="#ffffff", font=("Times New Roman", 13)).grid(row=0, column=0, padx=10, pady=8, sticky="w")
        tk.Entry(form_frame, textvariable=self.var_nombre, font=("Times New Roman", 13), width=22).grid(row=0, column=1, padx=10)

        tk.Label(form_frame, text="Precio:", bg="#ffffff", font=("Times New Roman", 13)).grid(row=0, column=2, padx=10, pady=8, sticky="w")
        tk.Entry(form_frame, textvariable=self.var_precio, font=("Times New Roman", 13), width=15).grid(row=0, column=3, padx=10)

        tk.Label(form_frame, text="Categoría:", bg="#ffffff", font=("Times New Roman", 13)).grid(row=1, column=0, padx=10, pady=8, sticky="w")
        categorias = ["Comida", "Bebida", "Postre"]
        self.combo_categoria = ttk.Combobox(form_frame, textvariable=self.var_categoria, values=categorias, state="readonly", width=20, font=("Times New Roman", 13))
        self.combo_categoria.grid(row=1, column=1, padx=10)

        # BOTONES 
        boton_frame = tk.Frame(self.root, bg="#f5f5f5")
        boton_frame.place(x=20, y=200, width=680, height=50)

        self.btn_agregar = tk.Button(boton_frame, text="Agregar", bg="#1f2a44", fg="white", font=("Times New Roman", 12, "bold"),
                                     width=12, command=self.agregar_producto)
        self.btn_agregar.grid(row=0, column=0, padx=5)

        self.btn_editar = tk.Button(boton_frame, text="Editar", bg="#34495e", fg="white", font=("Times New Roman", 12, "bold"),
                                    width=12, command=self.editar_producto, state="disabled")
        self.btn_editar.grid(row=0, column=1, padx=5)

        self.btn_eliminar = tk.Button(boton_frame, text="Eliminar", bg="#8b1d2c", fg="white", font=("Times New Roman", 12, "bold"),
                                      width=12, command=self.eliminar_producto, state="disabled")
        self.btn_eliminar.grid(row=0, column=2, padx=5)

        tk.Button(boton_frame, text="Refrescar", bg="#1f2a44", fg="white", font=("Times New Roman", 12, "bold"),
                  width=12, command=self.refrescar_vista).grid(row=0, column=3, padx=5)

        tk.Button(boton_frame, text="Limpiar", bg="#555555", fg="white", font=("Times New Roman", 12, "bold"),
                  width=12, command=self.limpiar_campos).grid(row=0, column=4, padx=5)

        # FILTRO
        filtro_frame = tk.Frame(self.root, bg="#f5f5f5")
        filtro_frame.place(x=20, y=255, width=680, height=40)
        tk.Label(filtro_frame, text="Filtrar por categoría:", bg="#f5f5f5", font=("Times New Roman", 13)).pack(side="left", padx=5)
        self.combo_filtro = ttk.Combobox(filtro_frame, textvariable=self.var_filtro, values=["Todas", "Comida", "Bebida", "Postre"],
                                         state="readonly", width=18, font=("Times New Roman", 12))
        self.combo_filtro.pack(side="left", padx=5)
        tk.Button(filtro_frame, text="Filtrar", bg="#34495e", fg="white", font=("Times New Roman", 11, "bold"),
                  width=10, command=self.filtrar_por_categoria).pack(side="left", padx=10)

        # TABLA 
        self.tabla = ttk.Treeview(self.root, columns=("id", "nombre", "categoria", "precio"), show="headings")
        self.tabla.place(x=20, y=300, width=680, height=200)

        self.tabla.heading("id", text="ID")
        self.tabla.heading("nombre", text="Nombre")
        self.tabla.heading("categoria", text="Categoría")
        self.tabla.heading("precio", text="Precio")

        self.tabla.column("id", width=40, anchor="center")
        self.tabla.column("nombre", width=220)
        self.tabla.column("categoria", width=120, anchor="center")
        self.tabla.column("precio", width=100, anchor="center")

        self.tabla.bind("<ButtonRelease-1>", self.seleccionar_fila)

        self.mostrar_productos()

        self.root.lift()
        self.root.focus_force()
        self.root.attributes('-topmost', True)
        self.root.after(100, lambda: self.root.attributes('-topmost', False))

    def mostrar_productos(self):
        for item in self.tabla.get_children():
            self.tabla.delete(item)

        query = "SELECT * FROM productos ORDER BY id ASC"
        datos = self.db.obtener_datos(query)
        if datos:
            for p in datos:
                self.tabla.insert("", "end", values=(p["id"], p["nombre"], p["categoria"], f"${p['precio']:.2f}"))
        self.btn_editar.config(state="disabled")
        self.btn_eliminar.config(state="disabled")

    def refrescar_vista(self):
        """Refresca tabla y mantiene o reinicia el filtro según su estado."""
        categoria = self.var_filtro.get()
        if categoria == "Todas" or not categoria:
            self.var_filtro.set("Todas")
            self.mostrar_productos()
        else:
            self.filtrar_por_categoria()

    def filtrar_por_categoria(self):
        categoria = self.var_filtro.get()
        for item in self.tabla.get_children():
            self.tabla.delete(item)
        if categoria == "Todas" or not categoria:
            self.mostrar_productos()
            return
        query = "SELECT * FROM productos WHERE categoria = %s"
        datos = self.db.obtener_datos(query, (categoria,))
        if datos:
            for p in datos:
                self.tabla.insert("", "end", values=(p["id"], p["nombre"], p["categoria"], f"${p['precio']:.2f}"))

    def agregar_producto(self):
        nombre = self.var_nombre.get().strip()
        categoria = self.var_categoria.get().strip()
        precio = self.var_precio.get().strip()

        if not nombre or not categoria or not precio:
            messagebox.showwarning("Campos vacíos", "Por favor completa todos los campos.")
            return

        try:
            precio = float(precio)
        except ValueError:
            messagebox.showerror("Error", "El precio debe ser numérico.")
            return

        query = "INSERT INTO productos (nombre, categoria, precio) VALUES (%s, %s, %s)"
        if self.db.ejecutar_consulta(query, (nombre, categoria, precio)):
            messagebox.showinfo("Éxito", "Producto agregado correctamente.")
            self.refrescar_vista()
            self.limpiar_campos()

    def seleccionar_fila(self, event):
        item = self.tabla.focus()
        if item:
            valores = self.tabla.item(item, "values")
            self.var_id = valores[0]
            self.var_nombre.set(valores[1])
            self.var_categoria.set(valores[2])
            self.var_precio.set(valores[3].replace("$", "").strip())
            self.btn_editar.config(state="normal")
            self.btn_eliminar.config(state="normal")

    def editar_producto(self):
        if not self.var_id:
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
            messagebox.showerror("Error", "El precio debe ser numérico.")
            return

        query = "UPDATE productos SET nombre=%s, categoria=%s, precio=%s WHERE id=%s"
        if self.db.ejecutar_consulta(query, (nombre, categoria, precio, self.var_id)):
            messagebox.showinfo("Éxito", "Producto actualizado correctamente.")
            self.refrescar_vista()
            self.limpiar_campos()

    def eliminar_producto(self):
        if not self.var_id:
            messagebox.showwarning("Atención", "Selecciona un producto primero.")
            return

        if messagebox.askyesno("Confirmar", "¿Deseas eliminar este producto?"):
            query = "DELETE FROM productos WHERE id=%s"
            if self.db.ejecutar_consulta(query, (self.var_id,)):
                messagebox.showinfo("Eliminado", "Producto eliminado correctamente.")
                self.refrescar_vista()
                self.limpiar_campos()

    def limpiar_campos(self):
        self.var_id = None
        self.var_nombre.set("")
        self.var_categoria.set("")
        self.var_precio.set("")
        self.btn_editar.config(state="disabled")
        self.btn_eliminar.config(state="disabled")

    def __del__(self):
        if self.db:
            self.db.cerrar()


if __name__ == "__main__":
    root = tk.Tk()
    app = CRUDProductos(root)
    root.mainloop()
