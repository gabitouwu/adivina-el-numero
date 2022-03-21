from time import sleep
import random 

BIENVENIDA='''

 ▄▄▄▄    ██▓▓█████  ███▄    █ ██▒   █▓▓█████  ███▄    █  ██▓▓█████▄  ▒█████   ▐██▌ 
▓█████▄ ▓██▒▓█   ▀  ██ ▀█   █▓██░   █▒▓█   ▀  ██ ▀█   █ ▓██▒▒██▀ ██▌▒██▒  ██▒ ▐██▌ 
▒██▒ ▄██▒██▒▒███   ▓██  ▀█ ██▒▓██  █▒░▒███   ▓██  ▀█ ██▒▒██▒░██   █▌▒██░  ██▒ ▐██▌ 
▒██░█▀  ░██░▒▓█  ▄ ▓██▒  ▐▌██▒ ▒██ █░░▒▓█  ▄ ▓██▒  ▐▌██▒░██░░▓█▄   ▌▒██   ██░ ▓██▒ 
░▓█  ▀█▓░██░░▒████▒▒██░   ▓██░  ▒▀█░  ░▒████▒▒██░   ▓██░░██░░▒████▓ ░ ████▓▒░ ▒▄▄  
░▒▓███▀▒░▓  ░░ ▒░ ░░ ▒░   ▒ ▒   ░ ▐░  ░░ ▒░ ░░ ▒░   ▒ ▒ ░▓   ▒▒▓  ▒ ░ ▒░▒░▒░  ░▀▀▒ 
▒░▒   ░  ▒ ░ ░ ░  ░░ ░░   ░ ▒░  ░ ░░   ░ ░  ░░ ░░   ░ ▒░ ▒ ░ ░ ▒  ▒   ░ ▒ ▒░  ░  ░ 
 ░    ░  ▒ ░   ░      ░   ░ ░     ░░     ░      ░   ░ ░  ▒ ░ ░ ░  ░ ░ ░ ░ ▒      ░ 
 ░       ░     ░  ░         ░      ░     ░  ░         ░  ░     ░        ░ ░   ░    
      ░                           ░                          ░                     '''

NOMBRE_DEL_JUEGO = '''


 █████╗ ██████╗ ██╗██╗   ██╗██╗███╗   ██╗ █████╗     ███████╗██╗         ███╗   ██╗██╗   ██╗███╗   ███╗███████╗██████╗  ██████╗ 
██╔══██╗██╔══██╗██║██║   ██║██║████╗  ██║██╔══██╗    ██╔════╝██║         ████╗  ██║██║   ██║████╗ ████║██╔════╝██╔══██╗██╔═══██╗
███████║██║  ██║██║██║   ██║██║██╔██╗ ██║███████║    █████╗  ██║         ██╔██╗ ██║██║   ██║██╔████╔██║█████╗  ██████╔╝██║   ██║
██╔══██║██║  ██║██║╚██╗ ██╔╝██║██║╚██╗██║██╔══██║    ██╔══╝  ██║         ██║╚██╗██║██║   ██║██║╚██╔╝██║██╔══╝  ██╔══██╗██║   ██║
██║  ██║██████╔╝██║ ╚████╔╝ ██║██║ ╚████║██║  ██║    ███████╗███████╗    ██║ ╚████║╚██████╔╝██║ ╚═╝ ██║███████╗██║  ██║╚██████╔╝
╚═╝  ╚═╝╚═════╝ ╚═╝  ╚═══╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝    ╚══════╝╚══════╝    ╚═╝  ╚═══╝ ╚═════╝ ╚═╝     ╚═╝╚══════╝╚═╝  ╚═╝ ╚═════╝ 
                                                                                                                                '''


def bienvenida(BIENVENIDA, NOMBRE_DEL_JUEGO): 
    for i in BIENVENIDA:
        print(i, end='')
    print('\n')

    print(NOMBRE_DEL_JUEGO)

