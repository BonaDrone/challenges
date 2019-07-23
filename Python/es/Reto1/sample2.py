import time
import cflib.crtp
from cflib.crazyflie.syncCrazyflie import SyncCrazyflie
from cflib.positioning.motion_commander import MotionCommander

URI = 'radio://0/80/2M'

def main():
    cflib.crtp.init_drivers(enable_debug_driver=False)
    
    numRepeticiones = int(input("¿Cuántas veces quieres repetir la ruta?"))
    ruta = input("¿Qué ruta quieres realizar?")
	
    print(numRepeticiones)
    print(ruta)

main()