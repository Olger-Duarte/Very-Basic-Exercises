import re

text = "Aenean vulputate eleifend tellus. Aenean leo ligula, porttitor eu, consequat vitae, eleifend ac, enim. Aliquam lorem ante, dapibus in, viverra quis, feugiat a, tellus. Phasellus viverra nulla ut metus varius laoreet. Quisque rutrum. Aenean imperdiet. Etiam ultricies nisi vel augue. Curabitur ullamcorper ultricies nisi. Nam eget dui. Etiam rhoncus. Maecenas tempus, tellus eget condimentum rhoncus, sem quam semper libero, sit amet adipiscing sem neque sed ipsum."

def countWords(text):
    # Dividir la cadena de texto en palabras utilizando una expresión regular que busque espacios en blanco o signos de puntuación
    words = re.split(r'[.,\/#!$%\^&\*;:{}=\-_`~()?]', text.lower())
    
    # Crear un diccionario para almacenar la frecuencia de cada palabra
    wordCounts = {}

    # Recorrer las palabras y aumentar la frecuencia en el diccionario
    for word in words:
        if word != "":
            if word not in wordCounts:
                wordCounts[word] = 1
            else:
                wordCounts[word] += 1

    return wordCounts

print(countWords(text))
