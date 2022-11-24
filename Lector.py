import os
import openpyxl
import time

ruta_carpetas = 'C:/Users/Estuardo Reyes/Desktop/Nueva carpeta/'
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
    dominio = ''
    antivirus = ''
    actualizado = ''
    usuario = []
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
                    auxiliar = ''
                    x = x + 1
                else:
                    auxiliar = auxiliar + actual 
                    x = x + 1
############################################################################
            elif state == 3: #agrega si tiene opcion a usb
                if actual == '\n':
                    state = 100
                    usb = auxiliar
                    auxiliar = ''
                    x = x + 1
                else:
                    auxiliar = auxiliar + actual 
                    x = x + 1
 ################################################################################
            elif state == 100: #agrega si tiene antivirus
                if actual == '\n':
                    state = 101
                    antivirus = auxiliar
                    auxiliar = ''
                    x = x + 1
                else:
                    auxiliar = auxiliar + actual 
                    x = x + 1  
 ################################################################################
            elif state == 101: #agrega si esta actualizado el antivirus
                if actual == '\n':
                    state = 4
                    actualizado = auxiliar
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
                        auxiliar = ''
                        x = x + 1
                    else:
                        auxiliar = auxiliar + actual
                        x = x + 1
                else:
                    x = x + 1
#######################################################
            elif state == 8: # se encarga de ignorar la palabra serial number
                if actual == '\n' and x > 5:
                    state = 9
                    auxiliar = ''
                    x = x + 1
                else:
                    x = x + 1
    ##################################################################################
            elif state == 9: #agrega el serial
                if x % 2 == 1 and ( x > 3 or ord(actual) != 10 ) :
                    if ord(actual) == 10:
                        state = 10
                        serial = auxiliar
                        auxiliar = ''
                        x = x + 1
                    else:
                        auxiliar = auxiliar + actual
                        x = x + 1
                else:
                    x = x + 1
#######################################################
            elif state == 10: # se encarga de ignorar la palabra ipaddress
                if ord(actual) == 34:
                    state = 11
                    auxiliar = ''
                    x = x + 1
                else:
                    x = x + 1
    ##################################################################################
            elif state == 11: #agrega la ip
                if x % 2 == 1 and ( x > 3 or ord(actual) != 10 ) :
                    if ord(actual) == 34:
                        state = 12
                        ip = auxiliar
                        auxiliar = ''
                        x = x + 1
                    else:
                        auxiliar = auxiliar + actual
                        x = x + 1
                else:
                    x = x + 1
######################################################################################
            elif state == 12:  
                if ord(actual) == 125:
                    state = 13
                    x = x + 1
                else:
                    x = x + 1
#######################################################
            elif state == 13: # se encarga de ignorar la palabra name del procesador
                if ord(actual) == 101:  
                    state = 14
                    auxiliar = ''
                    x = x + 2
                else:
                    x = x + 1
     #######################################################
            elif state == 14: # se encarga de ignorar la palabra name del procesador
                if ord(actual) == 10:
                    state = 15
                    auxiliar = ''
                    x = x + 2
                else:
                    x = x + 1
    ##################################################################################
            elif state == 15: #agrega el modelo del procesador
                if x % 2 == 1 and ( x > 3 or ord(actual) != 10 ) :
                    if ord(actual) == 10:
                        state = 16
                        cpu = auxiliar
                        auxiliar = ''
                        x = x + 1
                    else:
                        auxiliar = auxiliar + actual
                        x = x + 1
                else:
                    x = x + 1
####################################################################################
            elif state == 16:  #agrega   el primer disco duro
                if ord(actual) > 47 and ord(actual) < 58:
                    auxiliar = auxiliar + actual
                    x = x + 1
                elif ord(actual) == 10 and auxiliar != '':
                    state = 17
                    discoDuro = str(int(auxiliar)/1073741824)
                    auxiliar = ''
                    x = x + 1
                else:
                    x = x + 1
###########################################################
            elif state == 17: #verifica si viene otro disco duro o no
                if ord(actual) > 47 and ord(actual) < 58:
                    discoDuro = discoDuro + ",  "
                    state = 18
                elif ord(actual) == 77:
                    state = 19
                    auxiliar = ''
                else:
                    x = x + 1
#####################################################################
            elif state == 18:  #ingresa el otro disco duro
                if ord(actual) > 47 and ord(actual) < 58:
                    auxiliar = auxiliar + actual
                    x = x + 1
                elif ord(actual) == 10 and auxiliar != '':
                    state = 19
                    aux = str(int(auxiliar) / 1073741824)
                    discoDuro = discoDuro + aux
                    auxiliar = ''
                    x = x + 1
                else:
                    x = x + 1
#######################################################################
            elif state == 19: #confirma que lo que viene es la version de windows
                if ord(actual) == 77:
                    state = 20
                else:
                    x = x + 1
