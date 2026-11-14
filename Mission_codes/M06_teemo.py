#___________________________________________________________________________
from robot_base import fullbot

async def teemo():
    robot = fullbot()
    # Move out of start area 380mm
    await robot.straight.drive(400, 250)
    # Make a big forward right turn (280mm inner radius, 180 degrees)
    await robot.turn.Rwturn(280, 75, 250)
    #move attachment
    await robot.front_attach.run_angle(500, 200)
    #finish big
    await robot.turn.Rwturn(280, 60, 250)
    # Push the ants
    await robot.straight.drive(200, 120)
    #back up 150 mm
    await robot.straight.drive(-150, 250)
    #turn 25 degrees right
    await robot.turn.Rtturn(28, 220)
    #go forward to fungus
    await robot.straight.drive(225, 175)
    await robot.time.wait(1000)
    #turn 40 degrees right to pull fungus
    await robot.turn.Rtturn(45, 300)
    await robot.turn.Rtturn(-45, 175)#--| jiggle out fungus
    await robot.turn.Rtturn(45, 300)# --|
    '''# Reverse straight
    robot.straight.drive(-170, 170)
    # Reverse back along the exact same wide curve (-180 degrees)
    robot.turn.Rwturn(280, -180, 250)
    # Reverse back into start area
    robot.straight.drive(280, -250)'''
    #___________________________________________________________________________