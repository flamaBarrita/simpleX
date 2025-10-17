print("Programa SIMPLEX para la resolución de problemas de programación lineal")
variables = int(input("¿Cuántas variables tiene tu modelo? "))
restricciones = int(input("¿Cuántas restricciones tiene tu modelo? "))

# Crear encabezados y laterales
encabezados = [f"x{i}" for i in range(1, variables + 1)] + \
              [f"s{i}" for i in range(1, restricciones + 1)] + \
              ["Solución"]
laterales = ["Z"] + [f"s{i}" for i in range(1, restricciones + 1)]

tabla = []

# Llenar la función objetivo (se asume maximización, ingresar con signo opuesto)
print("\n-- Función Objetivo (ingresa los coeficientes de la función a maximizar) --")
# Multiplica por -1 para preparar para el algoritmo simplex
fila_z = [float(input(f"  x{i+1}: ")) * -1 for i in range(variables)]
fila_z.extend([0.0] * (restricciones + 1))
tabla.append(fila_z)

# Llenar las restricciones
print("\n-- Restricciones --")
for i in range(restricciones):
    print(f"\nRestricción {i+1}:")
    fila = [float(input(f"  x{j+1}: ")) for j in range(variables)]
    for j in range(restricciones):
        fila.append(1.0 if i == j else 0.0)
    fila.append(float(input("  Solución (lado derecho): ")))
    tabla.append(fila)

def imprimir_tabla():
    print("\n" + "="*70)
    print(f"{'':<6}" + "".join([f"{h:^8}" for h in encabezados]))
    print("-"*(len(encabezados)*8 + 6))
    for i, fila in enumerate(tabla):
        print(f"{laterales[i]:<6}" + "".join([f"{v:^8.2f}" for v in fila]))

print("\nTABLA INICIAL")
imprimir_tabla()

# Inicia el bucle para iterar hasta que no haya negativos en la fila Z
while min(tabla[0][:-1]) < 0:
    
    # Encontrar columna pivote
    fila_z = tabla[0]
    columna_piv = fila_z.index(min(fila_z[:-1]))

    # Encontrar fila pivote
    divisiones = []
    for i in range(1, len(tabla)):
        if tabla[i][columna_piv] > 0:
            divisiones.append(tabla[i][-1] / tabla[i][columna_piv])
        else:
            divisiones.append(float('inf'))
    
    if all(c == float('inf') for c in divisiones):
        print("El problema no tiene solución acotada.")
        quit()
        
    renglon_piv = divisiones.index(min(divisiones)) + 1

    # Actualizar la variable de la base
    laterales[renglon_piv] = encabezados[columna_piv]

    # <-- CORRECCIÓN 1: SE AÑADE EL PASO DE NORMALIZACIÓN FALTANTE -->
    # Primero, se normaliza el renglón pivote para que el elemento pivote sea 1.
    elemento_piv = tabla[renglon_piv][columna_piv]
    for j in range(len(tabla[renglon_piv])):
        tabla[renglon_piv][j] /= elemento_piv

    # <-- CORRECCIÓN 2: LA SIGUIENTE SECCIÓN SE INDENTA PARA ESTAR DENTRO DEL 'WHILE' -->
    # Ahora se hacen ceros en el resto de la columna pivote.
    # Usamos 'i' como el índice del renglón.
    for i in range(len(tabla)):
        # Nos aseguramos de NO modificar el renglón pivote, que ya está listo.
        if i != renglon_piv:
            coef_temp_column = tabla[i][columna_piv]
            # Usamos 'j' como el índice de la columna para recorrer las celdas.
            for j in range(len(tabla[i])):
                valor_renglon_pivote = tabla[renglon_piv][j]
                valor_actual = tabla[i][j]
                # Aplicamos la fórmula y actualizamos la celda.
                tabla[i][j] = valor_actual - (coef_temp_column * valor_renglon_pivote)

    imprimir_tabla()

# Esto se imprimirá solo cuando el bucle 'while' termine correctamente
print("\n\n========= SOLUCIÓN ÓPTIMA ENCONTRADA ==========")
print(f"Valor máximo de Z: {tabla[0][-1]:.2f}")
print("Valores de las variables:")

for var in encabezados[:-1]:
    if var in laterales:
        idx = laterales.index(var)
        print(f"  {var} = {tabla[idx][-1]:.2f}")
    else:
        print(f"  {var} = 0.00")