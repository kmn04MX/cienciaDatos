from datetime import date
fecha = date.today();

#print("La fecha de hoy es: " + fecha);
#La linea anterior marca error porque se intenta convinar un string con tipo de datos
#Para solucionarlo el tipo de dato se debe convertir a tipo string
#Utilizar la función str para solucionarlo
print("La fecha de hoy es: " + str(fecha))