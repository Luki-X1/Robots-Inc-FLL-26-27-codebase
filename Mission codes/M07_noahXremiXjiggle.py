#___________________________________________________________________________
async def noahXremiXjiggle():
    robot = fullbot()
    await robot.straight.drive(700,250)
    await robot.straight.drive(-400,400)
    await robot.straight.drive(150,200)
    await runloop.sleep_ms(100)
    await robot.straight.drive(-75,200)
    await robot.straight.drive(150,200)
    await runloop.sleep_ms(100)
    await robot.straight.drive(-700,500)
#___________________________________________________________________________
