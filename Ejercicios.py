"""
from tkinter import ttk
from tkinter import *

import sqlite3

class Productos:
    def __init__(self, root):
        self.wind = root
        self.wind.title("Productos")
        self.wind.geometry("900x600")

        frame1 = LabelFrame(self.wind, text="Información del Producto", font=("Calibri",14))
        frame2 = LabelFrame(self.wind, text="Datos del Producto", font=("Calibri",14))

        frame1.pack(fill="both", expand="yes", padx=20, pady=10)
        frame2.pack(fill="both", expand="yes", padx=20, pady=10)

        self.trv = ttk.Treeview(frame1,columns=(1,2,3,4), show="headings", height="5")
        self.trv.pack()

        self.trv.heading(1, text="ID del Producto")
        self.trv.heading(2, text="Nombre del producto")
        self.trv.heading(3, text="Precio del Producto")
        self.trv.heading(4, text="Cantidad del producto")
    


if __name__ == '__main__':
    root = Tk()
    product = Productos(root)
    root.mainloop()

"""




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





# print("Cosas que quiero probar con github")
# #genial, otro comentario innecesario
# asd = 91
# #str es para concatenar otro tipo de variables que no sean string
# print("La edad de tu gfa: "+str(asd))

# print("Tu mamá es tan gorda que si se cae le da la vuelta al mundo "+str(asd)+" veces")

# #Officia et qui pariatur elit nisi commodo reprehenderit cillum Lorem est.
# print("Culpa qui excepteur ut nisi ullamco nulla non consectetur id culpa incididunt. Deserunt voluptate aliquip laborum minim cupidatat quis amet minim. Ex exercitation amet nostrud sit non proident nisi. Fugiat cillum nulla veniam culpa reprehenderit voluptate dolore incididunt non id sit. Occaecat eu occaecat velit duis labore anim sunt ut laboris veniam elit et sint. Anim laboris aute dolore adipisicing. Aliqua id Lorem ullamco ex minim sit commodo cupidatat ea.")



print("A ver que pasa con los nuevos cambios que voy a hacer")
a,b,c = 10,20,30
print("suma de 10 en 10: "+str(a)+"+10= "+str(b)  )
