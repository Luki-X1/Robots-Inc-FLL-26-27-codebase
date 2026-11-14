#___________________________________________________________________________
from robot_base import fullbot

def teemo():
    robot = fullbot()
    # Move out of start area 380mm
    robot.straight.drive(400, 250)
    # Make a big forward right turn (280mm inner radius, 180 degrees)
    robot.turn.Rwturn(280, 75, 250)
    #move attachment
    robot.front_attach.run_angle(500, 200)
    #finish big
    robot.turn.Rwturn(280, 60, 250)
    # Push the ants
    robot.straight.drive(200, 130)
    '''# Reverse straight
    robot.straight.drive(-170, 170)
    # Reverse back along the exact same wide curve (-180 degrees)
    robot.turn.Rwturn(280, -180, 250)
    # Reverse back into start area
    robot.straight.drive(280, -250)'''
    #___________________________________________________________________________
