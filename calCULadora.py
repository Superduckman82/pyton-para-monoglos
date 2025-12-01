

while True:
    print("dame 2 numeros")
    numero1 = input("dame el primero: ")
    numero2 = input("ahora el otro numero: ")
    
    respuesta = input("que quieres hacer, sumar, restar, multiplicar o dividir? ")
    if respuesta == "sumar":
        resultado = int(numero1) + int(numero2) 
    elif respuesta == "restar":
        resultado = int(numero1) - int(numero2) 
    elif respuesta == "multiplicar":
        resultado = int(numero1) * int(numero2)
    elif respuesta == "dividir":
        resultado = int(numero1) / int(numero2)
    else:
        print(f"cara alfombra, sumar, restar o dividir, no {respuesta}")
        continue    
    
    print(f"este es el resultado: {resultado}")
