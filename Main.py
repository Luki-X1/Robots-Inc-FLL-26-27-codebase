from pybricks.parameters import Color, Button, Icon
from pybricks.tools import wait
from robot_base import fullbot

from Mission_codes.M01_wael import wael
from Mission_codes.M02_mia import mia
from Mission_codes.M03_daphne import daphne
from Mission_codes.M06_teemo import teemo
from Mission_codes.M07_noahXremiXjiggle import noahXremiXjiggle
from Mission_codes.M11_luke import luke
from Mission_codes.M_UND_swapside import swapside


class mission_selector(fullbot):
    def __init__(self):
        super().__init__()
        self.colorcode = {
            Color.RED: daphne,
            Color.YELLOW: mia,
            Color.MAGENTA: wael,
            Color.WHITE: luke,
            Color.GREEN: teemo,
            Color.BLUE: noahXremiXjiggle,
            Color.NONE: swapside,
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


if __name__ == "__main__":
    bot = mission_selector()
    bot.secondary()
