import datetime, random
from tkinter import *
from tkinter import messagebox, filedialog
from app.crud_productos import CRUDProductos

class SistemaFacturacion:

    def __init__(self, root):
        self.root = root
        self.root.title("Stack de Sabor - Sistema de Facturación")
        self.root.config(bg="#f5f5f5")
        self.root.resizable(True, True)

        self.nombre_restaurante = "Stack de Sabor"
        self.operador = ""
        self.rol_usuario = "admin"

        # Precios de productos
        self.precios_comidas = [120, 85, 25, 70, 45, 75, 35, 30]
        self.precios_bebidas = [20, 25, 45, 120, 30, 25, 30, 80]
        self.precios_postres = [55, 35, 25, 30, 48, 32, 40, 35]

        # Listas de productos
        self.lista_comidas = ["Pizza","Hamburguesa","Hot Dog","Tacos","Ensalada","Pasta","Sopa","Sandwich"]
        self.lista_bebidas = ["Agua","Refresco","Cerveza","Vino","Café","Té","Jugo","Tequila"]
        self.lista_postres = ["Pastel","Helado","Gelatina","Flan","Pay de Queso","Fruta Picada","Brownie","Cupcake"]

        # VARIABLES DINÁMICAS DE COSTO
        self.var_costo_comida = StringVar()
        self.var_costo_bebidas = StringVar()
        self.var_costo_postres = StringVar()
        self.var_subtotal = StringVar()
        self.var_impuestos = StringVar()
        self.var_total = StringVar()

        # VARIABLES DE CANTIDAD / CHECKS
        self.variables_comida = []
        self.variables_bebidas = []
        self.variables_postres = []

        self.texto_comida = []
        self.texto_bebidas = []
        self.texto_postres = []

        self.cuadros_comida = []
        self.cuadros_bebidas = []
        self.cuadros_postres = []

        self.construir_interfaz()

    def construir_interfaz(self):

        # Panel principal (layout de 2 filas y 2 columnas)
        self.panel_principal = Frame(self.root, bg="#f5f5f5")
        self.panel_principal.pack(fill="both", expand=True)

        self.panel_principal.columnconfigure(0, weight=3)
        self.panel_principal.columnconfigure(1, weight=4)
        self.panel_principal.rowconfigure(0, weight=4)
        self.panel_principal.rowconfigure(1, weight=1)

        # 🌟 Panel superior (Título del sistema)
        self.panel_superior = Frame(self.root, bg="#1f2a44", height=80)
        self.panel_superior.pack(side="top", fill="x")

        self.etiqueta_titulo = Label(
            self.panel_superior,
            text=f"{self.nombre_restaurante} - Sistema de Facturación",
            fg="white",
            font=("Times New Roman", 36, "bold"),
            bg="#1f2a44",
            pady=10
        )
        self.etiqueta_titulo.pack(fill="x")

        # Panel superior izquierdo (productos)
        self.panel_izquierdo = Frame(self.panel_principal, bg="#f5f5f5")
        self.panel_izquierdo.grid(row=0, column=0, sticky="nsew", padx=5, pady=5)

        # Panel derecho (calculadora + recibo)
        self.panel_derecha = Frame(self.panel_principal, bg="#f5f5f5")
        self.panel_derecha.grid(row=0, column=1, sticky="nsew", padx=5, pady=5)

        # Panel inferior (costos + botones)
        self.panel_inferior = Frame(self.panel_principal, bg="#f5f5f5")
        self.panel_inferior.grid(row=1, column=0, columnspan=2, sticky="nsew", padx=5, pady=5)
        self.panel_inferior.columnconfigure(0, weight=3)
        self.panel_inferior.columnconfigure(1, weight=2)

        # Subpanel de comidas
        self.crear_panel_comidas()
        self.crear_panel_bebidas()
        self.crear_panel_postres()
        self.crear_panel_costos()
        self.crear_panel_calculadora()
        self.crear_panel_recibo()
        self.crear_panel_botones()

    def crear_panel_comidas(self):
        # Panel de comidas
        self.panel_comida = LabelFrame(
            self.panel_izquierdo,
            text="Comidas",
            fg="#333333",
            font=("Times New Roman", 14, "bold"),
            bg="#ffffff",
            labelanchor="n",
            relief="flat",
            highlightthickness=1,
            highlightbackground="#e5e7eb"
        )
        self.panel_comida.pack(side="left", fill="both", expand=True, padx=5, pady=5)

        # Generar elementos dinámicamente
        for i, nombre in enumerate(self.lista_comidas):
            var = IntVar()
            self.variables_comida.append(var)

            check = Checkbutton(
                self.panel_comida,
                text=nombre.title(),
                font=("Times New Roman", 13),
                onvalue=1,
                offvalue=0,
                variable=var,
                bg="#ffffff",
                anchor="w",
                selectcolor="#e8f0fe",
                command=lambda i=i: self.on_toggle("comida", i)
            )
            check.grid(row=i, column=0, sticky="w", padx=10, pady=4)

            texto = StringVar(value="0")
            self.texto_comida.append(texto)

            entry = Entry(
                self.panel_comida,
                font=("Times New Roman", 13),
                bd=1,
                relief="solid",
                width=5,
                justify="center",
                state="disabled",
                disabledbackground="#ffffff",
                disabledforeground="#333333",
                textvariable=texto
            )
            entry.grid(row=i, column=1)
            self.cuadros_comida.append(entry)

    def crear_panel_bebidas(self):
        #Panel de bebidas
        self.panel_bebidas = LabelFrame(
            self.panel_izquierdo,
            text="Bebidas",
            fg="#333333",
            font=("Times New Roman", 14, "bold"),
            bg="#f5f5f5",
            labelanchor="n",
            relief="flat",
            highlightthickness=1,
            highlightbackground="#e5e7eb"
        )
        self.panel_bebidas.pack(side="left", fill="both", expand=True, padx=5, pady=5)

        #Generar elementos dinamicamente
        for i, nombre in enumerate(self.lista_bebidas):
            var = IntVar()
            self.variables_bebidas.append(var)

            check = Checkbutton(
                self.panel_bebidas,
                text=nombre.title(),
                font=("Times New Roman", 13),
                onvalue=1,
                offvalue=0,
                variable=var,
                bg="#ffffff",
                anchor="w",
                selectcolor="#e8f0fe",
                command=lambda i=i: self.on_toggle("bebida", i)
            )
            check.grid(row=i, column=0, sticky="w", padx=10, pady=4 )

            texto = StringVar(value=0)
            self.texto_bebidas.append(texto)

            entry = Entry(
                self.panel_bebidas,
                font=("Times New Roman", 13),
                bd=1,
                relief="solid",
                width=5,
                justify="center",
                state="disabled",
                disabledbackground="#ffffff",
                disabledforeground="#333333",
                textvariable=texto
            )
            entry.grid(row=i, column=1, padx=10, pady=4)
            self.cuadros_bebidas.append(entry)

    def crear_panel_postres(self):
        # Panel de postres
        self.panel_postres = LabelFrame(
            self.panel_izquierdo,
            text="Postres",
            fg="#333333",
            font=("Times New Roman", 14, "bold"),
            bg="#f5f5f5",
            labelanchor="n",
            relief="flat",
            highlightthickness=1,
            highlightbackground="#e5e7eb"
        )
        self.panel_postres.pack(side="left", fill="both", expand=True, padx=5, pady=5)

        # Generar elementos dinámicamente
        for i, nombre in enumerate(self.lista_postres):
            var = IntVar()
            self.variables_postres.append(var)

            check = Checkbutton(
                self.panel_postres,
                text=nombre.title(),
                font=("Times New Roman", 13),
                onvalue=1,
                offvalue=0,
                variable=var,
                bg="#ffffff",
                anchor="w",
                selectcolor="#e8f0fe",
                command=lambda i=i: self.on_toggle("postre", i)
            )
            check.grid(row=i, column=0, sticky="w", padx=10, pady=4)

            texto = StringVar(value="0")
            self.texto_postres.append(texto)

            entry = Entry(
                self.panel_postres,
                font=("Times New Roman", 13),
                bd=1,
                relief="solid",
                width=5,
                justify="center",
                state="disabled",
                disabledbackground="#ffffff",
                disabledforeground="#333333",
                textvariable=texto
            )
            entry.grid(row=i, column=1, padx=10, pady=4)
            self.cuadros_postres.append(entry) 

    def crear_panel_costos(self):
        # Panel de costos
        self.panel_costos = LabelFrame(
            self.panel_inferior,
            text="Costos",
            fg="#333333",
            font=("Times New Roman", 18, "bold"),
            bg="#f0f3f6",
            relief="flat",
            highlightthickness=1,
            highlightbackground="#e5e7eb"
        )
        self.panel_costos.grid(row=0, column=0, sticky="nsew", padx=5, pady=5)

        # Variables de texto
        self.var_costo_comida = StringVar()
        self.var_costo_bebidas = StringVar()
        self.var_costo_postres = StringVar()
        self.var_subtotal = StringVar()
        self.var_impuestos = StringVar()
        self.var_total = StringVar()

        # Etiquetas y entradas
        etiquetas = ["Costo comida", "Costo bebidas", "Costo postres", "Subtotal", "Propina", "Total"]
        variables = [
            self.var_costo_comida,
            self.var_costo_bebidas,
            self.var_costo_postres,
            self.var_subtotal,
            self.var_impuestos,
            self.var_total
        ]

        # Organización en dos columnas
        for i, (texto, var) in enumerate(zip(etiquetas, variables)):
            fila = i % 3
            col = i // 3 * 2

            etiqueta = Label(
                self.panel_costos,
                text=texto,
                font=("Times New Roman", 13, "bold"),
                bg="#f0f3f6",
                fg="#333333",
                anchor="w",
                padx=10
            )
            etiqueta.grid(row=fila, column=col, sticky="w", pady=5)

            entry = Entry(
                self.panel_costos,
                font=("Times New Roman", 13),
                width=12,
                justify="right",
                bd=1,
                relief="solid",
                state="readonly",
                textvariable=var,
                disabledbackground="#ffffff",
                disabledforeground="#333333"
            )
            entry.grid(row=fila, column=col + 1, padx=10, pady=5)

    def crear_panel_calculadora(self):
        # Panel de calculadora
        self.panel_calculadora = LabelFrame(
            self.panel_derecha,
            text="Calculadora",
            font=("Times New Roman", 14, "bold"),
            fg="#333333",
            bg="#ffffff",
            relief="flat",
            highlightthickness=1,
            highlightbackground="#e5e7eb"
        )
        self.panel_calculadora.pack(fill="both", expand=True, padx=5, pady=5)

        # Visor de la calculadora
        self.visor_calculadora = Entry(
            self.panel_calculadora,
            font=("Times New Roman", 16, "bold"),
            justify="right",
            bd=1,
            relief="solid",
            bg="#ffffff",
            fg="#333333",
            insertbackground="#1f2a44"
        )
        self.visor_calculadora.grid(row=0, column=0, columnspan=4, sticky="ew", padx=8, pady=(6, 10))

        for c in range(4):
            self.panel_calculadora.grid_columnconfigure(c, weight=1)

        # Botones de la calculadora
        botones = [
            "7", "8", "9", "+",
            "4", "5", "6", "-",
            "1", "2", "3", "*",
            "CE", "Borrar", "0", "/"
        ]

        fila, columna = 1, 0
        for texto in botones:
            # Colores por tipo de botón
            bg, fg, abg, bd, relief = "#f7f9fc", "#1f2a44", "#e9eef7", 1, "solid"
            if texto in ["+", "-", "*", "/", "CE"]:
                bg, fg, abg, bd, relief = "#1f2a44", "white", "#34495e", 0, "flat"
            elif texto == "Borrar":
                bg, fg, abg, bd, relief = "#8b1d2c", "white", "#a22a3a", 0, "flat"

            boton = Button(
                self.panel_calculadora,
                text=texto,
                font=("Times New Roman", 13, "bold"),
                fg=fg,
                bg=bg,
                activebackground=abg,
                activeforeground=fg,
                bd=bd,
                relief=relief,
                cursor="hand2",
                command=lambda t=texto: self.evento_calculadora(t)
            )
            boton.grid(row=fila, column=columna, sticky="nsew", padx=4, pady=4, ipadx=6, ipady=8)

            columna += 1
            if columna == 4:
                columna = 0
                fila += 1

    def evento_calculadora(self, texto):
        # Crear operador si no existe
        if not hasattr(self, "operador"):
            self.operador = ""

        if texto == "CE":  # Calcular
            expresion = self.operador.strip()
            try:
                if expresion:
                    resultado = eval(expresion)
                    self.visor_calculadora.delete(0, END)
                    self.visor_calculadora.insert(END, str(resultado))
                    # Reiniciar operador con el resultado actual para nuevas operaciones
                    self.operador = str(resultado)
                else:
                    self.visor_calculadora.delete(0, END)
                    self.visor_calculadora.insert(END, "0")
            except Exception:
                self.visor_calculadora.delete(0, END)
                self.visor_calculadora.insert(END, "Error")
                self.operador = ""
        elif texto == "Borrar":  # Resetear todo
            self.operador = ""
            self.visor_calculadora.delete(0, END)
        else:  # Agregar símbolo o número
            # Si el visor muestra Error o 0, reiniciar
            if self.visor_calculadora.get() in ("Error", "0"):
                self.visor_calculadora.delete(0, END)
                self.operador = ""
            # Añadir el nuevo carácter
            self.operador += texto
            self.visor_calculadora.delete(0, END)
            self.visor_calculadora.insert(END, self.operador)

    def crear_panel_recibo(self):
        # Panel del recibo
        self.panel_recibo = LabelFrame(
            self.panel_derecha,
            text="Recibo",
            font=("Times New Roman", 14, "bold"),
            fg="#333333",
            bg="#ffffff",
            relief="flat",
            highlightthickness=1,
            highlightbackground="#e5e7eb"
        )
        self.panel_recibo.pack(fill="both", expand=True, padx=5, pady=5)

        # Cuadro de texto donde se imprimirá el recibo
        self.texto_recibo = Text(
            self.panel_recibo,
            font=("Courier New", 12),
            bd=1,
            relief="solid",
            bg="#ffffff",
            fg="#333333",
            wrap="word"
        )
        self.texto_recibo.grid(row=0, column=0, sticky="nsew", padx=8, pady=8)

        # Permitir que el Text crezca con la ventana
        self.panel_recibo.grid_rowconfigure(0, weight=1)
        self.panel_recibo.grid_columnconfigure(0, weight=1)

    def crear_panel_botones(self):
        # Panel de botones principales
        self.panel_botones = LabelFrame(
            self.panel_inferior, 
            text="Acciones",
            font=("Times New Roman", 14, "bold"),
            fg="#333333",
            bg="#ffffff",
            relief="flat",
            highlightthickness=1,
            highlightbackground="#e5e7eb"
        )
        self.panel_botones.grid(row=0, column=1, sticky="nsew", padx=5, pady=5)

        # Lista de botones
        botones = ["Total", "Recibo", "Guardar", "Resetear"]
        funciones = [
            self.calcular_total,
            self.generar_recibo,
            self.guardar_recibo,
            self.limpiar_pantalla
        ]

        # Crear y organizar botones
        for i, (texto, comando) in enumerate(zip(botones, funciones)):
            boton = Button(
                self.panel_botones,
                text=texto,
                font=("Times New Roman", 13, "bold"),
                bg="#1f2a44",
                fg="white",
                activebackground="#34495e",
                activeforeground="white",
                bd=0,
                relief="flat",
                padx=20,
                pady=10,
                cursor="hand2",
                command=comando
            )
            boton.grid(row=0, column=i, padx=8, pady=8, sticky="ew")

            # Animación al pasar el cursor
            def on_enter(e, b=boton):
                b.config(bg="#34495e")
            def on_leave(e, b=boton):
                b.config(bg="#1f2a44")

            boton.bind("<Enter>", on_enter)
            boton.bind("<Leave>", on_leave)

            # Ajustar proporción de columnas
            self.panel_botones.grid_columnconfigure(i, weight=1)

        # Botón visible solo para administradores
        if self.rol_usuario == "admin":
            boton_admin = Button(
                self.panel_botones,
                text="Administrar Productos",
                font=("Times New Roman", 13, "bold"),
                bg="#34495e",
                fg="white",
                activebackground="#1f2a44",
                activeforeground="white",
                bd=0,
                relief="flat",
                padx=20,
                pady=10,
                cursor="hand2",
                command=self.abrir_crud_productos
            )
            boton_admin.grid(row=1, column=0, columnspan=4, padx=8, pady=8, sticky="ew")
            
    def calcular_total(self):
        # comidas
        sub_total_comida = 0.0
        for i, cantidad_var in enumerate(self.texto_comida):
            try:
                cant = float(cantidad_var.get() or "0")
            except ValueError:
                cant = 0.0
            sub_total_comida += cant * self.precios_comidas[i]

        # bebidas
        sub_total_bebida = 0.0
        for i, cantidad_var in enumerate(self.texto_bebidas):
            try:
                cant = float(cantidad_var.get() or "0")
            except ValueError:
                cant = 0.0
            sub_total_bebida += cant * self.precios_bebidas[i]

        # postres
        sub_total_postres = 0.0
        for i, cantidad_var in enumerate(self.texto_postres):
            try:
                cant = float(cantidad_var.get() or "0")
            except ValueError:
                cant = 0.0
            sub_total_postres += cant * self.precios_postres[i]

        subtotal = sub_total_comida + sub_total_bebida + sub_total_postres
        propina = subtotal * 0.10
        total = subtotal + propina

        self.var_costo_comida.set(f"$ {sub_total_comida:.2f}")
        self.var_costo_bebidas.set(f"$ {sub_total_bebida:.2f}")
        self.var_costo_postres.set(f"$ {sub_total_postres:.2f}")
        self.var_subtotal.set(f"$ {subtotal:.2f}")
        self.var_impuestos.set(f"$ {propina:.2f}")
        self.var_total.set(f"$ {total:.2f}")

    def generar_recibo(self):
        self.texto_recibo.config(state="normal")
        self.texto_recibo.delete("1.0", "end")

        num_recibo = f"N° {random.randint(1000, 9999)}"
        fecha = datetime.datetime.now()
        fecha_recibo = f"{fecha.day:02d}/{fecha.month:02d}/{fecha.year} {fecha.hour:02d}:{fecha.minute:02d}"

        COLS = 44
        line = lambda ch='-': ch * COLS

        nombre_rest = self.nombre_restaurante or "Stack de Sabor"
        self.texto_recibo.insert("end", f"{nombre_rest:^{COLS}}\n")
        self.texto_recibo.insert("end", f"{'Ticket':^{COLS}}\n")
        self.texto_recibo.insert("end", f"{fecha_recibo:<{COLS-12}}{num_recibo:>12}\n")
        self.texto_recibo.insert("end", line("=") + "\n")
        self.texto_recibo.insert("end", f"{'Artículo':<20}{'P.Unit':>9}{' ':1}{'Cant.':>5}{'Importe':>9}\n")

        subtotal = 0.0

        # Comidas
        self.texto_recibo.insert("end", f"{' Comidas ':=^{COLS}}\n")
        for i, cantidad_var in enumerate(self.texto_comida):
            txt = cantidad_var.get().strip()
            if txt.isdigit() and int(txt) > 0:
                cant = int(txt)
                pu = self.precios_comidas[i]
                imp = cant * pu
                subtotal += imp
                self.texto_recibo.insert(
                    "end",
                    f"{self.lista_comidas[i]:<20}{('$'+format(pu, '.2f')):>9}{cant:>5}{('$'+format(imp,'.2f')):>10}\n"
                )

        # Bebidas
        self.texto_recibo.insert("end", f"{' Bebidas ':=^{COLS}}\n")
        for i, cantidad_var in enumerate(self.texto_bebidas):
            txt = cantidad_var.get().strip()
            if txt.isdigit() and int(txt) > 0:
                cant = int(txt)
                pu = self.precios_bebidas[i]
                imp = cant * pu
                subtotal += imp
                self.texto_recibo.insert(
                    "end",
                    f"{self.lista_bebidas[i]:<20}{('$'+format(pu, '.2f')):>9}{cant:>5}{('$'+format(imp,'.2f')):>10}\n"
                )

        # Postres
        self.texto_recibo.insert("end", f"{' Postres ':=^{COLS}}\n")
        for i, cantidad_var in enumerate(self.texto_postres):
            txt = cantidad_var.get().strip()
            if txt.isdigit() and int(txt) > 0:
                cant = int(txt)
                pu = self.precios_postres[i]
                imp = cant * pu
                subtotal += imp
                self.texto_recibo.insert(
                    "end",
                    f"{self.lista_postres[i]:<20}{('$'+format(pu, '.2f')):>9}{cant:>5}{('$'+format(imp,'.2f')):>10}\n"
                )

        self.texto_recibo.insert("end", f"\n{' Totales + Propina ':=^{COLS}}\n")
        propina_pct = 0.10
        propina = subtotal * propina_pct
        total = subtotal + propina

        self.texto_recibo.insert("end", f"{'Subtotal (incl. IVA):':<30}{('$'+format(subtotal, '.2f')):>14}\n")
        self.texto_recibo.insert("end", f"{('Propina ' + str(int(propina_pct*100)) + '%:'):<30}{('$'+format(propina, '.2f')):>14}\n")
        self.texto_recibo.insert("end", f"{'Total a pagar:':<30}{('$'+format(total, '.2f')):>14}\n")
        self.texto_recibo.insert("end", line("=") + "\n")
        self.texto_recibo.insert("end", f"{'¡Gracias por su compra!':^{COLS}}\n")

        self.texto_recibo.see("end")

    def guardar_recibo(self):
        info_recibo = self.texto_recibo.get("1.0", "end")

        fecha = datetime.datetime.now()
        nombre_sugerido = f"Recibo_{fecha.year}-{fecha.month:02d}-{fecha.day:02d}_Hora-{fecha.hour:02d}-{fecha.minute:02d}.txt"

        archivo = filedialog.asksaveasfile(
            mode="w",
            defaultextension=".txt",
            initialfile=nombre_sugerido,
            title="Guardar recibo como...",
            filetypes=[("Archivo de texto", "*.txt"), ("Todos los archivos", "*.*")]
        )

        if archivo:
            archivo.write(info_recibo)
            ruta = getattr(archivo, "name", nombre_sugerido)
            archivo.close()
            messagebox.showinfo("Información", f"El recibo fue guardado como:\n{ruta}")
        else:
            messagebox.showwarning("Cancelado", f"No se guardó ningún archivo.\nSugerido: {nombre_sugerido}")

    def limpiar_pantalla(self):
        self.texto_recibo.delete("1.0", "end")

        for v in self.texto_comida:
            v.set("0")
        for v in self.texto_bebidas:
            v.set("0")
        for v in self.texto_postres:
            v.set("0")

        for e in self.cuadros_comida:
            e.config(state="disabled")
        for e in self.cuadros_bebidas:
            e.config(state="disabled")
        for e in self.cuadros_postres:
            e.config(state="disabled")

        for v in self.variables_comida:
            v.set(0)
        for v in self.variables_bebidas:
            v.set(0)
        for v in self.variables_postres:
            v.set(0)

        self.var_costo_comida.set("")
        self.var_costo_bebidas.set("")
        self.var_costo_postres.set("")
        self.var_impuestos.set("")
        self.var_subtotal.set("")
        self.var_total.set("")

    def hay_pendiente_vacio(self, excepto=None):
        # comidas
        for i, e in enumerate(self.cuadros_comida):
            if e['state'] == 'normal' and self.texto_comida[i].get().strip() == '' and excepto != ('comida', i):
                return e
        # bebidas
        for i, e in enumerate(self.cuadros_bebidas):
            if e['state'] == 'normal' and self.texto_bebidas[i].get().strip() == '' and excepto != ('bebida', i):
                return e
        # postres
        for i, e in enumerate(self.cuadros_postres):
            if e['state'] == 'normal' and self.texto_postres[i].get().strip() == '' and excepto != ('postre', i):
                return e
        return None

    def on_toggle(self, tipo, i):
        if tipo == 'comida':
            var, entry, txt = self.variables_comida[i], self.cuadros_comida[i], self.texto_comida[i]
        elif tipo == 'bebida':
            var, entry, txt = self.variables_bebidas[i], self.cuadros_bebidas[i], self.texto_bebidas[i]
        else:
            var, entry, txt = self.variables_postres[i], self.cuadros_postres[i], self.texto_postres[i]

        if var.get() == 1:
            pendiente = self.hay_pendiente_vacio(excepto=(tipo, i))
            if pendiente is not None:
                var.set(0)
                pendiente.bell()
                pendiente.focus_set()
                pendiente.selection_range(0, 'end')
                return
            entry.config(state='normal')
            if txt.get() == '0':
                txt.set('')
            entry.focus_set()
            entry.selection_range(0, 'end')
        else:
            entry.config(state='disabled')
            txt.set('0')

    def abrir_crud_productos(self):
        nueva_ventana = Toplevel(self.root)
        CRUDProductos(nueva_ventana)


if __name__ == "__main__":
    root = Tk()
    app = SistemaFacturacion(root)
    root.mainloop()
