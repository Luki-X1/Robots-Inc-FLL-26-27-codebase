from pybricks.pupdevices import Motor, ColorSensor
from pybricks.parameters import Port

for p in [Port.A, Port.B, Port.C, Port.D, Port.E, Port.F]:
    try:
        m = Motor(p)
        print("Motor found on:", p)
    except OSError:
        pass
    try:
        c = ColorSensor(p)
        print("ColorSensor found on:", p)
    except OSError:
        pass
