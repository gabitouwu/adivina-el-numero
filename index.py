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

def comprobarQSeaNum(lNP, numMin, numMax): # v = valor(estimacion), lNP = lista de numeros posibles, NUMMAX = Numero maximo por adivinar
    v = input()
    while v not in lNP:
        print('Ingresa un numero (%s al %s)' % (numMin, numMax))
        v = input()
        
    return v

def pista(nS, v, iJ): # nS = numero Secreto, v = valor(estimacion), iJ = intentos del Jugador
    iJ = iJ + 1
    
    if v > nS:
        return 'Tu estimación es muy alta', iJ

    elif v < nS:
        return 'Tu estimacion es muy baja.', iJ

    return 'Ganador', iJ

def compQNoSeaRep(v, lNI): #lNI = lista de Numeros Ingresados
    if v in lNI:
        return True

def ganador(nS, v, iD, iJ): # nS = numero secreto, v = valor(estimacion), iD = intentos Disponibles, iJ = intentos del Jugador
    if v == nS:    
        return 'Ganaste.'
    elif iD == iJ:
        return 'Perdiste.'
    else:
        return 1

def T_L_E_S(listaDeEnteros):
    lstr = []
    for i in listaDeEnteros:
        o = str(i)
        lstr.append(o)

    return lstr 

def jugarDeNuevo():
    r = input('¿Deseas volver a jugar? (S/N): ')
    if r == '':
        return True

    if r.startswith('s') or r.startswith('S'):
        return True
    else:
        return False

def siNo():    
    r = input('¿Deseas ingresar los numeros por adivinar? (S/N): ') 
    if r == '':
        return True

    if r.startswith('s') or r.startswith('S'):
        return True
    else:
        return False

def minAndMax(num):
    for i in num:
        if i not in '0 1 2 3 4 5 6 7 8 9'.split():
            return True
    if num == '':
        return True
    
    return False

MAXADIVINANZAS = 7
frases = ['Ya usaste ese numero', 'Ingresa otro numero', '¿Enserio?']
print(BIENVENIDA)
print(NOMBRE_DEL_JUEGO)

while True:
    a = False
    numMin = 1
    numMax = 0

    si_No = siNo()
    if si_No:

        print('Ingresa el numero minimo y el numero máximo por adivinar a continuacion.')

        while numMin > numMax:
            numMin = input('Numero min: ')    
            while minAndMax(numMin) or int(numMin) > 50:
                print('Ingrese numeros y que no sean mayores a 50.')
                numMin = input('Numero min: ')

            numMax = input('Numero max: ') 
            while minAndMax(numMax) or int(numMax) > 50:    
                print('Ingrese numeros y que no sean mayores a 50.')
                numMax = input('Numero max: ')

            if int(numMin) > int(numMax):
                print('El número mínimo no puede ser mayor al máximo.')

        numMin = int(numMin)
        numMax = int(numMax)

        a = True

    if not(a):
        numMin = 1
        numMax = 22

    numPosibles = list(range(numMin, numMax + 1))
    lstr = T_L_E_S(numPosibles)

    print('\nEstoy pensando en un número del %s al %s.' % (numMin, numMax))
    print('Ingresa tu estimacion a continuación:')
    MAXADIVINANZAS -= 1
    print('Tienes solo %s intentos.' % (MAXADIVINANZAS))
    MAXADIVINANZAS += 1
    numSecreto = random.randint(numMin, numMax)
    numIngresados = []
    numIntentos = 1

    while True:
        print('Intento #%s.' % (numIntentos))
        valor = comprobarQSeaNum(lstr, numMin, numMax)
        while compQNoSeaRep(valor, numIngresados):
            random.shuffle(frases)
            i = random.randint(0, (len(frases) - 1))
            print(frases[i])
            valor = comprobarQSeaNum(lstr, numMin, numMax)

        numIngresados.append(valor)
        pistas, numIntentos = pista(numSecreto, int(valor), numIntentos)
        
        if ganador(numSecreto, int(valor), MAXADIVINANZAS, numIntentos) == 'Ganaste.':
            print('Ganaste')
            break
        elif ganador(numSecreto, int(valor), MAXADIVINANZAS, numIntentos) == 'Perdiste.':
            print('Perdiste, el numero era %s.' % (numSecreto))
            break
                
        print(pistas)
        
    if not(jugarDeNuevo()):
        break