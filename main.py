print("PROGRAMA PARA SOLUCIONAR PROBLEMAS DE PROGRAMACIÓN LINEAL UTILIZANDO EL MÉTODO SIMPLEX")
variables = int(input("¿Cuántas variables varibales tiene tu modelo? "))
restricciones = int(input("Cuántas restricciones tiene tu modelo? "))

encabezados = []                        #creamos los respectivos encabezados en x
for i in range(1, variables + 1):
    encabezados.append(f"x{i}")
for i in range(1, restricciones + 1):
    encabezados.append(f"s{i}")
encabezados.append("Solución:")

laterales = ["Z"]                       #creamos los respectivos encabezados en y
for i in range(1, restricciones + 1):
    laterales.append(f"s{i}")


tabla_inicial = []
funcion_objetivo = []
# (Se eliminan las listas 'funcion_objetivo' y 'restricciones' vacías ya que no se usan)

print("\nIngresa los valores de la tabla:")

# FILA DE LA FUNCIÓN OBJETIVO (Z)
print(f"\nFila '{laterales[0]}':")
fila_z = [] # Usamos fila_z para más claridad
for j in range(len(encabezados)):
        if j < variables:
            # Pide coeficientes de variables originales (deberían ser negativos)
            valor = float(input(f"  {encabezados[j]}    = "))
            fila_z.append(valor)
        elif j < len(encabezados) - 1:
            # Las columnas de holgura (s) son 0 en la fila Z
            fila_z.append(0.0)
        else:
            # Columna de Solución (lado derecho) es 0 en la fila Z
            fila_z.append(0.0)
tabla_inicial.append(fila_z)


# FILAS DE LAS RESTRICCIONES (s1, s2, ...)
for i in range(1, len(laterales)):  # i recorre las filas de s (1 para s1, 2 para s2, etc.)
    fila = []
    # La variable de holgura que corresponde a esta fila es s(i-1)
    indice_s_propia = variables + (i - 1) 
    
    print(f"\nFila '{laterales[i]}':")
    for j in range(len(encabezados)):
        if j < variables:  # variables originales (x1, x2, ...)
            valor = float(input(f"  {encabezados[j]} = "))
            fila.append(valor)
        
        elif j == len(encabezados) - 1:  # columna de solución
            valor = float(input("  Solución = "))
            fila.append(valor)
            
        elif j >= variables and j < len(encabezados) - 1: # columnas de holgura (s1, s2, ...)
            # Esta es la lógica corregida:
            if j == indice_s_propia:  # Si la columna actual (j) es la columna de su propia variable de holgura
                fila.append(1.0)      # Coloca un 1
            else:                     # Si no es su propia columna de holgura
                fila.append(0.0)      # Coloca un 0
                
    tabla_inicial.append(fila)

    

print("\nTABLA INICIAL:\n")
print("       ", end="")
for e in encabezados:
    print(f"{e:^7}", end="")
print()


for i in range(len(laterales)):
    print(f"{laterales[i]:<5} |", end=" ")
    for valor in tabla_inicial[i]:
        # Usamos .2f para una mejor visualización de los decimales
        print(f"{valor:^7.2f}", end="") 
    print()