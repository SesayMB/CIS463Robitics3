import machine

from machine import Pin
import time
import gc

TRIG_PIN = 14
ECHO_PIN = 12
GREEN_PIN = 16
RED_PIN = 5

SOUND_VELOCITY = 0.034

trigger = Pin(TRIG_PIN, Pin.OUT, pull=None)
echo = Pin(ECHO_PIN, Pin.IN, pull=None)

green_lt = Pin(GREEN_PIN, Pin.OUT)
red_lt = Pin(RED_PIN, Pin.OUT)

sensor = HCSR04(trigger_pin=12, echo_pin=14, echo_timeout_us=10000)
def get_pulse_time():
    trigger.value(0)
    time.sleep_us(5)
    trigger.value(1)
    time.sleep_us(10)
    trigger.value(0)
#    return machine.time_pulse_us(echo, 1)
    try:
        pulse_time = machine.time_pulse_us(echo, 1)
        return pulse_time
    except OSSError as ex:
        if ex.args[0] == 110:
            raise OSError('Out of Range')
        raise ex
    
    
from machine import Pin
from time import sleep


while True:
  gc.collect()
  distance = sensor.distance_cm()
  print('Distance:', distance, 'cm')
  if distance >10:  
      green_lt.on()
      sleep(0.4)
      green_lt.off()
      sleep(0.8)
  if distance < 10:
      red_lt.on()
      sleep(0.4)
      red_lt.off()
      sleep(0.8)
  