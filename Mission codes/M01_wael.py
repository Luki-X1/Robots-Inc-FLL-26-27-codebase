#___________________________________________________________________________
async def wael():
    robot = fullbot()
    '''await motor_pair.move_for_degrees(robot.wheels, robot.mmtod(650), 0, velocity=250)
    await motor_pair.move_tank_for_degrees(robot.wheels, 78, 200, 400)
    await motor_pair.move_for_degrees(robot.wheels,-robot.mmtod(650),0,velocity=250)'''
    await robot.straight.drive(650,250)
    #await robot.turn.Larc_turn(5, 200)
    await robot.straight.drive(-650,250)
#___________________________________________________________________________
