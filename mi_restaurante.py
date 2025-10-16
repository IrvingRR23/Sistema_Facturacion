
"""
Sistema de facturación
"""

from tkinter import *
import random, datetime
from tkinter import filedialog, messagebox
from itertools import chain
from time import time as t

nombre_restaurante = "Stack de Sabor"
operador = ''
precios_comidas = [120, 85, 25, 70, 45, 75, 35, 30]
precios_bebidas = [20, 25, 45, 120, 30, 25, 30, 80]
precios_postres = [55, 35, 25, 30, 48, 32, 40, 35]


def click_boton(numero):
    global operador
    operador = operador + numero
    visor_calculadora.delete(0,END)
    visor_calculadora.insert(END, operador)

def borrar():
    global operador
    operador = ''
    visor_calculadora.delete(0,END)

def calcular():
    global operador
    resultado = str(eval(operador))
    visor_calculadora.delete(0,END)
    visor_calculadora.insert(0,resultado)
    operador = ''

def revisar_check():
    x = 0
    for c in cuadros_comida:
        if variables_comida[x].get() == 1:
            cuadros_comida[x].config(state=NORMAL)
            if cuadros_comida[x].get() == '0':
                cuadros_comida[x].delete(0,END)
            cuadros_comida[x].focus()
        else:
            cuadros_comida[x].config(state = DISABLED)
            texto_comida[x].set('0')
        x += 1
    
    x = 0
    for c in cuadros_bebidas:
        if variables_bebidas[x].get() == 1:
            cuadros_bebidas[x].config(state=NORMAL)
            if cuadros_bebidas[x].get() == '0':
                cuadros_bebidas[x].delete(0,END)
            cuadros_bebidas[x].focus()
        else:
            cuadros_bebidas[x].config(state = DISABLED)
            texto_bebidas[x].set('0')
        x += 1
    
    x = 0
    for c in cuadros_postres:
        if variables_postres[x].get() == 1:
            cuadros_postres[x].config(state=NORMAL)
            if cuadros_postres[x].get() == '0':
                cuadros_postres[x].delete(0,END)
            cuadros_postres[x].focus()
        else:
            cuadros_postres[x].config(state = DISABLED)
            texto_postres[x].set('0')
        x += 1

def total():
    sub_total_comida = 0
    p = 0
    for cantidad in texto_comida:
        sub_total_comida = sub_total_comida + (float(cantidad.get()) * precios_comidas[p])
        p += 1

    sub_total_bebida = 0
    p = 0
    for cantidad in texto_bebidas:
        sub_total_bebida = sub_total_bebida + (float(cantidad.get()) * precios_bebidas[p])
        p += 1

    sub_total_postres = 0
    p = 0
    for cantidad in texto_postres:
        sub_total_postres = sub_total_postres + (float(cantidad.get()) * precios_postres[p])
        p += 1

    sub_total = sub_total_comida +sub_total_bebida + sub_total_postres
    propina = sub_total * 0.1 #Llamada impuesto en el codigo
    total = sub_total + propina

    var_costo_comida.set(f"$ {round(sub_total_comida, 2)}")
    var_costo_bebidas.set(f"$ {round(sub_total_bebida, 2)}")
    var_costo_postres.set(f"$ {round(sub_total_postres, 2)}")
    var_subtotal.set(f"$ {round(sub_total, 2)}")
    var_impuestos.set(f"$ {round(propina, 2)}")
    var_total.set(f"$ {round(total, 2)}")

