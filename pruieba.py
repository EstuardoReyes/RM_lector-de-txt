import os 

ruta_carpetas = 'C:/Users/Estuardo Reyes/Desktop/Nueva carpeta/'



def automata():
    state = 0
    nombre =''
    auxiliar = ''
    f = open("Gerardo Lopez.txt", mode = 'r')
        mensaje = f.read()
    while (True):
        linea = archivo.readline()
        x=0
        while x < len(linea):
            actual = linea[x]
            if state == 0: 
                if actual == '\n':
                    state = 1
                    nombre = auxiliar
                    auxiliar = ''
                    x = x + 1
                else:
                    auxiliar = auxiliar + actual
            elif state == 1:
                print(auxiliar)





def buscar_archivos(ruta):
    archivos_texto = []
    archivos = os.listdir(ruta)
    for archivo in archivos:
        if archivo[-4] == ".txt":
            archivos_texto.append(archivo)
    return archivos_texto



nombre_carpetas = os.listdir(ruta_carpetas)
for carpeta in nombre_carpetas:
    ruta = ruta_carpetas + carpeta
    archivos_texto = buscar_archivos(ruta)
    for texto in archivos_texto:
        f = open(ruta + '/' + texto, mode = 'r')
        mensaje = f.read()
        automata(mensaje)