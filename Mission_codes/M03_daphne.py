#___________________________________________________________________________
async def daphne():
    robot = fullbot()
    await robot.straight.drive(300,100)
    await robot.time.stop()
    await robot.time.wait(200)
    await robot.straight.drive(350,-100)
#___________________________________________________________________________
