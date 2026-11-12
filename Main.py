from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor
from pybricks.parameters import Port, Direction, Color, Button, Icon
from pybricks.robotics import DriveBase
from pybricks.tools import wait

from Mission_codes.M01_wael import wael
from Mission_codes.M02_mia import mia
from Mission_codes.M03_daphne import daphne
from Mission_codes.M06_teemo import teemo
from Mission_codes.M07_noahXremiXjiggle import noahXremiXjiggle
from Mission_codes.M11_luke import luke
from Mission_codes.M_UND_swapside import swapside

# Initialize Hub, Motors, and Sensors once
hub = PrimeHub()
left_motor = Motor(Port.D, Direction.COUNTERCLOCKWISE)
right_motor = Motor(Port.C)
color_sensor = ColorSensor(Port.B)

# wheel_diameter = 88 (irad 44 * 2), axle_track = 120
drive_base = DriveBase(left_motor, right_motor, wheel_diameter=88, axle_track=120)
drive_base.use_gyro(True)


class robot_base_class:
    def __init__(self):
        self.hub = hub
        self.db = drive_base
        self.sensor = color_sensor
        self.trackwidth = 120

        self.colorcode = {
            Color.RED: daphne,
            Color.YELLOW: mia,
            Color.MAGENTA: wael,
            Color.WHITE: luke,
            Color.GREEN: teemo,
            Color.BLUE: noahXremiXjiggle,  # Pybricks uses Color.BLUE instead of AZURE
            Color.NONE: swapside,          # Pybricks uses Color.NONE instead of UNKNOWN
        }
        self.numtolet = [
            'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
            'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
            'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X',
            'Y', 'Z'
        ]

    def colorrun(self, colorread):
        print('running colorrun on color:', colorread)
        if colorread in self.colorcode:
            self.colorcode[colorread]()

    def secondary(self):
        print('starting second')
        right_pressed = False

        while True:
            readcolor = self.sensor.color()

            if readcolor == Color.RED:
                self.hub.display.char(self.numtolet[0])
            elif readcolor == Color.BLUE:
                self.hub.display.char(self.numtolet[1])
            elif readcolor == Color.YELLOW:
                self.hub.display.char(self.numtolet[2])
            elif readcolor == Color.MAGENTA:
                self.hub.display.char(self.numtolet[3])
            elif readcolor == Color.GREEN:
                self.hub.display.char(self.numtolet[4])
            elif readcolor == Color.WHITE:
                self.hub.display.char(self.numtolet[5])
            elif readcolor == Color.NONE:
                self.hub.display.icon(Icon.ARROW_LEFT)
            else:
                self.hub.display.off()

            pressed = self.hub.buttons.pressed()
            if Button.RIGHT in pressed and not right_pressed:
                right_pressed = True
                self.hub.speaker.beep(1500, 200)
                wait(125)
                self.colorrun(readcolor)
            elif Button.RIGHT not in pressed:
                right_pressed = False

            wait(20)


class straight_base_class(robot_base_class):
    def drive(self, dist, velo):
        # Set straight speed (mm/s) and drive distance (mm)
        self.db.settings(straight_speed=abs(velo))
        self.db.straight(dist)


class time_class(robot_base_class):
    def stop(self):
        self.db.stop()

    def wait(self, duration):
        wait(duration)


class turn_base_class(robot_base_class):
    # Tank (in-place) turns
    def Ltturn(self, angle, velo):
        self.db.settings(turn_rate=abs(velo))
        self.db.turn(-angle)

    def Rtturn(self, angle, velo):
        self.db.settings(turn_rate=abs(velo))
        self.db.turn(angle)

    # Wide turns: positive angle = forward curve, negative angle = backward curve
    def Lwturn(self, radius, angle, velo):
        self.db.settings(straight_speed=abs(velo))
        self.db.curve(abs(radius) + (self.trackwidth / 2), -angle)

    def Rwturn(self, radius, angle, velo):
        self.db.settings(straight_speed=abs(velo))
        self.db.curve(abs(radius) + (self.trackwidth / 2), angle)

    def Larc_turn(self, angle, velo):
        self.Lwturn(0, angle, velo)

    def Rarc_turn(self, angle, velo):
        self.Rwturn(0, angle, velo)

class fullbot(robot_base_class):
    def __init__(self):
        super().__init__()
        self.straight = straight_base_class()
        self.turn = turn_base_class()
        self.time = time_class()


if __name__ == "__main__":
    bot = fullbot()
    bot.secondary()