#######################################################################################
            elif state == 20 : #agrega la version de windows
                if x % 2 == 1 and ( x > 3 or ord(actual) != 10 ) :
                    if ord(actual) == 10:
                        state = 21
                        windows = auxiliar
                        auxiliar = ''
                        x = x + 1
                    else:
                        auxiliar = auxiliar + actual
                        x = x + 1
                else:
                    x = x + 1
#######################################################
            elif state == 21: # se encarga de ignorar orifinal productkey
                if ord(actual) == 10 and x > 5:
                    state = 22
                    auxiliar = ''
                    x = x + 1
                else:
                    x = x + 1
    ##################################################################################
            elif state == 22: #agrega la licencia de windows
                if x % 2 == 1 and ( x > 3 or ord(actual) != 10 ) :
                    if ord(actual) == 10:
                        state = 23
                        licenciaWindows = auxiliar
                        auxiliar = ''
                        x = x + 1
                    else:
                        auxiliar = auxiliar + actual
                        x = x + 1
                else:
                    x = x + 1
    #####################################################################################
            elif state == 23: #ignora todo hasta agregar el dominio
                if ord(actual) == 61:
                    state = 24
                    x = x + 1 
                else:
                    x = x + 1
    ######################################################################################    
            elif state == 24 : #agrega el dominio
                if x % 2 == 1 and ( x > 3 or ord(actual) != 10 ) :
                    if ord(actual) == 10:
                        state = 25
                        dominio = auxiliar
                        auxiliar = ''
                        x = x + 1
                    else:
                        auxiliar = auxiliar + actual
                        x = x + 1
                else:
                    x = x + 1
#####################################################################################
            elif state == 25: #ignora todo hasta agregar el nombre del equipo
                if ord(actual) == 61:
                    state = 26
                    x = x + 1 
                else:
                    x = x + 1
    ######################################################################################    
            elif state == 26 : #agrega el dominio
                if x % 2 == 1 and ( x > 3 or ord(actual) != 10 ) :
                    if ord(actual) == 10:
                        state = 27
                        nombreEquip = auxiliar
                        auxiliar = ''
                        x = x + 1
                    else:
                        auxiliar = auxiliar + actual
                        x = x + 1
                else:
                    x = x + 1
#####################################################################################
            elif state == 27: #ignora todo hasta agregar el ram
                if ord(actual) == 61:
                    state = 28
                    x = x + 1 
                else:
                    x = x + 1
    ######################################################################################    
            elif state == 28 : #agrega el ram
                if x % 2 == 1 and ( x > 3 or ord(actual) != 10 ) :
                    if ord(actual) == 10:
                        state = 29
                        ram = auxiliar
                        auxiliar = ''
                        x = x + 1
                    else:
                        auxiliar = auxiliar + actual
                        x = x + 1
                else:
                    x = x + 1
#####################################################################################
            elif state == 29: #ignora todo hasta agregar el username
                if ord(actual) == 92:
                    state = 30
                    x = x + 1 
                else:
                    x = x + 1
    ######################################################################################    
            elif state == 30 : #agrega el username
                if x % 2 == 1 and ( x > 3 or ord(actual) != 10 ) :
                    if ord(actual) == 10:
                        userName = auxiliar
                        auxiliar = ''
                        x = x + 1
                        state = 31
                    else:
                        auxiliar = auxiliar + actual
                        x = x + 1
                else:
                    x = x + 1
        #####################################################################################
            elif state == 31:
                x = x + 1
###########################################################################
        if not linea:
            usuario.append(nombre)
            usuario.append(userName)
            usuario.append(nombreEquip)
            usuario.append(ip)
            usuario.append(departamento)
            usuario.append(marca)
            usuario.append(modelo)
            usuario.append(serial)
            usuario.append(windows)
            usuario.append(licenciaWindows)
            usuario.append(antivirus)
            usuario.append(actualizado)
            usuario.append(cpu)
            usuario.append(discoDuro)
            ram = int(ram)/1073741824 
            usuario.append(str(ram))
            usuario.append(usb)
            usuario.append(carpeta)
            usuarios.append(usuario)
            break
    f.close()        

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
    hoja.append(('Responsable', 'Nombre de Usuario','Nombre de Equipo', 'IP', 'Departamento', 'Marca', 'Modelo', 'Serial', 'Sistema Operativo', 'Licencia','Antivirus','Actualizado','CPU', 'Disco Duro', 'RAM', 'USB', 'Carpetas Compartidas?')) # crea los encabezados de los datos
    for producto in usuarios: 
        hoja.append(producto) # agrega los valores de las listas a la hoja de datos
    
    wb.save('BD_USUARIO.xlsx') # guarda la hoja de excel con los datos obtenidos 


nombre_carpetas = os.listdir(ruta_carpetas)
for carpeta in nombre_carpetas:
    ruta = ruta_carpetas + carpeta
    archivos_texto = buscar_archivos(ruta)
    for texto in archivos_texto:
        automata(texto)
crear_excel(usuarios)
    
    
