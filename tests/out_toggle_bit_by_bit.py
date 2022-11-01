import wiringpi
from time import sleep

pin_base = 65       # lowest available starting number is 65
i2c_addr = 0x20     # A0, A1, A2 pins all wired to GND
channels = 6
mcp_base = pin_base + 8

wiringpi.wiringPiSetup()                    # initialise wiringpi
wiringpi.mcp23017Setup(pin_base, i2c_addr)   # set up the pins and i2c address

for p in range(mcp_base, mcp_base+8):
    wiringpi.pinMode(p, 1)         # sets GPA0 to output
    wiringpi.digitalWrite(p, 1)    # sets GPA0 to 0 (0V, off)

try:
    while True:
        for chan in range(mcp_base, mcp_base+8):
            print("On: %d" % (chan-pin_base-7))
            wiringpi.digitalWrite(chan, 0)
            sleep(1)
            print("Off: %d" % chan)
            wiringpi.digitalWrite(chan, 1)


finally:
    for p in range(mcp_base, mcp_base+8):
        wiringpi.pinMode(p, 0)         # sets GPA0 to output
        wiringpi.digitalWrite(p, 1)    # sets GPA0 to 0 (0V, off)