def nombreDelJugador():
    sleep(1)
    print('Ingresa tu nombre:', end=' ')
    nombre = input()
    while nombre == '':
        print('¡Ingresa un NOMBRE!')
        nombre = input()
        if nombre != '':
            break
    return nombre

def explicacionDelJuego(nombreDelJugador):
    for i in 'Hola, ' + nombreDelJugador + ', estoy pensando en un nuero del 1 al 20, ':
        sleep(0.029)
        print(i, end='')

    print()
    for i in 'intenta adivinarlo, tienes solo 6 intentos, ¡suerte!':
        sleep(0.029)
        print(i, end = '')
        
    print()

def numeroRandom(): #Se crea un numero random del 1 al 20
    numeroRandom = random.randint(1, 20)

    return numeroRandom
#--------------------------------------------------------------
def ingresarValor():
    for i in 'Ingrese su estimacion a continuacion:':
        sleep(0.029)
        print(i, end='')

    print()
    estimacion = input()
    while True:
        while len(estimacion) >= 0:
            if estimacion in '1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20'.split():
                return int(estimacion)
            else:
                for i in '¡SIGUE LAS NORMAS!':
                    sleep(0.029)
                    print(i, end='')
                print()
                estimacion = input()
                
#----------------------------------------------------------
def comprobarEstimacion(estimacionDelJugador, numeroRandom, intentosDisponibles, numeroDeIntentos): #Aqui se comprueba la estimacion del jugador
    
    while numeroDeIntentos < intentosDisponibles:
    
        numeroDeIntentos = numeroDeIntentos + 1
    
        if estimacionDelJugador < numeroRandom:
            sleep(1)
            print('El valor ingresado es muy bajo')
            if numeroDeIntentos == 1:
                print('Te quedan 5 intentos')

            if numeroDeIntentos == 2:
                print('Te quedan 4 intentos')

            if numeroDeIntentos == 3:
                print('Te quedan 3 intentos')

            if numeroDeIntentos == 4:
                print('Te quedan 2 intentos')

            if numeroDeIntentos == 5:
                print('Te quedan 1 intentos')
    
            if numeroDeIntentos == 6:
                print('¡Se te terminaron los intentos!')
                
        if estimacionDelJugador > numeroRandom:
            sleep(1)
            print('El valor ingresado es muy alto')

            if numeroDeIntentos == 1:
                print('Te quedan 5 intentos')

            if numeroDeIntentos == 2:
                print('Te quedan 4 intentos')

            if numeroDeIntentos == 3:
                print('Te quedan 3 intentos')

            if numeroDeIntentos == 4:
                print('Te quedan 2 intentos')

            if numeroDeIntentos == 5:
                print('Te quedan 1 intentos')
    
            if numeroDeIntentos == 6:
                print('¡Se te terminaron los intentos!')

        if estimacionDelJugador == numeroRandom:
            break

        if numeroDeIntentos == intentosDisponibles:
            break

        estimacionDelJugador = ingresarValor()


    if estimacionDelJugador == numeroRandom:
        sleep(2)
        print('¡Correcto ganaste en ' + str(numeroDeIntentos) + ' intentos!')

    if estimacionDelJugador != numeroRandom:
        sleep(2)
        print('¡El número en el que estaba pensando era el ' + str(numeroRandom) + '!')

    terminarJuego = True

    return terminarJuego

def jugarDeNuevo(): 
    print('¿Deseas volver a jugar de nuevo? (sí o no)')
    return input().lower().startswith('s') 

def ejecutarJuego():
    intentosDisponibles = 6 
    intentosDelJugador = 0

    explicacionDelJuego(nombreDelJugador())

    estimacionDelJugador = ingresarValor()

    terminarJuego = comprobarEstimacion(estimacionDelJugador, numeroRandom(), intentosDisponibles, intentosDelJugador) 
        
    return terminarJuego

bienvenida(BIENVENIDA, NOMBRE_DEL_JUEGO)    

terminarJuego = ejecutarJuego()

while terminarJuego == True:
    trueOrFalse = jugarDeNuevo()
    if trueOrFalse == True:
        terminarJuego = ejecutarJuego()
    else:
        break
