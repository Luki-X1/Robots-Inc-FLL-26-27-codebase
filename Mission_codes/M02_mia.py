#___________________________________________________________________________
from robot_base import fullbot

def mia():
    robot = fullbot()
    robot.straight.drive(230, 250)
    robot.turn.Lwturn(158, 130, 250)
    robot.turn.Ltturn(90, 250)
    robot.straight.drive(430, 250)
    #430 forward wide turn angle of 170 radius of 120 arc turn 90 300 out
# forward 230mm wide turn angl 130 radius of 158 forward 100mm thank turn 90deg forward 300mm
#___________________________________________________________________________
