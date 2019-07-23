import time
import cflib.crtp
from cflib.crazyflie.syncCrazyflie import SyncCrazyflie
from cflib.positioning.motion_commander import MotionCommander

URI = 'radio://0/80/2M'
rutaABC = 'ABC'
rutaBC = 'BC'
rutaCA = 'CA'
rutaCB = 'CB'
rutaAC = 'AC'

def main():
    cflib.crtp.init_drivers(enable_debug_driver=False)

    numRepeticions = int(input("Quants cops vols repetir la ruta?"))
    ruta = input("Quina ruta vols realitzar?")

    with SyncCrazyflie(URI) as scf:
        with MotionCommander(scf) as mq90:
            for num in range(numRepeticions):
                if ruta == rutaABC:
                    mq90.forward(1.5)
                    mq90.turn_right(135)
                    mq90.forward(0.71)

                    #Return to A from C
                    mq90.turn_right(90)
                    mq90.forward(0.71)
                    mq90.turn_right(135)

                elif ruta == rutaBC:
                    mq90.forward(0.71)

                    #Return to B from C
                    mq90.turn_right(180)
                    mq90.forward(0.71)
                    mq90.turn_right(180)

                elif ruta == rutaCB:
                    mq90.forward(0.71)

                    #Return to C
                    mq90.turn_right(180)
                    mq90.forward(0.71)
                    mq90.turn_right(180)

                elif ruta == rutaCA:
                    mq90.forward(0.71)

                    #Return to C
                    mq90.turn_right(180)
                    mq90.forward(0.71)
                    mq90.turn_right(180)

                elif ruta == rutaAC:
                    mq90.forward(0.71)

                    #Return to A from C
                    mq90.turn_right(90)
                    mq90.forward(0.71)
                    mq90.turn_right(135)

            mq90.land()

main()