def generar_recibo():
    texto_recibo.config(state="normal")
    texto_recibo.delete("1.0", END)
    num_recibo = f"N° {random.randint(1000,9999)}"
    fecha = datetime.datetime.now()
    fecha_recibo = f"{fecha.day:02d}/{fecha.month:02d}/{fecha.year} {fecha.hour:02d}:{fecha.minute:02d}"
    
    COLS = 44 
    line = lambda ch='-': ch*COLS

    # Encabezado
    try:
        nombre_rest = nombre_restaurante
    except NameError:
        nombre_rest = "Stack de Sabor"
    
    texto_recibo.insert(END, f"{nombre_rest:^{COLS}}\n")
    texto_recibo.insert(END,f"{'Ticket':^{COLS}}\n")
    texto_recibo.insert(END, f"{fecha_recibo:<{COLS-12}}{num_recibo:>12}\n")
    texto_recibo.insert(END, line("=") + "\n")

    texto_recibo.insert(END, f"{'Artículo':<20}{'P.Unit':>9}{' ':1}{'Cant.':>5}{'Importe':>9}\n")


    subtotal = 0

    #---------------- Comidas ----------------
    texto_recibo.insert(END, f"{' Comidas ':=^{COLS}}\n")
    cont = 0
    for comida in texto_comida:
        cantidad_txt = comida.get()
        if cantidad_txt.isdigit() and int(cantidad_txt) > 0:
            cantidad = int(cantidad_txt)
            pu = precios_comidas[cont]
            importe = cantidad * pu
            subtotal += importe
            texto_recibo.insert(END,
                        f"{lista_comidas[cont]:<20}{("$"+format(pu,".2f")):>9}{cantidad:>5}{("$"+format(importe,".2f")):>10}\n"
                        )
        cont += 1

    #---------------- Bebidas ----------------
    texto_recibo.insert(END, f"{' Bebidas ':=^{COLS}}\n")
    cont = 0
    for bebida in texto_bebidas:
        cantidad_txt = bebida.get()
        if cantidad_txt.isdigit() and int(cantidad_txt) > 0:
            cantidad = int(cantidad_txt)
            pu = precios_bebidas[cont]
            importe = cantidad * pu
            subtotal += importe
            texto_recibo.insert(END,
                f"{lista_bebidas[cont]:<20}{("$"+format(pu,".2f")):>9}{cantidad:>5}{("$"+format(importe,".2f")):>10}\n"
                )
        cont += 1
    
    #---------------- Postres ----------------
    texto_recibo.insert(END, f"{' Postres ':=^{COLS}}\n")
    cont = 0
    for postre in texto_postres:
        cantidad_txt = postre.get()
        if cantidad_txt.isdigit() and int(cantidad_txt) > 0:
            cantidad = int(cantidad_txt)
            pu = precios_postres[cont]
            importe = cantidad * pu
            subtotal += importe
            texto_recibo.insert(END,
                f"{lista_postres[cont]:<20}{("$"+format(pu,".2f")):>9}{cantidad:>5}{("$"+format(importe,".2f")):>10}\n"
                )
        cont += 1
    
     # -------- Totales (precios ya incluyen IVA) + Propina --------
    texto_recibo.insert(END, f"\n{' Totales + Propina ':=^{COLS}}\n")
    PROPINA_PCT = 0.10  
    propina = subtotal * 0.1
    total = subtotal + propina

    texto_recibo.insert(END,f"{'Subtotal (incl. IVA):':<30}{("$"+format(subtotal,".2f")):>14}\n")
    texto_recibo.insert(END,f"{('Propina ' +str(int(PROPINA_PCT*100)) + "%:"):<30}{("$"+format(propina,".2f")):>14}\n")
    texto_recibo.insert(END,f"{"Total a pagar: ":<30}{("$"+format(total,".2f")):>14}\n")
    texto_recibo.insert(END,line("=") + "\n")
    texto_recibo.insert(END, f"{'¡Gracias por su compra!':^{COLS}}\n")

    texto_recibo.see("end")

def guardar_recibo():
    info_recibo = texto_recibo.get(1.0,END)

    fecha = datetime.datetime.now()
    nombre_sugerido = f"Recibo_{fecha.year}-{fecha.month:02d}-{fecha.day:02d}_-{fecha.hour:02d}-{fecha.minute:02d}.txt"
    archivo = filedialog.asksaveasfile(
        mode="w",
        defaultextension=".txt",
        initialfile=nombre_sugerido,
        title="Guardar recibo como...",
        filetypes=[("Archivo de texto", "*.txt"), ("Todos los archivos", "*.*")]
    )

    if archivo:
        archivo.write(info_recibo)
        archivo.close()
        messagebox.showinfo("información",f"El recibo fue guardado como:\n{nombre_sugerido}")
    else:
        messagebox.showinfo("Cancelado", f"No se guardó ningun archivo como :\n{nombre_sugerido}")


