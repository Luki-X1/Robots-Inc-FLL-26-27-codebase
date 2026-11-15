from pybricks.parameters import Color, Button, Icon
from pybricks.tools import wait, multitask, run_task
from robot_base import fullbot

from Mission_codes.M01_wael import wael
from Mission_codes.M02_mia import mia
from Mission_codes.M03_daphne import daphne
from Mission_codes.M06_teemo import teemo
from Mission_codes.M07_noahXremiXjiggle import noahXremiXjiggle
from Mission_codes.M11_luke import luke
from Mission_codes.M_UND_swapside import swapside

from music import *

class mission_selector(fullbot):
    def __init__(self):
        super().__init__()
        self.colorcode = {
            Color.RED: [daphne, haydn_104_opening],
            Color.YELLOW: [mia, haydn_104_opening],
            Color.MAGENTA: [wael, haydn_104_opening],
            Color.WHITE: [luke, haydn_104_opening],
            Color.ORANGE: [teemo, ants_go_marching],
            Color.BLUE: [noahXremiXjiggle, final_countdown],
            Color.NONE: [swapside, haydn_104_opening],
        }
        self.numtolet = [
            'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
            'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
            'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X',
            'Y', 'Z'
        ]

    async def _run_mission_task(self, mission_func):
        await mission_func()

    def colorrun(self, colorread):
        print('running colorrun on color:', colorread)
        if colorread in self.colorcode:
            mission_func = self.colorcode[colorread][0]
            song = self.colorcode[colorread][1]
            # Runs the mission and background music simultaneously; stops music as soon as the mission finishes
            run_task(multitask(
                self._run_mission_task(mission_func),
                song.play_background(gap=50, loop=True),
                race=True
            ))
            self.hub.speaker.beep(0,0)

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
            elif readcolor == Color.ORANGE:
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

            readcolor = self.sensor.color()
            print(readcolor, self.sensor.hsv())
            wait(20)

if __name__ == "__main__":
    bot = mission_selector()
    bot.secondary()
