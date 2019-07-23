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
    
    numRepeticiones = int(input("¿Cuántas veces quieres repetir la ruta?"))
    ruta = input("¿Qué ruta quieres realizar?")

    with SyncCrazyflie(URI) as scf:
        with MotionCommander(scf) as mq90:
            for num in range(numRepeticiones):
                if ruta == rutaABC:
                    mq90.up(1)
                    mq90.forward(1)
                    ...
                    ...
                elif ruta == rutaBC:
                    mq90.up(1)
                    mq90.forward(1)
                    ...
                    ...
                elif ruta == rutaCB:
                    mq90.up(1)
                    mq90.forward(1)
                    ...
                    ...
                elif ruta == rutaCA:
                    mq90.up(1)
                    mq90.forward(1)
                    ...
                    ...
                elif ruta == rutaAC:
                    mq90.up(1)
                    mq90.forward(1)
                    ...
                    ...

            mq90.land()

main()