def limpiar_pantalla():
    texto_recibo.delete(0.1,END)

    for texto in texto_comida:
        texto.set('0')
    for texto in texto_bebidas:
        texto.set('0')
    for texto in texto_postres:
        texto.set('0')
    
    for cuadro in cuadros_comida:
        cuadro.config(state=DISABLED)
    for cuadro in cuadros_bebidas:
        cuadro.config(state=DISABLED)
    for cuadro in cuadros_postres:
        cuadro.config(state=DISABLED)

    for v in variables_comida:
        v.set(0)
    for v in variables_bebidas:
        v.set(0)
    for v in variables_postres:
        v.set(0)

    var_costo_comida.set('')
    var_costo_bebidas.set('')
    var_costo_postres.set('')
    var_impuestos.set('')
    var_subtotal.set('')
    var_total.set('')

def hay_pendiente_vacio(excepto=None):
    """Devuelve el Entry habilitado y vacío (si existe), excluyendo ‘excepto’ = ('tipo', i)."""
    # comidas
    for i, e in enumerate(cuadros_comida):
        if e['state'] == 'normal' and texto_comida[i].get().strip() == '' and excepto != ('comida', i):
            return e
    # bebidas
    for i, e in enumerate(cuadros_bebidas):
        if e['state'] == 'normal' and texto_bebidas[i].get().strip() == '' and excepto != ('bebida', i):
            return e
    # postres
    for i, e in enumerate(cuadros_postres):
        if e['state'] == 'normal' and texto_postres[i].get().strip() == '' and excepto != ('postre', i):
            return e
    return None

def on_toggle(tipo, i):
    """Se llama al marcar/desmarcar. Solo enfoca el que tocaste y bloquea si hay otro vacío."""
    if tipo == 'comida':
        var, entry, txt = variables_comida[i], cuadros_comida[i], texto_comida[i]
    elif tipo == 'bebida':
        var, entry, txt = variables_bebidas[i], cuadros_bebidas[i], texto_bebidas[i]
    else:  # 'postre'
        var, entry, txt = variables_postres[i], cuadros_postres[i], texto_postres[i]

    if var.get() == 1:  # activar
        pendiente = hay_pendiente_vacio(excepto=(tipo, i))
        if pendiente is not None:
            var.set(0)              # no permitas activar otro hasta llenar el pendiente
            pendiente.bell()
            pendiente.focus_set()
            pendiente.selection_range(0, 'end')
            return
        entry.config(state='normal')
        if txt.get() == '0':
            txt.set('')
        entry.focus_set()
        entry.selection_range(0, 'end')
    else:               # desactivar
        entry.config(state='disabled')
        txt.set('0')


# iniciar tkinker
aplicacion = Tk()

#Evitar maximizar
aplicacion.resizable( True, True)

#Titulo de la ventana
aplicacion.title(f"{nombre_restaurante} - Sistema de Facturacion")

#Color de fondo de la ventana 
aplicacion.config(bg="#f5f5f5")

#Panel superior
panel_superior = Frame(aplicacion, bg="#1f2a44", height=72)
panel_superior.pack(side="top", fill="x")

#Titulo
etiqueta_titulo = Label(panel_superior, 
                        text=f"{nombre_restaurante} - Sistema de Facturación", 
                        fg="white",
                        font=("Times New Roman", 40, "bold"), 
                        bg="#1f2a44",
                        anchor="center")
etiqueta_titulo.pack(pady=16, fill="x")

#Panel izquierdo
panel_izquierdo = Frame(aplicacion, bg="#f5f5f5", bd=0)
panel_izquierdo.pack(side="left", fill="both", expand=True, padx= 5, pady= 5)

