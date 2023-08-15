# Arohash | Método de encriptación de Ariel Alzogaray Flores

## En el método de encriptación Arohash me valí principalmente del uso de números primos y de la posición de las letras en el abecedario tanto en mínuscula como mayúscula:

1. Invertir las palabras en el texto:
Se Divide el texto en palabras y luego se invierte cada palabra individualmente.

2. Procesar cada carácter del texto invertido:
Se recorre cada carácter en el texto invertido obtenido en el paso anterior.

3. Si el carácter es un espacio:
Si el carácter es un espacio en blanco, se agrega un valor '0' a la lista de resultados.

4. Si el carácter es un número:
Si el carácter es un dígito numérico, se toma ese número para seleccionar el número primo correspondiente al índice en la lista "primes". Luego, ese número primo es convertido en una cadena y agregado a la lista de resultados.

5. Si el carácter es una letra:
Si el carácter es una letra, se calcula el índice correspondiente en la lista "alpha". Si la letra es mayúscula, el índice se calcula en función de su posición en el abecedario en mayúscula, si es minúscula, el índice se calcula en función de su posición en el abecedario en minúscula.

6. Verificación del índice:
Se verifica si el índice calculado está dentro del rango de la lista "primes". Si está dentro del rango, se procede a los siguientes pasos; de lo contrario, el índice se ajusta usando el operador módulo (%).

7. Cálculo del valor:
Se calcula un valor multiplicando el índice por el número primo correspondiente al índice en la lista "primes".

8. Agregar a la lista de resultados:
Se agrega la letra correspondiente de la lista "alpha" seguida del valor calculado (obtenido en el paso 7) a la lista de resultados.

9. Retorno del resultado:
El resultado final se obtiene al unir todos los elementos de la lista de resultados con el carácter '-' y se devuelve como una cadena.
