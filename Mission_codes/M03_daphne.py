#___________________________________________________________________________
from Main import fullbot

async def daphne():
    robot = fullbot()
    robot.straight.drive(300,100)
    robot.time.stop()
    robot.time.wait(200)
    robot.straight.drive(350,-100)
#___________________________________________________________________________
