#___________________________________________________________________________
from robot_base import fullbot

async def noahXremiXjiggle():
    robot = fullbot()
    await robot.straight.drive(800, 250)
    await robot.straight.drive(-200, 300)
    await robot.straight.drive(100, 200)
    await robot.time.wait(500)
    await robot.straight.drive(-700, 500)
#___________________________________________________________________________