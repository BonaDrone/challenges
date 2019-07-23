import time
import cflib.crtp
from cflib.crazyflie.syncCrazyflie import SyncCrazyflie
from cflib.positioning.motion_commander import MotionCommander

URI = 'radio://0/80/2M'

def main():
    cflib.crtp.init_drivers(enable_debug_driver=False)

    with SyncCrazyflie(URI) as scf:
        with MotionCommander(scf) as mq90:
            mq90.forward(1)
            mq90.turn_right(120)
            mq90.forward(1)
            mq90.turn_right(120)
            mq90.forward(1)
            mq90.land()

main()