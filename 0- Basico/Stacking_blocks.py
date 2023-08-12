"""
Tu tarea es escribir un programa que lea la cantidad de bloques que tienen los constructores, 
y generar la altura de la pirámide que se puede construir utilizando estos bloques.

Nota: La altura se mide por el número de capas completas - si los constructores no tienen la cantidad suficiente de bloques 
y no pueden completar la siguiente capa, terminan su trabajo inmediatamente.
"""

def build_blocks(total_blocks):
    used_blocks = 0
    residual_blocks = 0

    for required_block in range(total_blocks):
        used_blocks += required_block
        residual_blocks = total_blocks - used_blocks
        if residual_blocks <= required_block:
            #Los bloques requeridos es equivalente a a la altura, es decir cada nivel requiere la misma cantidad de bloques.
            return str(required_block)
            
    

blocks = int(input("Ingrese el número de bloques: "))

print(f"La altura de la pirámide es: {build_blocks(blocks)}")


