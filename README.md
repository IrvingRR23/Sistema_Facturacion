# Sistema de Facturación — *Stack de Sabor*

**Autor:** Irving Rodríguez Rodríguez  
**Lenguaje:** Python 3.11+  
**Interfaz:** Tkinter (GUI nativa de Python)  
**Estado del proyecto:** Completado  

---

##  Descripción general

El **Sistema de Facturación** es una aplicación de escritorio desarrollada en **Python con Tkinter**, diseñada para gestionar pedidos y generar recibos dentro de un restaurante ficticio llamado **“Stack de Sabor”**.

Este programa permite seleccionar alimentos, bebidas y postres mediante casillas interactivas, calcular subtotales, propinas y el total final. Además, genera un **recibo de compra con formato tipo ticket**, el cual puede **guardarse como archivo `.txt`**.

El sistema también incluye una **calculadora integrada**, panel de costos y una interfaz moderna y organizada.

---

## Características principales

| Funcionalidad | Descripción |
|----------------|-------------|
|  **Selección de productos** | Menús de comidas, bebidas y postres con precios configurables |
|  **Cálculo automático** | Calcula subtotales, propina (10%) y total final |
|  **Generación de recibo** | Crea un ticket con formato profesional y datos de fecha/hora |
|  **Guardado de recibos** | Permite exportar el recibo generado en un archivo `.txt` |
|  **Calculadora integrada** | Calculadora funcional con operaciones básicas (`+ - * /`) |
|  **Reinicio de pantalla** | Botón para limpiar todos los campos y comenzar un nuevo pedido |
|  **Interfaz amigable** | Diseño visual claro, con organización en paneles y colores suaves |

---

## Estructura visual de la interfaz

La ventana principal se divide en cuatro secciones principales:

1. **Panel superior** → Título del sistema con el nombre del restaurante.  
2. **Panel izquierdo** → Secciones de *Comidas, Bebidas y Postres*, cada una con checkboxes y campos de cantidad.  
3. **Panel derecho** → Contiene la *Calculadora*, el *Recibo* y los *Botones de acción*.  
4. **Panel inferior (Costos)** → Muestra el desglose de precios: comidas, bebidas, postres, subtotal, propina y total.

---

## Tecnologías y librerías usadas

| Librería | Uso principal |
|-----------|----------------|
| `tkinter` | Creación de la interfaz gráfica |
| `datetime` | Inserción de la fecha y hora del ticket |
| `random` | Generación del número de recibo |
| `filedialog`, `messagebox` | Interacción con el sistema de archivos y notificaciones |
| `itertools` | Manejo de iteraciones para listas de productos |

---

## Ejecución del programa

### Requisitos previos

Asegúrate de tener **Python 3.11 o superior** instalado en tu sistema.  
Puedes verificarlo con el siguiente comando:

```bash
python --version

Instalación y ejecución

Clona el repositorio y ejecuta el archivo principal:
git clone https://github.com/tu_usuario/SistemaFacturacion.git
cd SistemaFacturacion
python sistema_facturacion.py


Ejemplo de uso

Marca las casillas de los productos que el cliente desee.

Especifica la cantidad en los campos habilitados.

Presiona “Total” para calcular los costos.

Presiona “Recibo” para generar el ticket.

Puedes guardar el recibo con “Guardar” o limpiar con “Resetear”.

Ejemplo de salida en el recibo:

               Stack de Sabor
                    Ticket
15/10/2025 18:25          N° 8321
============================================
Artículo             P.Unit Cant.  Importe
============= Comidas =============
Pizza                $120.00    2   $240.00
Tacos                 $70.00    1    $70.00
============= Bebidas =============
Refresco              $25.00    2    $50.00
============= Postres =============
Brownie               $40.00    1    $40.00
============================================
Subtotal (incl. IVA):             $400.00
Propina 10%:                      $40.00
Total a pagar:                   $440.00
============================================
          ¡Gracias por su compra!
