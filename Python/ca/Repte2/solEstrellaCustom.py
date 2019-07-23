import time
import cflib.crtp
from cflib.crazyflie.syncCrazyflie import SyncCrazyflie
from cflib.positioning.motion_commander import MotionCommander

URI = 'radio://0/80/2M'

def main():
    cflib.crtp.init_drivers(enable_debug_driver=False)
    numVertex = int(input("Quin número de vertex vols que tingui la estrella?"))
    numRepeticions = int(input("Quants cops vols realitzar l'estrella?"))
    llargadaArestes = float(input("Longitud de les arestes (Entre 0.4m i 1 m)?"))

    with SyncCrazyflie(URI) as scf:
        with MotionCommander(scf) as mq90:
            grausAresta = 180-(180/numVertex)

            for repeticio in range(numRepeticions):
                for vertex in range(numVertex):
                    mq90.forward(llargadaArestes)
                    mq90.turn_right(grausAresta)

            mq90.land()

main()