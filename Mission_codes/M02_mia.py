#___________________________________________________________________________
from robot_base import fullbot

def mia():
    robot = fullbot()
    robot.straight.drive(430, 250)
    robot.turn.Lwturn(120, 220, 250)
    robot.turn.Ltturn(90, 250)
    robot.straight.drive(430, 250)
    #430 forward wide turn angle of 170 radius of 120 arc turn 90 300 out
#___________________________________________________________________________
