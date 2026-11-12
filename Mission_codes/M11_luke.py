#___________________________________________________________________________
async def luke():
    # write your code here
    robot = fullbot()
    '''await motor_pair.move_for_degrees(motor_pair.PAIR_1, round(440/mmpd), 0, velocity=200)
    await runloop.sleep_ms(250)
    await motor_pair.move_for_degrees(motor_pair.PAIR_1, -1*round(460/mmpd), 0, velocity=200)'''
    await robot.straight.drive(440,200)
    await robot.time.wait(250)
    await robot.straight.drive(-460,200)
#___________________________________________________________________________
