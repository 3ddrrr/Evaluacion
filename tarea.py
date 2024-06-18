import csv
import time
#menú principal de opciones, para cada una definir una función
def mostrar_menu():
    print("***Datos para la empresa***\n")
    time.sleep(1)
    print("***Menu de opciones***\n")
    time.sleep(1)
    print("1.- Registrar trabajador")
    print("2.- Lista de trabajadores")
    print("3.- Imprimir planilla de trabajadores")
    print("4.- Salir del programa\n")

#pedir datos trabajador y hacer los descuentos de su sueldo
def registrar_trabajador():
    nombre_trabajador=input("Ingrese su nombre y apellido: ")
    cargo=input("Ingrese su cargo (CEO, Analista de datos o Desarrollador): ")
    sueldo_bruto=int(input("Ingrese su sueldo bruto (ej: 999999): $ "))
    descuento_salud=sueldo_bruto*0.07 #Descuento salud (7%)
    descuento_afp=sueldo_bruto*0.12   #Descuento AFP (12%)
    sueldo_liquido=sueldo_bruto-descuento_salud-descuento_afp

#crear archivo donde se almacenarán los datos proporcionados
    matriz=[[nombre_trabajador, cargo, sueldo_bruto, descuento_salud, descuento_afp, sueldo_liquido]]
    with open('Archivo_trabajadores.csv','a', newline='',encoding='utf-8') as archivo_csv: #le cambie la w a la 'a'
        escritor_csv = csv.writer(archivo_csv)
        escritor_csv.writerow(['TRABAJADOR', 'CARGO', 'SUELDO BRUTO', 'DESCUENTO SALUD', 'DESCUENTO AFP', 'SUELDO LÍQUIDO'])
        escritor_csv.writerows(matriz)
    print("Trabajador registrado exitosamente.")

#listar datos
def listar_trabaj():
    try:
        with open('Archivo_trabajadores.csv','r',encoding='utf-8') as archivo_csv:
            lector_csv=csv.reader(archivo_csv)
            for fila in lector_csv:
                print(fila)
    except:
        print("Por ahora no hay trabajadores registrados.")

#imprimir planilla de datos de sueldo
def imprimir_planilla():
    try:
        with open('Archivo_trabajadores.csv','r',encoding='utf-8') as archivo_csv:
            lector_csv=csv.reader(archivo_csv)
            for fila in lector_csv:
                print(fila)
    except:
        print("No hay planilla disponible.")

#añadir a nuestro menú definido, las funciones en cada una de las opciones(1/2/3) 
def main():
    while True:
        mostrar_menu()
        try:
            opcion=int(input("Ingrese una opcion: "))
            if opcion==1:
                print("Eligió opción uno, Registrar Un Trabajador\n")
                registrar_trabajador()
            elif opcion==2:
                print("Eligió opción dos, Lista de los trabajadores\n")
                listar_trabaj()
            elif opcion==3:
                print("Eligió opción tres, Imprimir Planilla de sueldos\n")
                imprimir_planilla()
            elif opcion==4:
                print("Eligió opción cuatro, Saliendo del programa....")
                break
            else:
                print("Opción no válida. Intente nuevamente.\n")
        except ValueError:
            print("Error. Por favor, ingrese un número.\n")
main()


