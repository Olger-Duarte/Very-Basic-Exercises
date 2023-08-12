class Node:
    def __init__(self, name):
        self.name = name
        self.parent = None
        self.children = []

class File:
    def __init__(self, name, value=""):
        self.name = name
        self.content = value
        self.parent = None

class Tree:
    def __init__(self):
        self.root = Node("root")
        self.current_node = self.root

    def create_node(self, name):
        new_node = Node(name)
        new_node.parent = self.current_node
        self.current_node.children.append(new_node)

    def create_file(self, name, content=""):
        new_file = File(name, content)
        new_file.parent = self.current_node
        self.current_node.children.append(new_file)

    def insert_value(self, value, file_name, overwrite=False):
        for child in self.current_node.children:
            if isinstance(child, File) and child.name == file_name:
                if overwrite:
                    child.content = value
                    print("Contenido del archivo sobrescrito exitosamente.")
                else:
                    child.content += value
                    print("Valor insertado exitosamente en el archivo.")
                return
        print("Archivo no encontrado.")

    def go_to_parent(self):
        if self.current_node.parent is not None:
            self.current_node = self.current_node.parent
        else:
            print("No hay padre para este nodo.")

    def go_to_child(self, name):
        for child in self.current_node.children:
            if child.name == name:
                if isinstance(child, Node):
                    self.current_node = child
                    return
                else:
                    print("El destino especificado no es un nodo.")
                    return
        print("Nodo no encontrado.")

    def print_content(self, name):
        for child in self.current_node.children:
            if child.name == name:
                if isinstance(child, Node):
                    print(f"Contenido del nodo '{name}':")
                    for sub_child in child.children:
                        if isinstance(sub_child, Node):
                            print(f"-> {sub_child.name} (Nodo)")
                        elif isinstance(sub_child, File):
                            print(f"-> {sub_child.name} (Archivo)")
                    return
                elif isinstance(child, File):
                    print(f"Contenido del archivo '{name}':")
                    print(child.content)
                    return
        print("Nodo o archivo no encontrado.")

    def find_node(self, path):
        path_parts = path.split("/")
        current_node = self.current_node
        for part in path_parts:
            if part == "..":
                if current_node.parent is not None:
                    current_node = current_node.parent
                else:
                    return None
            else:
                found = False
                for child in current_node.children:
                    if child.name == part:
                        current_node = child
                        found = True
                        break
                if not found:
                    return None
        return current_node

    def delete_node(self, path):
        node = self.find_node(path)
        if node is None:
            print("Nodo no encontrado.")
            return
        if node.parent is not None:
            node.parent.children.remove(node)
        else:
            self.root = None

    def print_tree(self, node=None, level=0):
        if node is None:
            node = self.root
        prefix = "  " * level
        if isinstance(node, Node):
            print(f"{prefix}- {node.name} (Nodo)")
        elif isinstance(node, File):
            print(f"{prefix}- {node.name} (Archivo)")
        for child in node.children:
            self.print_tree(child, level + 1)

def show_prompt():
    print("---- Menú ----")
    print("Opciones:")
    print("1. Crear un nodo: mknode name")
    print("2. Crear un archivo: mkfile name")
    print("3. Insertar un valor en un archivo: insert value name")
    print("4. Ver contenido de un nodo o archivo: show name")
    print("5. Ver los nodos hijos del nodo actual: show nodes")
    print("6. Ver la ruta del nodo (desde el primero al actual): show path")
    print("7. Ver todo el árbol: show tree")
    print("8. Ir a un nodo concreto: goto name")
    print("9. Ir al nodo padre: goto ..")
    print("10. Borrar un nodo y todos sus hijos: del name")
    print("11. Salir")
    print("Ingrese su opción:")

show_prompt()

def interact_with_tree():
    tree = Tree()
    while True:
        option = input("\n shell@user: -$ ")
        option_parts = option.split()
        if len(option_parts) == 0:
            print("Opción inválida. Intente de nuevo.")
            continue
        command = option_parts[0].lower()

        match command:
            case "mknode":
                if len(option_parts) >= 2:
                    for part in option_parts[1:]:
                        if "/" in part:
                            path_parts = part.split("/")
                            for path_part in path_parts:
                                tree.create_node(path_part)
                                tree.go_to_child(path_part)
                            tree.go_to_parent()
                        else:
                            tree.create_node(part)
                    print("Nodo(s) creado(s) exitosamente.")
                else:
                    print("Sintaxis inválida. Intente de nuevo.")

            case "mkfile":
                if len(option_parts) == 2:
                    tree.create_file(option_parts[1])
                    print("Archivo creado exitosamente.")
                elif len(option_parts) == 3:
                    file_name = option_parts[1]
                    content = option_parts[2]
                    tree.create_file(file_name, content)
                    print("Archivo creado exitosamente.")
                else:
                    print("Sintaxis inválida. Intente de nuevo.")

            case "insert":
                if len(option_parts) == 3:
                    value = option_parts[1]
                    file_name = option_parts[2]
                    tree.insert_value(value, file_name)
                elif len(option_parts) == 4 and option_parts[3] == "--overwrite":
                    value = option_parts[1]
                    file_name = option_parts[2]
                    tree.insert_value(value, file_name, overwrite=True)
                else:
                    print("Sintaxis inválida. Intente de nuevo.")

            case "show":
                if len(option_parts) == 2:
                    name = option_parts[1]
                    tree.print_content(name)
                else:
                    print("Sintaxis inválida. Intente de nuevo.")

            case "show":
                if len(option_parts) == 2:
                    name = option_parts[1]
                    tree.print_content(name)
                else:
                    print("Sintaxis inválida. Intente de nuevo.")

            case "show":
                if len(option_parts) == 2:
                    name = option_parts[1]
                    tree.print_content(name)
                else:
                    print("Sintaxis inválida. Intente de nuevo.")

            case "show":
                if len(option_parts) == 2:
                    name = option_parts[1]
                    tree.print_content(name)
                else:
                    print("Sintaxis inválida. Intente de nuevo.")

            case "goto":
                if len(option_parts) == 2:
                    name = option_parts[1]
                    if name == "..":
                        tree.go_to_parent()
                    else:
                        tree.go_to_child(name)
                else:
                    print("Sintaxis inválida. Intente de nuevo.")

            case "del":
                if len(option_parts) == 2:
                    name = option_parts[1]
                    tree.delete_node(name)
                    print("Nodo y sus hijos borrados exitosamente.")
                else:
                    print("Sintaxis inválida. Intente de nuevo.")

            case "show":
                if len(option_parts) == 2 and option_parts[1] == "nodes":
                    tree.print_content(tree.current_node.name)
                elif len(option_parts) == 2 and option_parts[1] == "path":
                    node = tree.current_node
                    path = ""
                    while node is not None:
                        path = node.name + "/" + path
                        node = node.parent
                    print("Ruta del nodo:", path[:-1])
                elif len(option_parts) == 2 and option_parts[1] == "tree":
                    print("Árbol completo:")
                    tree.print_tree()
                else:
                    print("Sintaxis inválida. Intente de nuevo.")
            case "help":
                show_prompt()
            case "exit":
                print("Saliendo del programa...")
                break
            case _:
                print("Comando inválido. Intente de nuevo.")

interact_with_tree()
