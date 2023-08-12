# Solicitar la hora de inicio al usuario
hora_inicio = int(input("Introduce la hora de inicio (0-23): "))
min_inicio = int(input("Introduce los minutos de inicio (0-59): "))

# Solicitar la duración del evento al usuario
duracion = int(input("Introduce la duración del evento en minutos: "))

# Calcular la hora de finalización
minutos_totales = (hora_inicio * 60) + min_inicio + duracion
hora_final = minutos_totales // 60
min_final = minutos_totales % 60

# Imprimir la hora de finalización
print(f"El evento terminará a las {hora_final}:{min_final:02d}")
