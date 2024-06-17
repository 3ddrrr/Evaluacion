#Menu de opciones
listaTrabajadores=[]
trabajador=[]
import time

try:
    print("***Datos para la empresa***\n")
    time.sleep(2)
    print("***Menu de opciones***\n")
    time.sleep(2)
    print("1.- Registrar trabajador")
    print("2.- Lista de trabajadores")
    print("3.- Imprimir planilla de trabajadores")
    print("4.- Salir del programa\n")
    opcion=int(input("Ingrese una opcion: "))
    if (opcion==1):
            print("Elijio opcion uno, Registrar Un Trabajador\n")
            import csv
trabajador=[]
lista_cargo=[]
lista_sueldo=[]
while True:
        try:
                nombre_trabajador=input("ingrese su nombre y apellido: ")
                trabajador.append(nombre_trabajador)
                cargo=input("ingrese su cargo(CEO, Analista de datos o Desarrollador): ")
                lista_cargo.append(cargo)
                sueldo_bruto=int(input("ingrese su sueldo bruto(ej:999999): $"))
                lista_sueldo.append(sueldo_bruto)
        if (opcion==2):
            print("Elijio opcion dos, Lista de los trabajadores\n")
        
        if (opcion==3):
            print("Elijio opcion tres, Imprimir Planilla de sueldos\n")
            
        if (opcion==4):
            print("Elijio opcion cuatro, Saliendo del programa....")
        
        except:
              ValueError

matriz=[[nombre_trabajador, cargo, sueldo_bruto]]

        with open('Archivo_trabajadores.csv','w',newline='',encoding='utf-8') as archivo_csv:
            escritor_csv=csv.writer(archivo_csv)
            escritor_csv.writerow(['TRABAJADOR',
                                    'CARGO',
                                    'SUELDO BRUTO',
                                    ])
            escritor_csv.writerows(matriz)
except:
       ValueError
break;






        

   