#___________________________________________________________________________
from robot_base import fullbot

def teemo():
    robot = fullbot()
    # Move out of start area 380mm
    robot.straight.drive(380, 250)
    # Make a big forward right turn (280mm inner radius, 180 degrees)
    robot.turn.Rwturn(round(280*.25), 180, 250)
    # Push the ants
    robot.straight.drive(215, 130)
    #___________________________________________________________________________
    