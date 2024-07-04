import os
import random
os.system('cls')
personas = []


def grabar_persona():
    while True:
        nombre = input('Ingrese nombre para registrarse: ').lower()
        if len(nombre) <= 7:
            print('El nombre tiene que ser igual o mayor a 8 caracteres')
            continue
        try:
            edad = int(input('Ingrese la edad a registrar: '))
            if edad <= 0:
                print('Edad tiene que ser mayor que 0')
                continue
        except ValueError:
            print('Ingrese un edad mayor que 0')
            continue
              
        nif = input ('Ingrese NIF, ejemplo: (99999999-XXX): ')
        if len (nif) != 12 or not nif[8:].isdigit or not nif[:3].isalpha:
            print('Ingrese un Nif correcto')
            continue
        
        
        persona = {
            'Nombre': nombre,
            'Edad': edad,
            'Nif': nif
        }
            
    
        personas.append(persona)
        print('Registro exitoso')
        break
         

def buscar_persona():
    print('Bienvenido al sistema de busqueda de personas')
    nif_buscado = input('Ingrese el Nif de la persona a buscar: ')
    if nif_buscado.endswith('SP'):
        print('El nif de esta persona es de España')
    else:
        print('Esta persona pertence a la union Europea')
    for x in personas:
        if x['Nif'] == nif_buscado:
            print(x)
            

def imprimir_certificado():
    valor_certificado = random.randint(1500,5000)
    certificado = input('Ingrese certificado a imprimir (Nacimiento -Estado Conyugal - Pertenecia a la union Europea): ').lower()
    if certificado not in ['nacimiento','estado Conyugal','pertenencia a la union europea']:
        print('Eliga un certificado valido')
    else:
        print(f'Certificado: {certificado}')
        print(f'Valor certificado:{valor_certificado}')
        for persona in personas:
            print(persona)   
    
def salir():
    print('Saliendo del programa')
    print('Juan Jesus Llontop Roman')
    print('Version.1')
    exit()


while True:
    print('***************************Bienvenidos al programa de registro************************')
    print('''
          1) Registrar persona
          2) Buscar persona por NIF
          3) Imprimir Cerfificados
          4) Salir
          ''')
    try:
        opc = int(input('Ingrese una opcion: '))
        if opc < 1 or opc > 5:
            print('Ingrese una opcion valida')
    except:
        opc = 0
        
    if opc == 1:
            grabar_persona()      
    elif opc == 2:
            buscar_persona()
    elif opc == 3:
            imprimir_certificado()
    elif opc == 4:
            salir()
    else:
        print('Elija un opcion valida')        
        
        


        













           
