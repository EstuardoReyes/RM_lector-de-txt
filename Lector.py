import os
import openpyxl
import time

ruta_carpetas = 'D:/Galeria/Escritorio/Nueva carpeta/'
usuarios = []

def automata(archivo):
    state = 0
    auxiliar = ''
    nombre = ''
    nombreEquip = ''
    departamento = ''
    ip = ''
    marca = ''
    modelo = ''
    serial = ''
    cpu = ''
    discoDuro = ''
    ram = ''
    windows= ''
    licenciaWindows = ''
    usb = ''
    carpeta = ''
    userName = ''
    f = open(ruta+"/"+texto, 'r')
    while (True):
        linea = f.readline()
        x = 0
        while x < len(linea):
            actual = linea[x]
            if state == 0:    #agrega el nombre de usuario
                if actual == '\n':
                    state = 1
                    nombre = auxiliar
                    print(nombre)
                    auxiliar = ''
                    x = x + 1
                else:
                    auxiliar = auxiliar + actual 
                    x = x + 1
########################################################################
            elif state == 1:  #agrega el departamento al que pertenece
                if actual == '\n':
                    state = 2
                    departamento = auxiliar
                    print(departamento)
                    auxiliar = ''
                    x = x + 1
                else:
                    auxiliar = auxiliar + actual 
                    x = x + 1
##########################################################################
            elif state == 2: #agrega si tiene carpetas compartidas
                if actual == '\n':
                    state = 3
                    carpeta = auxiliar
                    print(carpeta)
                    auxiliar = ''
                    x = x + 1
                else:
                    auxiliar = auxiliar + actual 
                    x = x + 1
############################################################################
            elif state == 3: #agrega si tiene opcion a usb
                if actual == '\n':
                    state = 4
                    usb = auxiliar
                    print(usb)
                    auxiliar = ''
                    x = x + 1
                else:
                    auxiliar = auxiliar + actual 
                    x = x + 1
#######################################################
            elif state == 4: # se encarga de ignorar la palabra vendor
                if actual == '\n':
                    state = 5
                    auxiliar = ''
                    x = x + 1
                else:
                    x = x + 1
    ##################################################################################
            elif state == 5: #agrega el nombre del constructor del equipo
                if x % 2 == 1 and ( x > 3 or ord(actual) != 10 ) :
                    if ord(actual) == 10:
                        state = 6
                        marca = auxiliar
                        print(marca)
                        x = x + 1
                        auxiliar = ''

                    else:
                        auxiliar = auxiliar + actual
                        x = x + 1
                else:
                    x = x + 1
#######################################################
            elif state == 6: # se encarga de ignorar la palabra name
                if actual == '\n' and x > 5:
                    state = 7
                    auxiliar = ''
                    x = x + 1
                else:
                    x = x + 1
    ##################################################################################
            elif state == 7: #agrega el modelo del equipo
                if x % 2 == 1 and ( x > 3 or ord(actual) != 10 ) :
                    if ord(actual) == 10:
                        state = 8
                        modelo = auxiliar
                        print(modelo)
                        auxiliar = ''
                        x = x + 1
                    else:
                        auxiliar = auxiliar + actual
                        x = x + 1
                else:
                    x = x + 1


                
                    
                

def buscar_archivos(ruta):
    archivos_texto = []
    archivos = os.listdir(ruta)
    for archivo in archivos:
        if archivo[-4] == "." and archivo[-3] == "t" and archivo[-2] == "x" and archivo[-1] == "t":
            archivos_texto.append(archivo)
    return archivos_texto

def crear_excel(usuarios):
    wb = openpyxl.Workbook() #crea objeto para trabajar excel
    hoja = wb.active #crea una hoja de datos de excel
    hoja.append(('Nombre', 'Referencia', 'Stock', 'Precio')) # crea los encabezados de los datos
    for producto in usuarios: 
        hoja.append(producto) # agrega los valores de las listas a la hoja de datos
    
    wb.save('BD_USUARIOS.xlsx') # guarda la hoja de excel con los datos obtenidos 


nombre_carpetas = os.listdir(ruta_carpetas)
for carpeta in nombre_carpetas:
    ruta = ruta_carpetas + carpeta
    archivos_texto = buscar_archivos(ruta)
    for texto in archivos_texto:
        automata(texto)
#crear_excel(usuarios)
    
    
