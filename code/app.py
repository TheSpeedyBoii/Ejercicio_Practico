import os

# List to store personal records
ls_personal = []

def clear_screen():
    """Clears the console screen."""
    os.system("cls" if os.name == "nt" else "clear")

def print_header():
    """Prints program information."""
    clear_screen()
    print('Autor: Jose Agudelo')
    print('Fecha: 2024-05-16')
    print('Version: 1.0')
    print('\n\n')

def register_person():
    """Registers a new person."""
    print_header()
    id = input('ID:  ')
    name = input('Name: ')
    contact = input('Contact: ')
    email = input('Email: ')
    if not id or not name or not contact or not email:
        input('\nDebe diligenciar todos los datos <ENTER>')
    else:
        data = f"{id}    {name}       {contact}     {email}     "
        ls_personal.append(data)
        input(f'\nLa persona {name} ha sido registrada con éxito <ENTER>')

def view_records():
    """Displays all records."""
    print_header()
    print('<<< MODULO VER REGISTROS >>>\n')
    for record in ls_personal:
        print(record)
    input('\n<ENTER>')

def main():
    """Main program loop."""
    while True:
        options = input('<<<<<<<<< Menu Principal >>>>>>>>>\n1. AGREGAR\n2. VER\n3. CONSULTAR\n4. SALIR\n\n')
        if options == '4':
            input('\nFin del programa <ENTER>')
            break
        elif options == '1':
            register_person()
        elif options == '2':
            view_records()

if __name__ == "__main__":
    main()