#Panel costos
panel_costos = LabelFrame(panel_izquierdo, 
                          text="Costos",
                          fg="#333333", 
                          font=("times new roman", 18, "bold"), 
                          bg="#f0f3f6",
                          relief="flat",
                          highlightthickness=1,
                          highlightbackground="#e5e7eb")
panel_costos.pack(side="bottom", fill="x", padx=5, pady=5)

#Panel comida
panel_comida = LabelFrame(panel_izquierdo, 
                          text="Comida",
                          fg="#333333", 
                          font=("times new roman", 14, "bold"), 
                          bg="#ffffff",
                          labelanchor="n",
                          relief="flat",
                          highlightthickness=1,
                          highlightbackground="#e5e7eb")
panel_comida.pack(side="left", fill="both",expand=True, padx=5, pady=5)

#Panel bebidas
panel_bebidas = LabelFrame(panel_izquierdo, 
                          text="Bebidas",
                          fg="#333333", 
                          font=("times new roman", 14, "bold"), 
                          bg="#f5f5f5",
                          labelanchor="n",
                          relief="flat",
                          highlightthickness=1,
                          highlightbackground="#e5e7eb")
panel_bebidas.pack(side="left", fill="both",expand=True, padx=5, pady=5)

#Panel postres
panel_postres = LabelFrame(panel_izquierdo, 
                          text="Postres",
                          fg="#333333", 
                          font=("times new roman", 14, "bold"), 
                          bg="#f5f5f5",
                          labelanchor="n",
                          relief="flat",
                          highlightthickness=1,
                          highlightbackground="#e5e7eb")
panel_postres.pack(side="left", fill="both",expand=True, padx=5, pady=5)

#Panel derecha
panel_derecha = Frame(aplicacion, bg="#f5f5f5", bd=0)
panel_derecha.pack(side="right", fill="both", expand=True, padx=5, pady=5)

#Panel calculadora
panel_calculadora = LabelFrame(panel_derecha, 
                               text="Calculadora",
                               font=("Arial", 14, "bold"),
                               fg="#333333", bg="#ffffff",
                               relief="flat",
                               highlightthickness=1,
                               highlightbackground="#e5e7eb")
panel_calculadora.pack(fill="both", expand=True, padx=5, pady=5)

#Panel recibo
panel_recibo = LabelFrame(panel_derecha, 
                               text="Recibo",
                               font=("Arial", 14, "bold"),
                               fg="#333333", bg="#ffffff",
                               relief="flat",
                               highlightthickness=1,
                               highlightbackground="#e5e7eb")
panel_recibo.pack(fill="both", expand=True, padx=5, pady=5)

#Panel botones
panel_botones = LabelFrame(panel_derecha, 
                               text="Botones",
                               font=("Arial", 14, "bold"),
                               fg="#333333", bg="#ffffff",
                               relief="flat",
                               highlightthickness=1,
                               highlightbackground="#e5e7eb")
panel_botones.pack(fill="both", expand=True, padx=5, pady=5)

#Lista de productos

lista_comidas = ["Pizza","Hamburguesa","Hot Dog","Tacos","Ensalada","Pasta","Sopa","Sandwich"]
lista_bebidas = ["Agua","Refresco","Cerveza","Vino","Café","Té","Jugo","Tequila"]
lista_postres = ["Pastel","Helado","Gelatina","Flan","Pay de Queso","Fruta Picada","Brownie","Cupcake"]

#Generar items en comida
variables_comida = []
cuadros_comida = []
texto_comida = []
contador = 0
for comida in lista_comidas:

    #Crear checkbutton
    variables_comida.append('')
    variables_comida[contador] = IntVar()
    # --- Comidas ---
    comida = Checkbutton(
        panel_comida,
        text=comida.title(),
        font=("times new roman", 13),
        onvalue=1, offvalue=0,
        variable=variables_comida[contador],
        bg="#ffffff", anchor="w",
        selectcolor="#e8f0fe",
        command=lambda i=contador: on_toggle('comida', i)   # <- aquí
    )
    comida.grid(row = contador, column = 0, sticky = W, padx=10, pady=4)

    #Crear los cuadros de entrada
    cuadros_comida.append('')
    texto_comida.append(StringVar(value="0"))
    cuadros_comida[contador] = Entry(panel_comida,
                                     font=("times new roman", 13),
                                     bd = 1, relief="solid",
                                     width=5, justify="center", 
                                     state="disabled",
                                     disabledbackground="#ffffff",  
                                     disabledforeground="#333333",
                                     textvariable=texto_comida[contador])
    cuadros_comida[contador].grid(row = contador,
                                  column=1)
    contador += 1

