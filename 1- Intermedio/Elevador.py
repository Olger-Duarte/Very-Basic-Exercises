class Elevator:
    def __init__(self, bottom, top, current):
        # Inicializa la instancia Elevator.
        self.bottom = bottom
        self.top = top
        self.current = current
        print(f"Planta actual: {self.current}")
        
    def min_max(self):
        # Verifica si la planta actual está dentro del rango de plantas permitido.
        if self.current >= self.bottom and self.current <= self.top:
            return True
        elif self.current < self.bottom:
            # Si la planta actual es menor al rango permitido, se mueve a la planta inferior más cercana.
            self.current = self.bottom
            print(f"¡Planta inexistente! Moviendo a la planta más cercana: {self.current}")
            return True 
        elif self.current > self.top:
            # Si la planta actual es mayor al rango permitido, se mueve a la planta superior más cercana.
            self.current = self.top
            print(f"¡Planta inexistente! Moviendo a la planta más cercana: {self.current}")
            return True
            
    def up(self):
        # Mueve el ascensor una planta hacia arriba si se encuentra dentro del rango permitido.
        if self.min_max():
            self.current += 1
            self.min_max()
            print(f"Planta actual (UP): {self.current}")
        
    def down(self):
        # Mueve el ascensor una planta hacia abajo si se encuentra dentro del rango permitido.
        if self.min_max():
            self.current -= 1
            self.min_max()
            print(f"Planta actual (DOWN): {self.current}")
    
    def go_to(self, floor):
        # Mueve el ascensor a la planta especificada si se encuentra dentro del rango permitido.
        if self.min_max():
            self.current = floor
            self.min_max()
        print(f"Planta actual (GoTo): {self.current}")

elevator = Elevator(-1, 10, 0)

elevator.up() 
elevator.down() 
elevator.go_to(10)
