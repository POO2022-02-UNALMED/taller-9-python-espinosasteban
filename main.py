from tkinter import Tk, Button, Entry

# Configuración ventana principal
root = Tk()
root.title("Calculadora POO")
root.resizable(False,False)
root.geometry("265x250")







# Configuración pantalla de salida
pantalla = Entry(root, width=20, bg="black", fg="white", borderwidth=0, font=("arial", 18, "bold"))
pantalla.grid(row=0, column=0, columnspan=4, padx=1, pady=1, sticky= "WE")

def obtener_numero(numero):
    i = len(pantalla.get())
    pantalla.insert(i,numero)
    i += 1

def hacer_operacion(operador):
    i = len(pantalla.get())
    pantalla.insert(i,operador)
    i += 1

def calcular():
    estado_pantalla = pantalla.get()
    resultado = estado_pantalla

    if "*" in estado_pantalla:
        dos_numeros = estado_pantalla.split("*")
        resultado = float(dos_numeros[0]) * float(dos_numeros[1])
    elif "+" in estado_pantalla:
        dos_numeros = estado_pantalla.split("+")
        resultado = float(dos_numeros[0]) + float(dos_numeros[1])
    elif "-" in estado_pantalla:
        dos_numeros = estado_pantalla.split("-")
        resultado = float(dos_numeros[0]) - float(dos_numeros[1])

    elif "/" in estado_pantalla:

        dos_numeros = estado_pantalla.split("/")
        if dos_numeros[1] != 0:
            resultado = float(dos_numeros[0]) / float(dos_numeros[1])
        else:
            pass
    resultado = float(resultado)
    pantalla.delete(0,len(estado_pantalla))
    pantalla.insert(0, str(round(resultado,5)))

# Configuración botones
boton_1 = Button(root, text="1", width=3, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2", command= lambda: obtener_numero(1)).grid(row=1, column=0, padx=2, pady=1, sticky= "WE")
boton_2 = Button(root, text="2", width=3, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2", command= lambda: obtener_numero(2) ).grid(row=1, column=1, padx=1, pady=1,sticky= "WE")
boton_3 = Button(root, text="3", width=3, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2", command= lambda: obtener_numero(3)).grid(row=1, column=2, padx=1, pady=1,sticky= "WE")
boton_4 = Button(root, text="4", width=3, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2", command= lambda: obtener_numero(4)).grid(row=2, column=0, padx=2, pady=1,sticky= "WE")
boton_5 = Button(root, text="5", width=3, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2", command= lambda: obtener_numero(5)).grid(row=2, column=1, padx=1, pady=1,sticky= "WE")
boton_6 = Button(root, text="6", width=3, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2", command= lambda: obtener_numero(6)).grid(row=2, column=2, padx=1, pady=1,sticky= "WE")
boton_7 = Button(root, text="7", width=3, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2",command= lambda: obtener_numero(7)).grid(row=3, column=0, padx=1, pady=1,sticky= "WE")
boton_8 = Button(root, text="8", width=3, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2", command= lambda: obtener_numero(8)).grid(row=3, column=1, padx=1, pady=1,sticky= "WE")
boton_9 = Button(root, text="9", width=3, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2", command= lambda: obtener_numero(9)).grid(row=3, column=2, padx=1, pady=1,sticky= "WE")

boton_igual = Button(root, text="=", width=10, height=3, bg="red", fg="white", borderwidth=0, cursor=" hand2", command= lambda : calcular()).grid(row=4, column=0, columnspan=2, padx=1, pady=1,sticky="WE")
boton_punto = Button(root, text=".", width=3, height=3, bg="spring green", fg="black", cursor="hand2", borderwidth=0, command= lambda: hacer_operacion(".")).grid(row=4, column=2, padx=1, pady=1, sticky="WE")

boton_mas = Button(root, text="+", width=3, height=3, bg="deep sky blue", fg="black", borderwidth=0, cursor="hand2", command= lambda: hacer_operacion("+"), ).grid(row=1, column=3, padx=1, pady=1,sticky="WE")
boton_menos = Button(root, text="-", width=3, height=3, bg="deep sky blue", fg="black", borderwidth=0, cursor="hand2",command= lambda: hacer_operacion("-")).grid(row=2, column=3, padx=1, pady=1,sticky="WE")
boton_multiplicacion = Button(root, text="*",  width=3, height=3, bg="deep sky blue", fg="black", borderwidth=0, cursor="hand2", command= lambda: hacer_operacion("*")).grid(row=3, column=3, padx=1, pady=1,sticky="WE")
boton_division = Button(root, text="/", width=3, height=3, bg="deep sky blue", fg="black", borderwidth=0, cursor="hand2", command= lambda: hacer_operacion("/")).grid(row=4, column=3, padx=1, pady=1,sticky="WE")

root.mainloop()