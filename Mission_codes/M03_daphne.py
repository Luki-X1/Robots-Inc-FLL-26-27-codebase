#___________________________________________________________________________
from robot_base import fullbot

def daphne():
    robot = fullbot()
    robot.straight.drive(300, 200)
    robot.time.stop()
    robot.time.wait(200)
    robot.straight.drive(-350, 300)
#___________________________________________________________________________
