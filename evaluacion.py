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
    break



