
####Imprimit como un titulo
texto = "temperatures and facts about the moon"
print(texto.title()) 
print("\n-------------------\n")

####Division de una cadena
temperaturas = """Daylight: 260 F
Nighttime: -280 F"""

print(temperaturas.split()) #Separacion de todos las cadenas
print(temperaturas.split('\n')) #Separacion por alguna caracteristica
print("\n-------------------\n")




####Busqueda de cadenas -- Devuelve verdadero o falso
cadena1 = ("Moon" in "This text will describe facts and challenges with space travel")
cadena2 = ("Moon" in "This text will describe facts about the Moon")
print(cadena1)
print(cadena2)

##Buqueda de cadenas por posicion
cadena3 = """Saturn has a daytime temperature of -170 degrees Celsius, while Mars has -28 Celsius."""
print(cadena3.find("has"))

##Busqueda de cadena, este metodo cuenta cuantas veces esta la palabra en la cadena
print(cadena3.count("has"))
print("\n-------------------\n")



####conversion de cadenas
print(cadena3.lower())
print(cadena3.upper())
print("\n-------------------\n")


####Dividiendo la cadena split y usando arr[-1]
temperaturas2 = "Mars Average Temperature: -60 C"
temperaturas2 = temperaturas2.split(":")
print(temperaturas2[-1])
print("\n-------------------\n")




####Recorriendo una cadena
mars_temperature = "The highest temperature on Mars is about 30 C"
for item in mars_temperature.split():
    if item.isnumeric():
        print(item)
#isnumeric() --> comprueba numeros enteros
#isdecimal() --Z compureba numeros decimales
#startswith() --> sirve para detectar el guin de un numero negativo por ejemplo si tenemos -60, esta función separa el guin del numero y después comprueba si es un numero, por ejemplo "-60".startswith('-') esto indicará verdaderp
#endswith() --> compurbeba el ultimo caracter de  una cadena

print("\n-------------------\n")


#### Transforar un teto
temperaturas = "Saturn has a daytime temperature of -170 degrees Celsius, while Mars has -28"
temperaturas = temperaturas.replace("Celsius", "C")
print(temperaturas)

print("\n-------------------\n")


#### unir cadenas con .join()
moon_facts = ["The Moon is drifting away from the Earth.","On average, the Moon is moving about 4cm every year"]
moon_facts = "\n".join(moon_facts) #Une todas las cadenas con un salto de linea
print(moon_facts)



