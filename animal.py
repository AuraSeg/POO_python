import animales

#print(animales.gato)

menu = {
    '1':'1. Perro',
    '2':'2. Gato',
    '3':'3. Buho',
    '4':'4. Elefante',
    '5':'5. Oso',
    '0':'0. Exit',
}

class Animal():
    def __init__(self, type):
        self.type = type

    def mostrar_animal(self):
        animal_art = getattr(animales, self.type)
        return animal_art

#Ejecución principal
if __name__ == '__main__':
    for option in menu:
        print(menu.get(option))

    while True:
        user_input = input('Ingresa una opción: ')
        if user_input == '0':
            print('Salir')
            break
        elif user_input in menu:
            menu_value = menu.get(user_input)
            ani=menu_value.split(' ')
            animal=str(ani[1])
            animal_elegido = Animal(animal)
            print(animal_elegido.type)
            print(animal_elegido.mostrar_animal())
        else:
            print('Opción inválida')
