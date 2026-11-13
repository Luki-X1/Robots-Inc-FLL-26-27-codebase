#___________________________________________________________________________
from Main import fullbot

async def noahXremiXjiggle():
    robot = fullbot()
    robot.straight.drive(700, 250)
    robot.straight.drive(-400, 400)
    robot.straight.drive(150, 200)
    robot.time.wait(100)
    robot.straight.drive(-75, 200)
    robot.straight.drive(150, 200)
    robot.time.wait(100)
    robot.straight.drive(-700, 500)
#___________________________________________________________________________
