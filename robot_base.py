from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor
from pybricks.parameters import Port, Direction, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait

# Initialize Hub, Motors, and Sensors once
hub = PrimeHub()
left_motor = Motor(Port.D, Direction.COUNTERCLOCKWISE)
right_motor = Motor(Port.C)
color_sensor = ColorSensor(Port.B)

drive_base = DriveBase(left_motor, right_motor, wheel_diameter=88, axle_track=120)
drive_base.use_gyro(True)


class robot_base_class:
    def __init__(self):
        self.hub = hub
        self.db = drive_base
        self.sensor = color_sensor
        self.trackwidth = 120


class straight_base_class(robot_base_class):
    def drive(self, dist, velo):
        self.db.settings(straight_speed=abs(velo))
        self.db.straight(dist, then=Stop.COAST)


class time_class(robot_base_class):
    def stop(self):
        self.db.stop()

    def wait(self, duration):
        wait(duration)


class turn_base_class(robot_base_class):
    def Ltturn(self, angle, velo):
        self.db.settings(turn_rate=abs(velo))
        self.db.turn(-angle)

    def Rtturn(self, angle, velo):
        self.db.settings(turn_rate=abs(velo))
        self.db.turn(angle)

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
