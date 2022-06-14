# #el type() funciona para mostrar el tipo de variable que es una variable
# print(type("Cosas simples"))
# #el + funciona para unir cadenas de texto y en numeros los suma 
# print("bye " + "mundo")

# #Entero
# print(30)
# print(type(30))

# #float o decimales
# print(30.1)
# print(type(30.1))

# #listas
# lista1 = [1,2,3,4]
# print(type(lista1))
# #tuplas, son listas pero que no se pueden cambiar los datos
# dupla1 = (10,20,30,40)
# print(type(dupla1))


# #diccionarios
# diccionario1 = {
#     "Nombre de la persona":"Ryan",
#     "Apellido":"Ray",
#     "Nickname":"oxjleoxo"
# }
# print(type(diccionario1))

# #variable sin datos
# Nada = None
# print(type(Nada))
# #Las variables de python son case sensitive

# #Se pueden guardar varias variables y sus datos a la vez
# x,book = 100,"La caida de Reach"

# #para usar constantes tienes que usar todo el nombre de la variable en mayusculas y generalmente en otro archivo de Python para que así no se pueda cambiar
# GRAVITY = 3.14
# print(type(GRAVITY))

# end="" funciona para evitar que se haga un salto de linea, para cuando se tienen que imprimir varias cosas en la misma linea
# print("Caso de prueba "+str(n4),end="")
# print(":  numero: "+str(n3))





con1=True
while con1 == True:
    try:
        casosDePrueba=int(input("Cantidad de casos de prueba: "))
    except Exception:
        print("No es un número admitido")
    else:
        con1=False
        n4=0
        # n4 = contador de numeros de pruebas -Eliminar al terminar
        while n4<casosDePrueba:
            try:
                n3=int(input("Numero de Prueba "+str(n4+1)+": "))
            except Exception:
                print("No es un numero admitido")
            else:
                n4+=1
                
                i=2
                modulo=2
                print(str(n3)+" = ",end="")

                while modulo > 1:
                    modulo=i%n3
                    
                    if (modulo%i)<1 :
                        i+=1
                    else:
                        
                        n3=round(n3/i)
                        
                        print(" Modulo: "+str(modulo),end="")
                        print(" Resultado: "+str(n3)+", ",end="")    
                print("")    
                    
                # print("Caso de prueba "+str(n4),end="")
                # print(":  numero: "+str(n3))