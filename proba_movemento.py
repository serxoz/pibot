from lib.Mover import Mover
import RPi.GPIO as GPIO

#Inicio dos GPIO
GPIO.setmode(GPIO.BOARD)

m = Mover()

m.adiante(0.5)
m.atrais(0.5)
m.rotar_horario(0.5)
m.rotar_antih(0.5)

m.adiante_dta(0.5)
m.quieto()

m.atrais_dta(0.5)
m.quieto()

m.adiante_izq(0.5)
m.quieto()

m.atrais_izq(0.5)
m.quieto()


#por si acaso :D
m.quieto()

#Restauracion dos GPIO
GPIO.cleanup()
