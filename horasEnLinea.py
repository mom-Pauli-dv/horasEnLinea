#Preguntarle el nombre al usuario y saludarlo
name = input("¿Cómo te llamas?")
print("¡Hola, {}!".format(name))

total_hours = 0
lowest_hours = None

#Preguntarle al usuario la cantidad de horas que estuvo en línea cada uno de los últimos 7 días
for i in range(1, 8):
  hours = float(input("¿Cuántas horas estuviste en línea el día {}?: ".format(i)))
  total_hours += hours
  
  #Check if current hours are the lowest hours and store if so
  if lowest_hours == None or hours < lowest_hours:
     lowest_hours = hours
    
print("Estuviste {} horas en línea en total.".format(total_hours))
print("La cantidad mínima de tiempo que estuviste en línea en un día fue {} horas".format(lowest_hours))
