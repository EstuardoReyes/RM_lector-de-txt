import os
import openpyxl
import time

ruta_carpetas = 'c:/Users/Estuardo Reyes/Desktop/Nueva carpeta/'
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
    while (True):
        linea = archivo.readline()
        x = 0
        while x < len(linea[x]):
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
            elif state == 4: #ignora la palabra vendor
                if actual == '\n':
                    state = 5
                    usb = auxiliar
                    print(usb)
                    auxiliar = ''
                    x = x + 1
                else:
                    auxiliar = auxiliar + actual 
                    x = x + 1
#######################################################
            elif state == 5: 
                print(actual)
                time.sleep(2)
                if actual == '\n':
                    state = 5
                    nombre = auxiliar
                    auxiliar = ''
                    x = x + 1
                else:
                    auxiliar = auxiliar + actual 
                    x = x + 1
                
                    
                

def buscar_archivos(ruta):
    print("entro a buscar")
    archivos_texto = []
    archivos = os.listdir(ruta)
    for archivo in archivos:
        if archivo[-4] == ".txt":
            archivos_texto.append(archivo)
            print(archivo)
    return archivos_texto

def crear_excel(usuarios):
    wb = openpyxl.Workbook() #crea objeto para trabajar excel
    hoja = wb.active #crea una hoja de datos de excel
    hoja.append(('Nombre', 'Referencia', 'Stock', 'Precio')) # crea los encabezados de los datos
    for producto in usuarios: 
        hoja.append(producto) # agrega los valores de las listas a la hoja de datos
    
    wb.save('BD_USUARIOS.xlsx') # guarda la hoja de excel con los datos obtenidos 


print("iniciando")
nombre_carpetas = os.listdir(ruta_carpetas)
for carpeta in nombre_carpetas:
    print(carpeta)
    ruta = ruta_carpetas + carpeta
    archivos_texto = buscar_archivos(ruta)
    
    for texto in archivos_texto:
        print(texto)
        f = open(ruta+"/"+texto, mode='r')
        mensaje = f.read()
        automata(mensaje)
#crear_excel(usuarios)
    
    
