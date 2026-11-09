#___________________________________________________________________________
async def teemo():
    robot = fullbot()
    loci = 280
    #move out of start area 380mm
    #await motor_pair.move_tank_for_degrees(motor_pair.PAIR_1, round(380/mmpd), 250, 250)
    await robot.straight.drive(380,250)
    incirc = loci*2*pi
    outcirc = (loci+robot.trackwidth)*2*pi
    inarc = incirc/2
    outarc = outcirc/2
    ratio = inarc/outarc

    #make a big turn
    #await motor_pair.move_tank_for_degrees(motor_pair.PAIR_1, round(inarc/mmpd), 250, round(250*ratio))
    await robot.turn.Rwturn(280,180,250)

    #Push the ants 35mm
    #await motor_pair.move_for_degrees(motor_pair.PAIR_1, round(285/mmpd), 0, velocity=180)
    await robot.straight.drive(215,130)
    #reverse
    #await motor_pair.move_for_degrees(motor_pair.PAIR_1, round(245/mmpd), 0, velocity=-170)
    await robot.straight.drive(170,-170)
    await motor_pair.move_tank_for_degrees(motor_pair.PAIR_1, -round(inarc/robot.mmpd), 250, round(250*ratio))
    #await robot.turn.Rwturn(-280,180,250)
    #await motor_pair.move_tank_for_degrees(motor_pair.PAIR_1, round(380/mmpd), -250, -250)
    await robot.straight.drive(280, -250)
#___________________________________________________________________________
