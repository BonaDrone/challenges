import time
import cflib.crtp
from cflib.crazyflie.syncCrazyflie import SyncCrazyflie
from cflib.positioning.motion_commander import MotionCommander

URI = 'radio://0/80/2M'

valueToMove = 1
valueGoForwardBig = 1.5
totalDegreesTurnRight = 135
valueGoForwardSmall = 0.71

def main():
    cflib.crtp.init_drivers(enable_debug_driver=False)

    with SyncCrazyflie(URI) as scf:
        with MotionCommander(scf) as mq90:
            mq90.up(valueToMove)
            mq90.forward(valueGoForwardBig)
            mq90.turn_right(totalDegreesTurnRight)
            mq90.forward(valueGoForwardSmall)
            mq90.land()

main()