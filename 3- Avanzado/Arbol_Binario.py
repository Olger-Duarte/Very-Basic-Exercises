class Node:
    def __init__(self, name):
        self.name = name
        self.parent = None
        self.children = []

    def add_child(self, child):
        child.parent = self
        self.children.append(child)
    
    def update_name(self, new_name):
        self.name = new_name

    def remove_child(self, child):
        child.parent = None
        self.children.remove(child)

    def print_all_nodes(self):
        print(self.name)
        for child in self.children:
            if isinstance(child, Node):
                child.print_all_nodes()

class File:
    def __init__(self, name, content=""):
        self.name = name
        self.content = content
        self.parent = None

    def update_content(self, new_content):
        self.content = new_content

    def update_name(self, new_name):
        self.name = new_name

    def delete(self):
        if self.parent:
            self.parent.remove_child(self)


# Creación del árbol binario
root = Node("sysroot")

# Creación de nodos y archivos
folder1 = Node("Folder 1")
folder2 = Node("Folder 2")
folder1_2 = Node("Folder 1.2")
file1 = File("File 1", "ABCDEFG")
file2 = File("File 2", "HIJKLMN")
file3 = File("File 3", "OPQRSTW")

# Construcción del árbol (agregar los nodos/archivos al sistema raiz)
root.add_child(folder1)
root.add_child(folder2)
folder1.add_child(file1)
folder1.add_child(folder1_2)
folder2.add_child(file2)
folder1_2.add_child(file3)

# Lectura de nombres y datos almacenados
print("Nombres de los nodos:")
root.print_all_nodes()

print("\nNombres y contenido de los nodos:")
for child in folder1.children:
    if isinstance(child, File):  # Verificar si el hijo es un objeto de la clase File
        print(f"{child.name}.txt: {child.content}")
    else:
        print(f"{child.name}")

# Actualización de nombres y datos almacenados
folder1.update_name("New Folder 1")
file1.update_name("New File 1")
file2.update_content("New content of File 2")

# Eliminación de un archivo
file1.delete()

# Lectura actualizada de nombres y datos almacenados
print("\nNombres de los nodos después de la actualización:")
root.print_all_nodes()

print("\nNombres y contenido de los nodos después de la eliminación:")
for child in folder1.children:
    if isinstance(child, File):  # Verificar si el hijo es un objeto de la clase File
        print(f"{child.name}.txt: {child.content}")
    else:
        print(f"{child.name}")
