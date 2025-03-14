"""
Convertir a binario
"""


# Entradas
numero = int(input("Introduce un número: "))

# 2. Si el número es 0, su representación binaria es 0 directamente
if numero == 0:
    print("El número 0 en binario es: 0")
else:
    # 3. Creamos una variable para ir guardando los bits
    binario = ""

    # 4. Guardamos temporalmente el valor original si queremos mostrarlo después
    numero_original = numero

    # 5. Bucle que se ejecuta mientras el número sea mayor que 0
    while numero > 0:
        residuo = numero % 2     # Tomamos el bit menos significativo
        numero = numero // 2     # Dividimos el número por 2
        binario = str(residuo) + binario  # Agregamos el bit al inicio de la cadena

    # 6. Mostramos el resultado
    print(f"El número {numero_original} en binario es: {binario}")