#Generar items en bebidas
variables_bebidas = []
cuadros_bebidas = []
texto_bebidas = []
contador = 0
for bebidas in lista_bebidas:
    variables_bebidas.append('')
    variables_bebidas[contador] = IntVar()
    # --- Bebidas ---
    bebidas = Checkbutton(
        panel_bebidas,
        text=bebidas.title(),
        font=("times new roman", 13),
        onvalue=1, offvalue=0,
        variable=variables_bebidas[contador],
        bg="#ffffff", anchor="w",
        selectcolor="#e8f0fe",
        command=lambda i=contador: on_toggle('bebida', i)
    )
    bebidas.grid(row = contador, column = 0, sticky = W, padx=10, pady=4)

    #Crear los cuadros de entrada
    cuadros_bebidas.append('')
    texto_bebidas.append(StringVar(value="0"))
    cuadros_bebidas[contador] = Entry(panel_bebidas,
                                     font=("times new roman", 13),
                                     bd=1, relief="solid",         
                                     width=5, justify="center",
                                     state="disabled",
                                     disabledbackground="#ffffff",  
                                     disabledforeground="#333333",
                                     textvariable=texto_bebidas[contador])
    cuadros_bebidas[contador].grid(row = contador, column=1, padx=10, pady=4)

    contador += 1

#Generar items en postres
variables_postres = []
cuadros_postres = []
texto_postres = []
contador = 0
for postres in lista_postres:
    variables_postres.append('')
    variables_postres[contador] = IntVar()
    # --- Postres ---
    postres = Checkbutton(
        panel_postres,
        text=postres.title(),
        font=("times new roman", 13),
        onvalue=1, offvalue=0,
        variable=variables_postres[contador],
        bg="#ffffff", anchor="w",
        selectcolor="#e8f0fe",
        command=lambda i=contador: on_toggle('postre', i)   # <- aquí
    )
    postres.grid(row = contador, column = 0, sticky = W, padx=10, pady=4)
    
    #Crear los cuadros de entrada
    cuadros_postres.append('')
    texto_postres.append(StringVar(value="0"))
    cuadros_postres[contador] = Entry(panel_postres,
                                     font=("times new roman", 13),
                                     bd=1, relief="solid",
                                     width=5, justify="center",
                                     state="disabled",
                                     disabledbackground="#ffffff",
                                     disabledforeground="#333333",
                                     textvariable=texto_postres[contador])
    cuadros_postres[contador].grid(row = contador,
                                  column=1, padx=10, pady=4)
    
    contador += 1

#variables
var_costo_comida = StringVar()
var_costo_bebidas = StringVar()
var_costo_postres = StringVar()
var_subtotal = StringVar()
var_impuestos = StringVar()
var_total = StringVar()

#Etiquetas de costo y campos de entrada
#Costo comida
etiqueta_costo_comida = Label(panel_costos,
                              text="Costo comida",
                              font=("times new roman", 13, "bold"),
                              bg="#f0f3f6",
                              fg="#333333",
                              anchor="w", padx=10
                              )
etiqueta_costo_comida.grid(row=0,column=0,sticky="w", pady=5)

texto_costo_comida = Entry(panel_costos,
                           font=("Times New Roman", 13),
                           width=12, justify="right",
                           bd=1, relief="solid",
                           state="readonly",
                           textvariable=var_costo_comida,
                           disabledbackground="#ffffff",
                           disabledforeground="#333333")
texto_costo_comida.grid(row=0,column=1, padx=10 ,pady=5)

