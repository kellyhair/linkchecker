import syslog
import time
import RPi.GPIO as GPIO
import pyping # requires the installation of pyping - "pip install pyping"

link_description = "Frontier DSL"

GPIO_PIN_TYPE = "BCM" # Either BCM or BOARD.  BOARD = physical pin numbers
GPIO_PIN = 4 # GPIO ping on RPi to send signal. 


Time_to_power_off = 10 # How long we will turn off the device.
Time_to_allow_Initialization = 30 # How long we wait after powering on 
# Missed_Ping = 0
Host1 = "8.8.8.8" # Google DNS
Host2 = "www.cnn.com" #likely will resolve to Fastly but this ends up testing DNS too..

#Setup the Raspberry Pi to 

GPIO.setmode(GPIO.GPIO_PIN_TYPE)
GPIO.setup(GPIO_PIN, GPIO.OUT)
GPIO.output(GPIO_PIN, 0)
    
def reboot_device():
  syslog.syslog("%s service will now reboot" % link_description)
  GPIO.output(GPIO_PIN, 1)
  # CODE TO SEND OFF SIGNAL TO POWERTAIL/IOT AC/DC RELAY 
  time.sleep(Time_to_power_off)
  GPIO.output(GPIO_PIN, 0)
  # CODE TO SEND ON SIGNAL TO POWERTAIL/IOT AC/DC RELAY 
  syslog.syslog("%s service rebooted. Waiting %d seconds to initialize " % ( 
      link_description, Time_to_allow_Initialization))
  time.sleep(Time_to_allow_Initialization)
  syslog.syslog("%s service initialized; returning to testing" % link_description )
  
#Main loop here: 

while True:
    ping1 = pyping.ping(Host1)
    
    if ping1.ret_code == 0:
        # Missed_Ping = Missed_Ping + 1
        syslog.syslog("%s is not responding. Trying 2nd host" % link_description)

        ping2 = pyping.ping(Host2)
        
        if ping2.ret_code == 0:
            syslog.syslog ("%s we are down! Calling reboot procedure" % link_description )
            reboot_device()
        

