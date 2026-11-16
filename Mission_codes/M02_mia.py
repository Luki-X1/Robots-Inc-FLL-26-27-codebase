#___________________________________________________________________________
from robot_base import fullbot

async def mia():
    robot = fullbot()
    await robot.straight.drive(430, 250)
    await robot.turn.Lwturn(140, 110, 250)
    await robot.turn.Ltturn(90, 250)
    await robot.straight.drive(450, 250)
    #430 forward wide turn angle of 170 radius of 120 arc turn 90 300 out
#___________________________________________________________________________