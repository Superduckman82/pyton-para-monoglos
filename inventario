
inventario = {
        
        "elemento1": {
         "objeto": "patatas",
         "cantidad": 5,
         "precio": 1.20
        },
        "elemento2": {
         "objeto": "manzanas",
         "cantidad": 10,
         "precio": 0.80 
        }
}

while True:


    print("que quieres hacer?")
    print("1. ver el inventario")
    print("2. modificar algo")
    print("3. salir. ")


    elección = int(input())
    if elección == 1: 
        for clave, datos in inventario.items():
            objeto = datos["objeto"]
            cantidad = datos["cantidad"]
            precio = datos["precio"]
            print(f"hay {cantidad} de {objeto} a {precio}")
    elif elección == 2:
                cambio1 = input("que quiere cambiar, las patatas o las manzanas? ")
        if cambio1 == "patatas":
            print("precio o cantidad? ")
            precant = input("")
            if precant == "precio":
                augprec = float(input("a cuanto lo quiere augmentar? "))
                inventario["elemento1"]["precio"] = augprec
            elif precant == "cantidad":
                augcant = int(input("a cuanto lo quiere augmentar? "))
                inventario["elemento1"]["cantidad"] = augcant
        elif cambio1 == "manzanas":
            print("precio o cantidad? ")
            precant = input("")
            if precant == "precio": 
                augprec = float(input("a cuanto lo quiere augmentar? "))
                inventario["elemento2"]["precio"] = augprec
            elif precant == "cantidad":
                augcant = int(input("a cuanto lo quiere augmentar? "))
                 inventario["elemento2"]["cantidad"] = augcant
    elif elección == 3:
        print("vayase usté a cagar") 
        break

