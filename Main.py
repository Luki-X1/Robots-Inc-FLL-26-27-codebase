from hub import *
import motor_pair,motor
import color_sensor,distance_sensor, runloop, color
from math import pi

motor_pair.pair(motor_pair.PAIR_1,port.D,port.C)

class robot_base_class:
    def __init__ (self):
        self.trackwidth = 120
        self.wheels = motor_pair.PAIR_1
        self.irad = 44
        self.idiam = self.irad*2
        self.icirum = self.idiam*pi
        self.mmpd = self.icirum/360
        self.mmtod = lambda mm: round(mm/self.mmpd)
        self.calc_arc = lambda angle, radius: (angle/360)*(2*radius*pi)
        self.colorcode = {
            color.RED: daphne,
            color.YELLOW: mia,
            color.MAGENTA: wael,
            color.WHITE: luke,
            color.GREEN: teemo,
            color.AZURE: noahXremiXjiggle,
            color.UNKNOWN: swapside,
        }
        self.numtolet = [
            'A','B','C','D',
            'E','F','G','H',
            'I','J','K','L',
            'M','N','O','P',
            'Q','R','S','T',
            'U','V','W','X',
            'Y','Z'
        ]

    async def colorrun (self,colorread):
        print('running colorrun on color')
        for codecolor, code in self.colorcode.items():
            if colorread == codecolor:
                runloop.run(code())
        '''if colorread == color.RED :
            runloop.run(self.colorcode['red']())
        elif colorread == color.YELLOW:
            runloop.run(self.colorcode['yellow']())'''

    async def secondary(self):
        print('starting second')
        true_set = True
        right_pressed = False
        init = False
        while true_set:
            readcolor = color_sensor.color(port.B)
            
            if readcolor == color.RED:
                light_matrix.write(self.numtolet[0])
            elif readcolor == color.AZURE:
                light_matrix.write(self.numtolet[1])
            elif readcolor == color.YELLOW:
                light_matrix.write(self.numtolet[2])
            elif readcolor == color.MAGENTA:
                light_matrix.write(self.numtolet[3])
            elif readcolor == color.GREEN:
                light_matrix.write(self.numtolet[4])
            elif readcolor == color.WHITE:
                light_matrix.write(self.numtolet[5])
            elif readcolor == color.UNKNOWN:
                light_matrix.show_image(light_matrix.IMAGE_ARROW_W)
            else:
                light_matrix.clear()

            if button.pressed(button.RIGHT) and not right_pressed and init == False:
                right_pressed = True
                sound.beep(1500, 200, 100)
                await runloop.sleep_ms(125)
                await self.colorrun(readcolor)
            elif not button.pressed(button.RIGHT):
                right_pressed = False

class straight_base_class(robot_base_class):
    def __init__(self):
        super().__init__()

    async def drive (self, dist, velo):
        await motor_pair.move_for_degrees(self.wheels, self.mmtod(dist), 0, velocity=velo)

class time_class(robot_base_class):
    def __init__(self):
        super().__init__()
    
    async def stop(self):
        motor_pair.stop(self.wheels)
    
    async def wait (self, duration):
        await runloop.sleep_ms (duration)

class turn_base_class(robot_base_class):
    def __init__(self):
        super().__init__()
    #arc turns
    async def Larc_turn (self, angle, velo):
        await motor_pair.move_tank_for_degrees(self.wheels, self.mmtod(self.calc_arc(angle, self.trackwidth)), 0, velo)
    async def Rarc_turn (self, angle, velo):
        await motor_pair.move_tank_for_degrees(self.wheels, self.mmtod(self.calc_arc(angle, self.trackwidth)), velo, 0)
    #tank turns
    async def Ltturn (self, angle, velo):
        await motor_pair.move_tank_for_degrees(self.wheels, self.mmtod(self.calc_arc(angle, self.trackwidth/2)), -velo, velo)
    async def Rtturn (self, angle, velo):
        await motor_pair.move_tank_for_degrees(self.wheels, self.mmtod(self.calc_arc(angle, self.trackwidth/2)), velo, -velo)
    #wide turns
    async def Lwturn (self, radius, angle, velo):
        r1 = radius
        r2 = radius+self.trackwidth
        await motor_pair.move_tank_for_degrees(self.wheels, self.mmtod(self.calc_arc(angle, radius)), round(velo*(r1/r2)), velo)
    async def Rwturn (self, radius, angle, velo):
        r1 = radius
        r2 = radius+self.trackwidth
        await motor_pair.move_tank_for_degrees(self.wheels, self.mmtod(self.calc_arc(angle, radius)), velo, round(velo*(r1/r2)))


class fullbot(robot_base_class):
    def __init__(self):
        super().__init__()
        self.straight = straight_base_class()
        self.turn = turn_base_class()
        self.time = time_class()
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
async def mia():
    robot = fullbot()
    await robot.straight.drive(430, 250)
    await robot.turn.Lwturn(120, 220, 250)
    await robot.turn.Ltturn(90, 250)
    await robot.straight.drive(430, 250)
    #430 forward wide turn angle of 170 radius of 120 arc turn 90 300 out
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
async def daphne():
    robot = fullbot()
    await robot.straight.drive(300,100)
    await robot.time.stop()
    await robot.time.wait(200)
    await robot.straight.drive(350,-100)
#___________________________________________________________________________
async def noahXremi():
    robot = fullbot()
    await robot.straight.drive(700,250)
    await robot.straight.drive(-700,500)
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
async def swapside():
    robot = fullbot()
    await robot.straight.drive(1650, 500)

async def main():
    bot = fullbot()
    await bot.secondary()

runloop.run(main())