
import wiringpi
from time import sleep

pin_base = 65       # lowest available starting number is 65
i2c_addr = 0x20     # A0, A1, A2 pins all wired to GND

wiringpi.wiringPiSetup()                    # initialise wiringpi
wiringpi.mcp23017Setup(pin_base,i2c_addr)   # set up the pins and i2c address


wiringpi.pinMode(65, 0)         # sets GPB7 to input
wiringpi.pullUpDnControl(65, 2) # set internal pull-up

# Note: MCP23017 has no internal pull-down, so I used pull-up and inverted
# the button reading logic with a "not"

try:
    while True:
        print ( '%d%d%d%d%d%d%d%d'%(
		wiringpi.digitalRead(65),wiringpi.digitalRead(66),
		wiringpi.digitalRead(67),wiringpi.digitalRead(68),
		wiringpi.digitalRead(69),wiringpi.digitalRead(70),
		wiringpi.digitalRead(71),wiringpi.digitalRead(72)))
        sleep(0.05)
finally:
    wiringpi.pinMode(65, 0)      # sets GPIO GPA1 back to input Mode
    # GPB7 is already an input, so no need to change anything

