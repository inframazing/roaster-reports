import argparse
import ctypes
import datetime
import os
import pyautogui
import time
from fpdf import FPDF

#Generar Parámetros
parser = argparse.ArgumentParser()
parser.add_argument("-df", "--fecha", help="dato_fecha")
parser.add_argument("-dm", "--maquina", help="dato_maquina")
parser.add_argument("-dhi", "--horai", help="dato_hora_inicio")
parser.add_argument("-du", "--usuario", help="dato_usuario")
parser.add_argument("-dhf", "--horaf", help="dato_hora_final")
parser.add_argument("-tt", "--tiempototal", help="tiempo_total")
parser.add_argument("-td", "--tabladatos", help="tabla_datos")
parser.add_argument("-nap", "--nombrearchivop", help="nombre_archivo_pdf")
parser.add_argument("-pl", "--pathlogo", help="path_logo")
parser.add_argument("-nat", "--nombrearchivot", help="nombre_archivo_txt")

#Leer los Parámetros
args = parser.parse_args()
dato_fecha = args.fecha
dato_maquina = args.maquina
dato_hora_inicio = args.horai
dato_usuario = args.usuario
dato_hora_final = args.horaf
tiempo_total = args.tiempototal
tabla_datos = args.tabladatos
nombre_archivo_pdf = args.nombrearchivop
path_logo = args.pathlogo
nombre_archivo_txt = args.nombrearchivot

#Proceso de llenado de PDF
timestamp = datetime.datetime.now().strftime('%d-%m-%Y_%H-%M-%S')
filename = "Prueba_" + timestamp + ".pdf"
pdf = FPDF(format='letter')  # Se crea el objeto
pdf.add_page()  # Se agrega una pagina
epw = pdf.w - 2 * pdf.l_margin  # Ancho de página efectivo
col_width = epw / 4  # Dividir en 4 porciones exactas el ancho de página

#Encabezado
pdf.image(path_logo, x=10, y=10, w=196)  # Se inserta el logo
pdf.set_line_width(0.5)
pdf.line(pdf.l_margin, 55, pdf.w - pdf.r_margin, 55)

#Seccion - Titulo
pdf.ln(46)
pdf.set_font("Arial", size=18)
pdf.cell(200, 18, 'Reporte de Tostado - Modo Manual', 0, 1, 'C')
pdf.set_line_width(0.5)
pdf.line(pdf.l_margin, 75, pdf.w - pdf.r_margin, 75)

#Sección - Datos Generales
pdf.ln(6)
pdf.set_font("Arial", size=14)
pdf.cell(200, 14, 'Datos Generales', 0, 1, 'C')

valores_generales = [['Fecha:', dato_fecha, 'Máquina:', dato_maquina],
['Hora Inicio:', dato_hora_inicio, 'Usuario:', dato_usuario],
['Hora Fin:', dato_hora_final, '', '']
]

pdf.set_font("Arial", size=12)

# La altura de la celda es la misma que el tamaño de fuente
th = pdf.font_size

for row in valores_generales:
    for datum in row:
        pdf.cell(col_width, th, str(datum), border=1)
    pdf.ln(th)

pdf.set_line_width(0.5)
pdf.line(pdf.l_margin, 115, pdf.w - pdf.r_margin, 115)

#Sección - Tiempos de Proceso
pdf.ln(16)
pdf.set_font("Arial", size=14)
pdf.cell(200, 14, 'Tiempos de Proceso', 0, 1, 'C')

tiempos_proceso = [['', 'Tiempo Total:', tiempo_total, '']]

pdf.set_font("Arial", size=12)

# La altura de la celda es la misma que el tamaño de fuente
th = pdf.font_size

for row in tiempos_proceso:
    for datum in row:
        pdf.cell(col_width, th, str(datum), border=0)
    pdf.ln(th)

pdf.set_line_width(0.5)
pdf.line(pdf.l_margin, 150, pdf.w - pdf.r_margin, 150)

#Sección - Gráfica
pdf.ln(16)
pdf.set_font("Arial", size=14)
pdf.cell(200, 14, 'Gráfica', 0, 1, 'C')

user32 = ctypes.windll.user32
width = user32.GetSystemMetrics(0)  # Se obtiene el largo de la pantalla
height = user32.GetSystemMetrics(1)  # Se obtiene el ancho de la pantalla

if width == 800 and height == 600:
    im = pyautogui.screenshot(region=(125, 50, 615, 140))
    im.save('C:\\Scripts\\Python\\temp.png')
    pdf.image('C:\\Scripts\\Python\\temp.png', x=10, y=175, w=196)
    time.sleep(0.2)
elif width == 1366 and height == 768:
    im = pyautogui.screenshot(region=(410, 125, 615, 140))
    im.save('C:\\Scripts\\Python\\temp.png')
    pdf.image('C:\\Scripts\\Python\\temp.png', x=10, y=175, w=196)
    time.sleep(0.2)
else:
    im = pyautogui.screenshot(region=(1005, 305, 615, 140))
    im.save('C:\\Scripts\\Python\\temp.png')
    pdf.image('C:\\Scripts\\Python\\temp.png', x=10, y=175, w=196)
    time.sleep(0.2)

pdf.add_page()  # Se agrega una pagina
pdf.set_font("Arial", size=18)
pdf.cell(200, 18, 'Historial', 0, 1, 'C')
pdf.set_line_width(0.5)
pdf.line(pdf.l_margin, 25, pdf.w - pdf.r_margin, 25)
pdf.ln(6)

with open(nombre_archivo_txt, 'r') as myfile:
    data = myfile.readlines()

for row in data:
    pdf.cell(150, 6.5, row, 1, 1, 'L')

pdf.output(nombre_archivo_pdf)
time.sleep(0.2)
os.remove('C:\\Scripts\\Python\\temp.png')
#Abrir el archivo generado
#os.startfile(nombre_archivo)