#Boton de activación
print("TARJETA INGRESADA CON EXITO")

cont = 0
clave = 123456
saldo = 85000
saldosol = 3584
menu = 0
destino = 98765


def tipomoneda():
    moneda = int(input("1.PESOS 2.SOLES: "))
    if moneda == 1:
        moneda = saldo
    else:
        moneda = saldosol

    return moneda
def consultas():
    op = int(input("""OPCIONES
                      1.Posición Global
                      2.Movimientos
                      : """))
    moneda = tipomoneda()            
    if op == 1:
        vv = int(input("1.Ver en pantalla 2.Imprimir: "))
        if vv == 1:
            print(f"Saldo disponible es: {moneda}")
        else:
            print(f"Imprimir saldo disponible: {moneda}")
    else:
        vv = int(input("1.Ver en pantalla 2.Imprimir: "))
        if vv == 1:
            print("Imprimir últimos 10 movimientos")
        else:
            print("Ultimos 10 movimientos")
        
    
def retiros():
    rcont = 0
    moneda = tipomoneda()
    while rcont < 2:
        mr = int(input("Ingrese monto a retirar: "))
        if mr <= moneda:
            intento = int(input("INGRESE LA CLAVE DE ACCESO: ")) 
            if intento == clave:
               iv = int(input("1.Imprimir Voucher 2. No Imprimir Voucher"))
               if iv == 1:
                   print(f"Imprimir voucher: Su saldo actual es de: {moneda - mr}")
                   rcont = 2
               else:
                   rcont = 2
            else:
                rcont = rcont + 1
        else:
            print("Saldo Ingresado no disponible")
            rcont = rcont + 1
            
def transferencias():
    CBU = int(input("INGRESAR CBU: "))
    if CBU == destino:
        moneda = tipomoneda()
        mt = int(input("INGRESAR MONTO A TRANSFERIR: "))
        while mt >= moneda:
            mt = int(input("REINGRESE MONTO A TRANSFERIR: "))
        cdc = int(input(f"""La cuenta destino {CBU} es correcta
                        1.SI 2.NO: """))
        if cdc == 1:
            moneda = moneda - mt
            print(f"Su transferencia ha sido efectuada con exito! a la cuenta {CBU}, su saldo actual es de {moneda} ")
        else:
            print("Despues de 3 dias podras observar la devolución del dinero en movimientos")
                  
while cont < 3:
    intento = int(input("INGRESE LA CLAVE DE ACCESO: "))
    if intento == clave:
        dni = int(input("INGRESE SU DNI: "))
        if dni == 12345678:
            while menu != 4:
                menu = int(input("""    
                    MENU
                    1.Consultas
                    2.Retiros
                    3.Transferencias 
                    4.Salir
                    """))
            
                if menu == 1:
                    consulta = consultas()
                elif menu == 2:
                    retiro = retiros()
                elif menu == 3:
                    trans = transferencias()
                elif menu == 4:
                    quit()
                else:
                    print("ERROR: 1 EL NUMERO INGRESADO NO SE ENCUENTRA EN EL MENU")
                    
    else:
        cont = cont + 1