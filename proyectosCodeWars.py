# TRUCO
from logging import raiseExceptions
import random
import os

def clear_console():
    os.system('clear')


# diccionario con el valor de cada carta; cual mata a cual
valor_cartas = {"ancho_Espada": 100, "ancho_Basto": 18, "siete_Espada": 17, "siete_Basto": 16, "doce_Espada": 12, "doce_Basto": 12, "doce_Oro": 12, "doce_Copa": 12, "once_Espada": 11, "once_Basto": 11, "once_Oro": 11, "once_Copa": 11, "diez_Espada": 10, "diez_Basto": 10, "diez_Oro": 10, "diez_Copa": 10, "siete_Oro": 7, "siete_Copa": 7, "tres_Espada": 15,
                "tres_Basto": 15, "tres_Oro": 15, "tres_Copa": 15, "dos_Espada": 14, "dos_Basto": 14, "dos_Oro": 14, "dos_Copa": 14, "ancho_Oro": 13, "ancho_Copa": 13, "seis_Espada": 3, "seis_Basto": 3, "seis_Oro": 3, "seis_Copa": 3, "cinco_Espada": 2, "cinco_Basto": 2, "cinco_Oro": 2, "cinco_Copa": 2, "cuatro_Espada": 1, "cuatro_Basto": 1, "cuatro_Oro": 1, "cuatro_Copa": 1}
# SEPARAR EN STRING VALOR Y PALO POR UN "_" PARA PODER MANEJAR EL STRING Y OBTENER EL PALO MÁS FÁCIL

# diccionario con valor para envido
valor_envido ={"ancho_Espada": 1, "ancho_Basto": 1, "siete_Espada": 7, "siete_Basto": 7, "doce_Espada": 0, "doce_Basto": 0, "doce_Oro": 0, "doce_Copa": 0, "once_Espada": 0, "once_Basto": 0, "once_Oro": 0, "once_Copa": 0, "diez_Espada": 0, "diez_Basto": 0, "diez_Oro": 0, "diez_Copa": 0, "siete_Oro": 7, "siete_Copa": 7, "tres_Espada": 3,
                "tres_Basto": 3, "tres_Oro": 3, "tres_Copa": 3, "dos_Espada": 2, "dos_Basto": 2, "dos_Oro": 2, "dos_Copa": 2, "ancho_Oro": 1, "ancho_Copa": 1, "seis_Espada": 6, "seis_Basto": 6, "seis_Oro": 6, "seis_Copa": 6, "cinco_Espada": 5, "cinco_Basto": 5, "cinco_Oro": 5, "cinco_Copa": 5, "cuatro_Espada": 4, "cuatro_Basto": 4, "cuatro_Oro": 4, "cuatro_Copa": 4}

mazo = list(valor_cartas)

# ENVIDO

def tipo_de_carta(tipo,carta):
    if tipo in carta: return True

def chequear_Palo_Carta(carta):
    palo = carta.split("_")
    return palo[1] 

def chequear_Palo_Mano(mano): # DEVUELVE LOS PALOS DE LA MANO RECIBIDA
    manoNueva = []
    for carta in mano:
        palo = carta.split("_")
        manoNueva.append(palo[1])
        palo.clear()
    return manoNueva 

def esParDe(carta1,carta2):
    return chequear_Palo_Carta(carta1) == chequear_Palo_Carta(carta2)

def cartasPares(mano): #DEVUELVE CARTAS CON EL MISMO PALO EN UNA MANO
    lst_Pares=[]
    i = 0
    for i in range(0,3):
        for j in range(1,3):
            if mano[i] != mano[j] and esParDe(mano[i],mano[j]): 
                lst_Pares.append(mano[i])
                lst_Pares.append(mano[j]) 

    return list(set(lst_Pares))    

def valores_Mas_Altos(mano):
    for carta in mano:
        lista_valores = list(map(valor_envido.get,mano))

    lista_valores.remove(min(lista_valores))

    return lista_valores    

def valor_envido_Mas_Alto(mano):
    for carta in mano:
        lista_valores = list(map(valor_envido.get,mano))

    return max(lista_valores)    
    

def envido(jugador): # ENVIDO DE JUGADOR 
    envido_Valor = 0
    mano1 = jugador.cartas_en_mano
    pares = cartasPares(mano1)
    if len(pares) == 2:
        envido_Valor += 20
        for carta in pares:
            envido_Valor += valor_envido[carta]
    elif len(pares) == 3:
        envido_Valor += 20
        mano1 = valores_Mas_Altos(pares)
        for carta in mano1:
            envido_Valor += carta
    else: 
        envido_Valor = valor_envido_Mas_Alto(mano1)      
           

    return envido_Valor


