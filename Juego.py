from Jugador import Jugador
from Tablero import Tablero

class Juego:


    def __init__(self):
        
        self.miJugador=Jugador("humano")

        self.computador=Jugador("computador")

        self.miTablero=Tablero()

    def jugarTriqui(self):
    
        self.miJugador.seleccionar_simbolo()
        if self.miJugador.miFicha.simbolo=='X':
            self.computador.miFicha.simbolo='O'
        else:
            self.computador.miFicha.simbolo='X'
        jugadas=0

        while jugadas<9:
            self.miJugador.realizar_jugada(self.miTablero)
            if self.miTablero.verificar_triqui():
                print("Ganaste")
                return True
            self.computador.realizar_jugada(self.miTablero)
            if self.miTablero.verificar_triqui():
                    print("Perdiste")
                    return True
            self.miTablero.mostrar_tablero()
            jugadas=jugadas+1

miJuego=Juego()
miJuego.jugarTriqui()