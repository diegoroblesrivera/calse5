# # explicacion y usa de for

# for i in range(5):
#     print("hola")

# for i in range(5):
#     print(i+1)

# cant=int(input("Ingrese la cant de repeticiones "))

# for i in range(cant):
#     print("repeticion" ,i+1)


# nombre=input("ingrese su nombre")
# edad=input("ingrese su edad")

# print("Hola", nombre, "su edad es", edad)
# print(f"Hola {nombre} su edad es {edad}")


# Escribir = print()
# Leer = input()
# si=if
# para =for

# #tabla de multiplicar, definida por el usuario
# num=int(input("Ingrese un numero"))
# #Escribir i,"x", j, "=",i*j
# for i in range(1,11):
#     print(num,"x", i, "=",i*num)

# # todas las tablas de multiplicar del 1 al 10

# for i in range(1,11):
#     print("Tabla del ", i)
#     for j in range(1,11):
#         print(i,"x", j, "=",i*j)

# # pedir al usuario la cant de notas y promediarlas

# cant=int(input("Ingrese la cantidad de notas"))
# total=0
# notasAzules=0
# for i in range(cant):
#     print("Ingrese la nota ", i+1)
#     nota=float(input())
#     total=total+nota
#     if nota>=4:
#         notasAzules=notasAzules+1
#         # notasAzules+=1
# prom=total/cant

# print(f"Su promedio es {round(prom,1)}")
# print(f"La cantidad de notas sobre 4 fue {notasAzules}")

# if prom>=4:
#     print("el alumno aprobó")    
# else:
#     print("el alumno reprobó")


clave=3344

password=int(input("Ingrese las password :"))

if password==clave:
    print("bienvenido al sistema")
else:
    print("ERROR, clave invalida")


for i in range (3):
    password=int(input("Ingrese las password :"))

    if password==clave:
        print("bienvenido al sistema")
        break
    else:
        print("ERROR, clave invalida")

