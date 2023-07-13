# DATES #

from datetime import datetime

#Para trabajar sobre la fecha de ahora mismo, el momento actual:
now = datetime.now()

print(now.year)
print(now.month)
print(now.day)
print(now.hour)
print(now.minute)
print(now.second)

#una marca formato standard para mandar 1 valor q represente un momento especifico, 
# se usa mucho en base de datos, es relativa al horario q le tira el sistema en una zona horaria especifica
timestamp = now.timestamp()

print(timestamp)

#Para trabajar con una fecha/hora que yo defina
# con argumentos de entrada/argumentos por clave:
year_2023 = datetime(2023, 9, 21)

print(year_2023)