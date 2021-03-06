'''
Fades an externally connected LED to D13 of nRF52840 feather sense from off to on in 10% increments using the range function.
Written by Beverly Wilt (beverly.wilt@sjsu.edu) 
'''

import board
import pulseio
import time

PIN_LEDPWM = board.D13

led = pulseio.PWMOut(PIN_LEDPWM)

# Turn on LED at the specify brightness level

def led_level(level):
    led.duty_cycle = int((0.1*level)*((2**16)-1))

while True:
    for brightness in range(0,11,1):
        # fade from off to on
        led_level(brightness)
        time.sleep(0.1)
    for brightness in range(10,-1,-1):
        # fade from on to off
        led_level(brightness)
        time.sleep(0.1)
