""" En las plantillas de strings, se pueden usar variables o funciones """

mass_percentage = "1/6"

print(f"On the Moon, you would weigh about {mass_percentage} of your weight on Earth")


print("\n---------------------------------------------\n")

print(f"El siguiente numero por la funciona around es {round(100/6,1)}")


print("\n---------------------------------------------\n")

name = "Ganymede"
planet = "Mars"
gravity = "1.43"
template ="""Gravity Facts about {name}
Planet name: {planet}
Gravity on {name}: {gravity} m/s2
"""

print(template.format(name=name, gravity=gravity, planet = planet))