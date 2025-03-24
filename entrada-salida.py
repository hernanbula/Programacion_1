#Entradas de string

nombre = input("Ingresa tu nombre: ");
print("Hola " + nombre);
print("Hola ", nombre);

edad = input("Ingresa tu edad: ");
print("Tu edad es " + edad);

# Entradas numericas
numEntero = input("Ingresa un numero entero: ");

#Convertimos (casteamos) el dato ingresado a un número entero con int()
numEntero = int(numEntero);
print("El numero entero que ingresaste es: ", numEntero);

#Pedimos un numero decimal
numDecimal = input("Ingrese un numero decimal: ");

#Convertimos el dato ingresado a un numero decimal (punto flotante) con float()
numDecimal = float(numDecimal); #Ahora la variable tiene un numero decimal
print("El número decimal que ingresaste es: ", numDecimal);

#Ejemplo: operaciones con los numeros ingresados.
suma = numEntero + numDecimal
print("La suma de los dos números es: ", suma);

#f_strings
edad = int(edad);
print("Tu nombre es", nombre, "y tu edad es", edad);
print("Tu nombre es " + nombre + " y tu edad es " + str(edad));
print(f"Tu nombre es {nombre} y tu edad es {edad}");