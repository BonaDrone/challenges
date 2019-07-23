import time
import cflib.crtp
from cflib.crazyflie.syncCrazyflie import SyncCrazyflie
from cflib.positioning.motion_commander import MotionCommander

URI = 'radio://0/80/2M'

def main():
    cflib.crtp.init_drivers(enable_debug_driver=False)
    numVertices = int(input("¿Qué número de vertices quieres que tenga la estrella?"))
    numRepeticiones = int(input("¿Cuántas veces quieres realizar la estrella?"))
    distanciaAristas = float(input("¿Longitud de las aristas (Entre 0.4m y 1 m)?"))

    with SyncCrazyflie(URI) as scf:
        with MotionCommander(scf) as mq90:
            gradosArista = 180-(180/numVertices)

            for repeticio in range(numRepeticiones):
                for vertex in range(numVertices):
                    mq90.forward(distanciaAristas)
                    mq90.turn_right(gradosArista)

            mq90.land()

main()