# Escritura de archivo de texto
with open('my_notes.txt', 'w') as file:
    file.write("Nota 1: Hoy es un día soleado.\n")
    file.write("Nota 2: Recordar comprar leche en el supermercado.\n")
    file.write("Nota 3: Revisar el informe técnico antes de enviarlo.\n")

# Lectura de archivo de texto
with open('my_notes.txt', 'r') as file:
    lines = file.readlines()
    for line in lines:
        print(line.strip())  # strip() elimina los espacios en blanco al principio y al final de la línea
