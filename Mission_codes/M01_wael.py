#___________________________________________________________________________
from Main import fullbot

async def wael():
    robot = fullbot()
    '''await motor_pair.move_for_degrees(robot.wheels, robot.mmtod(650), 0, velocity=250)
    await motor_pair.move_tank_for_degrees(robot.wheels, 78, 200, 400)
    await motor_pair.move_for_degrees(robot.wheels,-robot.mmtod(650),0,velocity=250)'''
    '''await robot.straight.drive(650,250)
        #await robot.turn.Larc_turn(5, 200)
        await robot.straight.drive(-650,250)'''
    robot.straight.drive(600,500)
    robot.turn.Larc_turn(60, 200)
    robot.turn.Larc_turn(-60, 200)
    robot.straight.drive(-650,1000)
#___________________________________________________________________________