#costo bebida
etiqueta_costo_bebidas = Label(panel_costos,
                              text="Costo bebidas",
                              font=("times new roman", 13, "bold"),
                              bg="#f0f3f6",
                              fg="#333333",
                              anchor="w", padx=10
                              )
etiqueta_costo_bebidas.grid(row=1,column=0,sticky="w", pady=5)

texto_costo_bebidas = Entry(panel_costos,
                           font=("Times New Roman", 13),
                           width=12, justify="right",
                           bd=1, relief="solid",
                           state="readonly",
                           textvariable=var_costo_bebidas,
                           disabledbackground="#ffffff",
                           disabledforeground="#333333")
texto_costo_bebidas.grid(row=1,column=1, padx=10 ,pady=5)

#Costo Postres

etiqueta_costo_postres = Label(panel_costos,
                              text="Costo postres",
                              font=("times new roman", 13, "bold"),
                              bg="#f0f3f6",
                              fg="#333333",
                              anchor="w", padx=10
                              )
etiqueta_costo_postres.grid(row=2,column=0,sticky="w", pady=5)

texto_costo_postres = Entry(panel_costos,
                           font=("Times New Roman", 13),
                           width=12, justify="right",
                           bd=1, relief="solid",
                           state="readonly",
                           textvariable=var_costo_postres,
                           disabledbackground="#ffffff",
                           disabledforeground="#333333")
texto_costo_postres.grid(row=2,column=1, padx=10 ,pady=5)

#Costo Subtotal

etiqueta_subtotal = Label(panel_costos,
                              text="Subtotal",
                              font=("times new roman", 13, "bold"),
                              bg="#f0f3f6",
                              fg="#333333",
                              anchor="w", padx=10
                              )
etiqueta_subtotal.grid(row=0,column=2,sticky="w", pady=5)

texto_subtotal = Entry(panel_costos,
                           font=("Times New Roman", 13),
                           width=12, justify="right",
                           bd=1, relief="solid",
                           state="readonly",
                           textvariable=var_subtotal,
                           disabledbackground="#ffffff",
                           disabledforeground="#333333")
texto_subtotal.grid(row=0,column=3, padx=10 ,pady=5)

#Costo impuestos

etiqueta_impuestos = Label(panel_costos,
                              text="Propina",
                              font=("times new roman", 13, "bold"),
                              bg="#f0f3f6",
                              fg="#333333",
                              anchor="w", padx=10
                              )
etiqueta_impuestos.grid(row=1,column=2,sticky="w", pady=5)

texto_impuestos = Entry(panel_costos,
                           font=("Times New Roman", 13),
                           width=12, justify="right",
                           bd=1, relief="solid",
                           state="readonly",
                           textvariable=var_impuestos,
                           disabledbackground="#ffffff",
                           disabledforeground="#333333")
texto_impuestos.grid(row=1,column=3, padx=10 ,pady=5)

#Costo total

etiqueta_total = Label(panel_costos,
                              text="Total",
                              font=("times new roman", 13, "bold"),
                              bg="#f0f3f6",
                              fg="#333333",
                              anchor="w", padx=10
                              )
etiqueta_total.grid(row=2,column=2,sticky="w", pady=5)

texto_total = Entry(panel_costos,
                           font=("Times New Roman", 13),
                           width=12, justify="right",
                           bd=1, relief="solid",
                           state="readonly",
                           textvariable=var_total,
                           disabledbackground="#ffffff",
                           disabledforeground="#333333")
texto_total.grid(row=2,column=3, padx=10 ,pady=5)

#Construir botones
lista_botones = ["Total","Recibo","Guardar","Resetear"]
botones_creados = []
for i in range(len(lista_botones)):
    panel_botones.grid_columnconfigure(i, weight=1)

columnas = 0

for boton in lista_botones:
    boton = Button(panel_botones,
                   text=boton.title(),
                   font=("Times New Roman", 13, "bold"),
                   bg="#1f2a44",                             
                   fg="white",                               
                   activebackground="#34495e",               
                   activeforeground="white",
                   bd=0,                                     
                   relief="flat",                            
                   padx=20, pady=10,
                   cursor="hand2")
    botones_creados.append(boton)
    boton.grid(row = 0, column = columnas, padx=8, pady=8, sticky="ew")
    columnas += 1

    def on_enter(e, b=boton): 
        b.config(bg="#34495e")
    def on_leave(e, b=boton): 
        b.config(bg="#1f2a44")
    boton.bind("<Enter>", on_enter)
    boton.bind("<Leave>", on_leave)

