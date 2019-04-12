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
parser.add_argument("-dr", "--receta", help="dato_receta")
parser.add_argument("-vp", "--vprecalentado", help="valor_precalentado")
parser.add_argument("-vtu", "--tostadouno", help="valor_tostado1")
parser.add_argument("-vfu", "--flamauno", help="valor_flama1")
parser.add_argument("-vtd", "--tostadodos", help="valor_tostado2")
parser.add_argument("-vfd", "--flamados", help="valor_flama2")
parser.add_argument("-ve", "--enfriado", help="valor_enfriado")
parser.add_argument("-tp", "--tprecalentado", help="tiempo_precalentado")
parser.add_argument("-tcf", "--tcmabioflama", help="tiempo_cambio_flama")
parser.add_argument("-ttf", "--ttempfinal", help="tiempo_temp_final")
parser.add_argument("-tt", "--tiempototal", help="tiempo_total")
parser.add_argument("-na", "--nombrearchivo", help="nombre_archivo")
parser.add_argument("-pl", "--pathlogo", help="path_logo")

#Leer los Parámetros
args = parser.parse_args()
dato_fecha = args.fecha
dato_maquina = args.maquina
dato_hora_inicio = args.horai
dato_usuario = args.usuario
dato_hora_final = args.horaf
dato_receta = args.receta
valor_precalentado = args.vprecalentado
valor_tostado1 = args.tostadouno
valor_flama1 = args.flamauno
valor_tostado2 = args.tostadodos
valor_flama2 = args.flamados
valor_enfriado = args.enfriado
tiempo_precalentado = args.tprecalentado
tiempo_cambio_flama = args.tcmabioflama
tiempo_temp_final = args.ttempfinal
tiempo_total = args.tiempototal
nombre_archivo = args.nombrearchivo
path_logo = args.pathlogo

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
pdf.cell(200, 18, 'Reporte de Tostado - Modo Automático', 0, 1, 'C')
pdf.set_line_width(0.5)
pdf.line(pdf.l_margin, 75, pdf.w - pdf.r_margin, 75)

#Sección - Datos Generales
pdf.ln(4)
pdf.set_font("Arial", size=14)
pdf.cell(200, 14, 'Datos Generales', 0, 1, 'C')

valores_generales = [['Fecha:', dato_fecha, 'Máquina:', dato_maquina],
['Hora Inicio:', dato_hora_inicio, 'Usuario:', dato_usuario],
['Hora Fin:', dato_hora_final, 'Receta:', dato_receta]
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

#Sección - Información de la Receta
pdf.ln(14)
pdf.set_font("Arial", size=14)
pdf.cell(200, 14, 'Información de la Receta', 0, 1, 'C')

informacion_receta = [['Precalentado (°C):', valor_precalentado, '', ''],
['Tostado 1 (°C):', valor_tostado1, 'Flama:', valor_flama1],
['Tostado 2 (°C):', valor_tostado2, 'Flama:', valor_flama2],
['Enfriado (min):', valor_enfriado, '', '']
]

pdf.set_font("Arial", size=12)

# La altura de la celda es la misma que el tamaño de fuente
th = pdf.font_size

for row in informacion_receta:
    for datum in row:
        pdf.cell(col_width, th, str(datum), border=1)
    pdf.ln(th)

pdf.set_line_width(0.5)
pdf.line(pdf.l_margin, 160, pdf.w - pdf.r_margin, 160)

#Sección - Tiempos de Proceso
pdf.ln(12)
pdf.set_font("Arial", size=14)
pdf.cell(200, 14, 'Tiempos de Proceso', 0, 1, 'C')

tiempos_proceso = [['', 'Tiempo Precalentado:', tiempo_precalentado, ''],
['', 'Tiempo Cambio Flama:', tiempo_cambio_flama, ''],
['', 'Tiempo Temp Final:', tiempo_temp_final, ''],
['', 'Tiempo Total:', tiempo_total, '']
]

pdf.set_font("Arial", size=12)

# La altura de la celda es la misma que el tamaño de fuente
th = pdf.font_size

for row in tiempos_proceso:
    for datum in row:
        pdf.cell(col_width, th, str(datum), border=0)
    pdf.ln(th)

pdf.set_line_width(0.5)
pdf.line(pdf.l_margin, 198, pdf.w - pdf.r_margin, 198)

#Sección - Gráfica
pdf.ln(6)
pdf.set_font("Arial", size=14)
pdf.cell(200, 14, 'Gráfica', 0, 1, 'C')

user32 = ctypes.windll.user32
width = user32.GetSystemMetrics(0)  # Se obtiene el largo de la pantalla
height = user32.GetSystemMetrics(1)  # Se obtiene el ancho de la pantalla

if width == 800 and height == 600:
    im = pyautogui.screenshot(region=(132, 50, 605, 140))
    im.save('C:\\Scripts\\Python\\temp.png')
    pdf.image('C:\\Scripts\\Python\\temp.png', x=10, y=210, w=196)
    time.sleep(0.1)
    pdf.output(nombre_archivo)
    os.remove('C:\\Scripts\\Python\\temp.png')
else:
    im = pyautogui.screenshot(region=(1012, 305, 605, 140))
    im.save('C:\\Scripts\\Python\\temp.png')
    pdf.image('C:\\Scripts\\Python\\temp.png', x=10, y=210, w=196)
    time.sleep(0.1)
    pdf.output(nombre_archivo)
    os.remove('C:\\Scripts\\Python\\temp.png')

#Abrir el archivo generado
#pdf.output(nombre_archivo)
#os.startfile(filename)