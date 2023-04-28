#Generar un archivo CSV con lo datos de status.txt que nos indica si los trails están abiertos o cerrados
#CSV es la manera de separar los valores en columnas, tener la información más estrucutrada
#El formato del archivo CSV es que debemos elegir las columnas del status, por ejemplo:
#status, blankets_creek, rope_mill
#"open" --> 0, 0
#"closed" --> 1,1
# función set hace que se eliminen los duplicados



#Eliminando las horaciones duplicadas con el método set()
def eliminar_duplicados():
    status_unicos = set ()  

    with open ('./IntroCienciaDatos/status.txt', 'r') as f:
        for line in f.readlines():
            status_unicos.add(line.strip())
    return list(status_unicos) #El set lo convierte a una lista


def imprimir_status(status_unicos):
    for status in status_unicos:
        print(status)

"""Otro problemas son 
 - Algunos delimitadores tienen comas, puntos, signos de admiración/exclamación, de debe hacer una limpieza
"""

#Función para eliminar caracteres
def limpiar_datos(statuses):
    #statuses es una lista de strings que representan los estados de los trails
    status_limpio = []

    for status in statuses:
        linea = status.replace(',', ' ')
        linea = status.replace('?', ' ')
        linea = status.replace('!', ' ')
        linea = status.replace('.', ' ')
        status_limpio.append(linea)
    return status_limpio

#sirve para normalizar datos, es decir, todas a mayusculas o minusculas
def normalizar_datos(statuses):
    status_normalizados = []
    for status in statuses:
        status_normalizados.append(status.lower())
    return status_normalizados

def identificar_status(statuses):
    #status, blankets_creek, rope_mill
    #Regresar status 0, 0
    #status 1,1
    valores = []
    for status in statuses:
        if "all trails are open" in status:
            valores.append([status,1,1])
        elif "all trails are closed" in status:
            valores.append([status, 0.0])
        elif "trails are open" in status:
            valores.append([status,1,1])
        elif "trails are closed" in status:
            valores.append([status,0,0])
        elif "blankets creek is closed" in status and "rope mill is closed" in status:
            valores.append([status,0,0])
        elif "blankets creek is closed" in status and "rope mill is open" in status:
            valores.append([status,0,1])
        elif "blankets creek is open" in status and "rope mill is closed" in status:
            valores.append([status,1,0])
    return valores
    pass

def main():
    status = eliminar_duplicados
    status = limpiar_datos(status)
    status = normalizar_datos(status)
    #status =  identificar_status(status):
    with open('./IntroCienciaDatos/status.csv', 'w') as f:
        import csv
        headers = ['status', 'blankets_creek', 'rope_mill']
        writer = csv.writer(f)
        writer.writerow(headers)
        writer.writerows(identificar_status(status)) 

if __name__ == '__main__': #Se le dice al python, que si se ejecuta de manera directa desde la terminal, vas a ejecutar la función main
    main()