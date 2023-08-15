# Array de los primeros 27 números primos (cantidad de letras en el abecedario)
primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41,
          43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103]

# Array del abecedario incluyendo minúsculas y mayúsculas (54 valores)
alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
         'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

# Método de encriptación Arohash


def arohash(text):
    # Declaro una lista vacía de strings que luego almacenará el resultado final
    result = []

    # Invierto las palabras en el texto
    words = text.split()
    reversed_words = [word[::-1] for word in words]
    reversed_text = ' '.join(reversed_words)

    # Por cada carácter en el texto invertido...
    for char in reversed_text:

        # Si el carácter es un espacio, se agrega un 0 como valor a la lista result
        if char == ' ':
            result.append('0')

        # Si el carácter es un número, se tomará ese número para seleccionar el número primo correspondiente al índice de la lista primes para luego ser agregado a la lista result
        elif char.isdigit():
            result.append(str(primes[int(char)]))

        # Si el carácter es una letra
        elif char.isalpha():

            # Calculo el índice correspondiente en la lista alpha
            char_index = ord(
                char) - ord('A') if char.isupper() else ord(char) - ord('a')

            # Verifico si el índice está dentro del rango de la lista primes
            if char_index >= 0 and char_index < len(primes):

                # Calculo el valor multiplicando el índice por el número primo correspondiente
                val = char_index * primes[char_index]

                # Corrigo el índice si es mayor o igual que la longitud de primes
                corrected_index = char_index % len(primes)

                # Agrego la letra correspondiente de alpha seguida del valor calculado
                result.append(alpha[corrected_index] + str(val))

    # Retorna el resultado como un string y por cada valor agrego el carácter '-'
    return '-'.join(result)


# Inputs de prueba
input_string_0 = "Hola TIC"
input_string_1 = "ME GUSTA EL ANANA DE NEUQUEN"
input_string_2 = "aaaaa bbbbb ccccc AAAAA BBBBB CCCCC 12345 67890"

output_string = 'Hola TIC -> ' + arohash(input_string_0) + '\n\n' + 'ME GUSTA EL ANANA DE NEUQUEN -> ' + arohash(
    input_string_1) + '\n\n' + "aaaaa bbbbb ccccc AAAAA BBBBB CCCCC 12345 67890 -> " + arohash(input_string_2)

print(output_string)
