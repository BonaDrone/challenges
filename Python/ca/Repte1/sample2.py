import time
import cflib.crtp
from cflib.crazyflie.syncCrazyflie import SyncCrazyflie
from cflib.positioning.motion_commander import MotionCommander

URI = 'radio://0/80/2M'

def main():
    cflib.crtp.init_drivers(enable_debug_driver=False)
    
	numRepeticions = int(input("Quants cops vols repetir la ruta?"))
    ruta = input("Quina ruta vols realitzar?")

    print(numRepeticions)
    print(ruta)

main()