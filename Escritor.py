import openpyxl

productos = []
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
elementos = [3, 'a', 8, 7.2, 'hola']
lista = [1, 8.9, 'hola']
productos.append(numeros)
productos.append(lista)
productos.append(lista)

wb = openpyxl.Workbook()
hoja = wb.active
# Crea la fila del encabezado con los títulos
hoja.append(('Nombre', 'Referencia', 'Stock', 'Precio'))
for producto in productos:
    # producto es una tupla con los valores de un producto 
    hoja.append(producto)
    
wb.save('productos.xlsx')