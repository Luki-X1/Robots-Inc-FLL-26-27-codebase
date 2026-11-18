#___________________________________________________________________________
from robot_base import fullbot

async def daphne():
    robot = fullbot()
    await robot.straight.drive(300, 200)
    robot.time.stop()
    await robot.time.wait(200)
    await robot.straight.drive(-350, 300)
#___________________________________________________________________________