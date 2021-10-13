import time
import math
from adafruit_circuitplayground.express import cpx

if not cpx.switch:
    file = open("Data.txt", "w")

    while True:

        if not cpx.switch:
            readingsCount = -1
            readings = []
            if cpx.button_a:
                readingsCount = 0
                while readingsCount >= 0 and readingsCount < 100:
                    cpx.red_led = True
                    x, y, z = cpx.acceleration
                    g = math.sqrt(x * x + y * y + z * z)
                    readings.append(g / 1000)
                    readingsCount += 1
                    time.sleep(0.05)
                    cpx.red_led = False
                file.write(str(readings))
        else:
            print("Not logging data. Flip the switch and then hit reset")
            time.sleep(3)
