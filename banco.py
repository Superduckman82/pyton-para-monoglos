def crear_cuenta(banco, num_cuenta, nombre, pin, saldoi):

        banco[num_cuenta] = {
            "nombre": nombre,
            "pin": pin,
            "saldoi": saldoi,
            "historial": [f"apertura de cuenta: +{saldoi:.2f}€"]
        }   
        print("cuenta creada con exito")

cuentas_banco = {}


while True:

    print("---- BANCO ----")
    print("1. iniciar sesión")
    print("2. crear cuenta")
    print("3. salir")

    try:
        opcion = int(input())
    except ValueError:
        print("esa no es una opción disponible, intentalo otra vez.")
        continue

    if opcion == 1:
        num_cuenta = input("introduce tu numero de cuenta: ")

        if num_cuenta in cuentas_banco:
            intentos = 3

            while intentos > 0:
                pin_input = input("pin: ")

                if pin_input == cuentas_banco[num_cuenta]["pin"]:

                    while True:
                        print(f"\nBienbenido/a, {cuentas_banco[num_cuenta]['nombre']}!")
                        #bucle de funciones de sesión iniciada
                        print("\n que desea hacer?")
                        print("1. consultar saldo")
                        print("2. añadir saldo")
                        print("3. retirar saldo")
                        print("4. ver el historial")
                        print("5. transferencia bancaria")
                        print("6. salir")

                        try:
                            opcion2 = int(input())
                        except ValueError:
                            print("esa no es una opción disponible, inténtelo otra vez.")
                            continue


                        if opcion2 == 1:
                            print(f"su saldo es de {cuentas_banco[num_cuenta]['saldoi']}") 
                            continue

                        elif opcion2 == 2:
                            while True:
                                try: 
                                    ingreso = float(input("cuanto dinero quiere ingresar?"))
                                except ValueError:
                                    print("eso no es un valor monetario, apollardao, escribalo otra vez")
                                    continue

                                cuentas_banco[num_cuenta]['saldoi'] += ingreso
                                cuentas_banco[num_cuenta]['historial'].append(f"ingreso: +{ingreso: .2f}€")

                                print("dinero ingresado, muchas gracias!")
                                break

                        elif opcion2 == 3:
                            while True:
                                try: 
                                    retiro = float(input("cuanto dinero quiere retirar??"))
                                except ValueError:
                                    print("eso no es un valor monetario, apollardao, escribalo otra vez")
                                    continue

                                while True:
                                    if retiro > 0 and retiro < saldoi:
                                        cuentas_banco[num_cuenta]['saldoi'] -= retiro
                                        cuentas_banco[num_cuenta]['historial'].append(f"retiro: -{retiro: .2f}€")
                                        print("dinero retirado, muchas gracias!")
                                        break
                                    elif retiro < 0:
                                        print("no puede retirar numeros negativos, para hacer eso deberia ingresar dinero, intentelo de nuevo.")
                                        continue
                                    elif retiro > 0 and retiro > saldoi:
                                        print("no tiene suficiente saldo en su cuenta, intentelo de nuevo")
                                        continue
                                    else:
                                        print("no ha introducido un valor apto, intentelo de nuevo.")
                                        continue
                                        
                                break

                        elif opcion2 == 4:
                            print("----- historial de movimientos -----")

                            for movimientos in cuentas_banco[num_cuenta]['historial']:
                                print (f"- {movimientos}")
                        

                        elif opcion2 == 5:
                            print("a que numero de cuenta quieres tranferir el dinero?")

                            try:
                                target = input()
                            except ValueError:
                                print("eso no es un numero de cuenta valido")
                                continue


                            if target in cuentas_banco:
                                if target == num_cuenta:
                                    print("no puedes enviarte dinero a tu propia cuenta.")

                                else: 
                                    print(f"cuenta encontrada, vas a transferir dinero a la cuenta {cuentas_banco[target]['nombre']}")

                                    while True:
                                    
                                        print("cuanto dinero quieres transferir?")
                                        try:
                                            value = float(input())
                                        except ValueError:
                                            print("eso no es un numero, intentelo otra vez.")
                                            continue

                                        if value < cuentas_banco[num_cuenta]['saldoi']:
                                            cuentas_banco[num_cuenta]['saldoi'] -= value
                                            cuentas_banco[num_cuenta]['historial'].append(f"traspaso: -{value: .2f}€")

                                            cuentas_banco[target]['saldoi'] += value                     
                                            cuentas_banco[target]['historial'].append(f"traspaso: +{value: .2f}€")

                                            print("transferencia realizada")
                                            break

                                        else: 
                                            print("no tienes suficiente saldo, intentelo de nuevo")
                                            continue

                            else: 
                                print("el numero de destino no existe")
                                break
                        
                        elif opcion2 == 6:
                            break
                    break
                else: 
                        intentos -= 1
                if intentos > 0:
                    print(f"pin incorrecto, le quedan {intentos} restantes")
                else:
                    print("has agotado los 3 intentos, te bloqueo la cuenta, pollo")
        else:
            print("el numero de cuenta no existe")



    elif opcion == 2:
        while True:
            num_cuenta = input("numero de cuenta: ")
            if num_cuenta in cuentas_banco:
                print("ese numero ya existe, intentelo otra vez")
                continue

            nombre = input("introduzca su nombre: ")

            pin = input("itroduzca el pin que quiere tener: ")
            while True:
                try:
                    saldoi = float(input("itroduzca el saldo que quiere poner en la cuenta: "))
                except ValueError:
                    print("eso no es un numero, introduzca un numero")
                    continue
                break
                
            crear_cuenta(cuentas_banco, num_cuenta, nombre, pin, saldoi)
            break
 
    elif opcion == 3: 
        break
   