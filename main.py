#!/usr/bin/env pybricks-micropython

from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase

from Car import Car

def main():
    ev3 = EV3Brick()

    infra = InfraredSensor(Port.S4)
    left = Motor(Port.A)
    right = Motor(Port.D)
    arm = Motor(Port.B)
    
    car = Car(left, right, arm, infra, ev3)
    
    car.autorun()
    
    ev3.speaker.beep()

if __name__ == '__main__':
    main()
    