botones_creados[0].config(command=total)
botones_creados[1].config(command=generar_recibo)
botones_creados[2].config(command=guardar_recibo)
botones_creados[3].config(command=limpiar_pantalla)

texto_recibo = Text(panel_recibo,
                    font=("Courier New", 12),
                    bd=1, relief="solid",
                    bg="#ffffff", fg="#333333",
                    wrap="word"
                    )
texto_recibo.grid(row=0,column=0, sticky="nsew", padx=8, pady=8)

panel_recibo.grid_rowconfigure(0, weight=1)
panel_recibo.grid_columnconfigure(0, weight=1)

#Calculadora
visor_calculadora = Entry(panel_calculadora,
                          font=("Times New Roman", 16, "bold"),
                          justify="right",
                          bd=1, relief="solid",
                          bg="#ffffff", fg="#333333",
                          insertbackground="#1f2a44")
visor_calculadora.grid(row=0, column=0, columnspan=4, sticky="ew", padx=8, pady=(6,10))

for c in range(4):
    panel_calculadora.grid_columnconfigure(c, weight=1)


botones_calculadora = ["7","8","9","+",
                       "4","5","6","-",
                       "1","2","3","*",
                       "CE","Borrar","0","/"]
botones_guardados = []

fila, columna = 1,0
for boton in botones_calculadora:
    # paleta por tipo de boton
    bg, fg, abg, bd, relief = "#f7f9fc", "#1f2a44", "#e9eef7", 1, "solid"  
    if boton in ["+","-","*","/","CE"]:
        bg, fg, abg, bd, relief = "#1f2a44", "white", "#34495e", 0, "flat"  
    elif boton == "Borrar":
        bg, fg, abg, bd, relief = "#8b1d2c", "white", "#a22a3a", 0, "flat"  # borgoña (borrar todo)
    
    boton = Button(panel_calculadora,
                   text=boton.title(),
                   font=("Times New Roman", 13,"bold"),
                   fg=fg,bg=bg,
                    activebackground=abg, activeforeground=fg,
                   bd=bd, relief=relief, cursor="hand2")
    
    botones_guardados.append(boton)

    boton.grid(row=fila,column=columna, sticky="nsew", 
               padx=4, pady=4,ipadx=6, ipady=8)
    
    if columna == 3:
        fila += 1
    
    columna += 1

    if columna == 4:
        columna = 0

botones_guardados[0].config(command=lambda : click_boton('7'))
botones_guardados[1].config(command=lambda : click_boton('8'))
botones_guardados[2].config(command=lambda : click_boton('9'))
botones_guardados[3].config(command=lambda : click_boton('+'))
botones_guardados[4].config(command=lambda : click_boton('4'))
botones_guardados[5].config(command=lambda : click_boton('5'))
botones_guardados[6].config(command=lambda : click_boton('6'))
botones_guardados[7].config(command=lambda : click_boton('-'))
botones_guardados[8].config(command=lambda : click_boton('1'))
botones_guardados[9].config(command=lambda : click_boton('2'))
botones_guardados[10].config(command=lambda : click_boton('3'))
botones_guardados[11].config(command=lambda : click_boton('*'))
botones_guardados[12].config(command=lambda : calcular())
botones_guardados[13].config(command= lambda: borrar())
botones_guardados[14].config(command=lambda : click_boton('0'))
botones_guardados[15].config(command=lambda : click_boton('/'))

#Evitar que se cierre la pantallas

aplicacion.update_idletasks()
w = aplicacion.winfo_reqwidth()
h = aplicacion.winfo_reqheight()
aplicacion.minsize(w, h)                  
aplicacion.geometry(f"{w}x{h}+0+0")      


aplicacion.mainloop()