#CLASE JUGADOR
class Jugador:
    cant_cartas = 3

    def __init__(self, cartas_en_mano, manos_ganadas,puntos_ganados):
        self.cartas_en_mano = cartas_en_mano
        self.manos_ganadas = manos_ganadas
        self.puntos_ganados = puntos_ganados

    def tirarCarta_random(self):
        carta = random.choice(self.cartas_en_mano)
        self.cartas_en_mano.remove(carta)
        print(carta)
        return carta   

    def tirarCarta(self, carta):
        self.cartas_en_mano.remove(carta)

    def armarMano(self):
        for i in range(0,3):
            carta = random.choice(mazo)
            self.cartas_en_mano.append(carta)
            mazo.remove(carta)

    def sumar_puntos(self, puntos):
        self.manos_ganadas = self.manos_ganadas + puntos

    def puntos_totales(self):
        return self.manos_ganadas

    def tieneCartas(self):
        return len(self.cartas_en_mano) > 0

    def ver_cartas(self):
        return self.cartas_en_mano



def carta_mata_carta(carta1, carta2): # CARTA VS CARTA
    if valor_cartas[carta1] == valor_cartas[carta2]:
        return 0.5     # "EMPATE"
    elif valor_cartas[carta1] > valor_cartas[carta2]:
        return 1  # CARTA 1 MATA CARTA 2
    else:
        return 2  # CARTA 2 MATA CARTA 1


def armar_mano():
    mano = []
    carta = 0
    for i in range(0, 3):
        carta = random.choice(mazo)  # TOMO CARTA DEL MAZO
        mano.append(carta)  # AGREGO A LA MANO DEL JUGADOR
        mazo.remove(carta)  # SACO DEL MAZO

    return mano

def jugar_Envido(jugador_A, jugador_B):

    
    if envido(jugador_A) > envido(jugador_B):
        print(f"\nGana jugador 1: {envido(jugador_A)} > {envido(jugador_B)}\n")
        return 0

    elif envido(jugador_A) < envido(jugador_B):
        print(f"\nGana jugador 2: {envido(jugador_B)} > {envido(jugador_A)}\n")
        return 1

    else: 
        print(f"\nGana jugador 1: {envido(jugador_A)} = {envido(jugador_B)}; jugador 1 es mano \n")
        return 0

    pass                

# LOOP DEL JUEGO

def jugar_una_mano(jugador_A, jugador_B):
    contador = [0,0] # CONTADOR DE PUNTOS
    envido_cantado = False
    primera_mano_jugada = False

    jugador_A.armarMano()
    jugador_B.armarMano() 
    
    while(jugador_B.tieneCartas()): #COMIENZO DE MANO

        if (jugador_A.puntos_totales() == 2 or jugador_B.puntos_totales() == 2):  # GANA DOS MANOS
            break

        print(f"\nPUNTOS DEL JUGADOR: {contador[0]}\n")
        print(f"\nPUNTOS DEL JUGADOR: {contador[1]}\n")
        print(f"\nCartas jugador_1: {jugador1.cartas_en_mano}")

        if not envido_cantado and not primera_mano_jugada:    
            opcion = input("\n Quiere cantar envido?: (si/no)")
 
            if opcion == "si":
                contador[jugar_Envido(jugador_A,jugador_B)] += 2
                envido_cantado = True
            else: pass    
        
        carta1 = input("\nElija una carta de su mano: ('R' para irse al mazo)\n")
            
        if carta1 == "R":       #IRSE AL MAZO (RESIGN)
            print("\nJugador 1 se fue al mazo.")
            break

        jugador_A.tirarCarta(carta1)
        carta2 = jugador_B.tirarCarta_random()

        primera_mano_jugada = True
            
        if carta_mata_carta(carta1, carta2) == 0.5:  # CARTAS TIENEN MISMO VALOR
            jugador_A.sumar_puntos(0.5)
            jugador_B.sumar_puntos(0.5)
            print("\n EMPATE \n")
        elif carta_mata_carta(carta1, carta2) == 1:  # CARTA 1 MATA CARTA 2
            jugador_A.sumar_puntos(1)
            print("\n GANA JUGADOR 1 \n")
        else:                               # CARTA 2 MATA CARTA 1
            jugador_B.sumar_puntos(1)
            print("\n GANA JUGADOR 2 \n")

    if jugador_A.manos_ganadas > jugador_B.manos_ganadas :
        contador[0] += 1
    elif jugador_A.manos_ganadas < jugador_B.manos_ganadas :
        contador[0] += 1
    else:  print("EMPATE")        


    mazo = list(valor_cartas)
    print(contador)
    return f"El jugador 1 ha ganado: {jugador_A.puntos_totales() >  jugador_B.puntos_totales()}"







# INSTANCIAS DE JUGADORES
jugadorPrueba = Jugador(["tres_Oro","ancho_Espada","ancho_Basto"], 0, 0)
jugador1 = Jugador([], 0, 0)
jugador2 = Jugador([], 0, 0)


# TESTS

#print(jugador1.cartas_en_mano)
#print(jugador2.cartas_en_mano)
print(mazo)
print("\n")

print(jugar_una_mano(jugador1, jugador2))  # SIMULACION MANO
