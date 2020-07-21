#Funtions to control 28BYJ-48 stepper motor with ULN2003AN driver board 
import RPi.GPIO as GPIO 
from time import sleep

STEPPER_PIN_1 = 32
STEPPER_PIN_2 = 36
STEPPER_PIN_3 = 38
STEPPER_PIN_4 = 40

GPIO.setmode(GPIO.BOARD)
GPIO.setup(STEPPER_PIN_1, GPIO.OUT)
GPIO.setup(STEPPER_PIN_2, GPIO.OUT)
GPIO.setup(STEPPER_PIN_3, GPIO.OUT)
GPIO.setup(STEPPER_PIN_4, GPIO.OUT)

step_number = 0

def OneStep(dir):
    global step_number
    
    if(dir) and (step_number == 0):
        GPIO.output(STEPPER_PIN_1, 1)
        GPIO.output(STEPPER_PIN_2, 0)
        GPIO.output(STEPPER_PIN_3, 0)
        GPIO.output(STEPPER_PIN_4, 0)
    elif(dir) and (step_number == 1):
        GPIO.output(STEPPER_PIN_1, 0)
        GPIO.output(STEPPER_PIN_2, 1)
        GPIO.output(STEPPER_PIN_3, 0)
        GPIO.output(STEPPER_PIN_4, 0)
    elif(dir) and (step_number == 2):
        GPIO.output(STEPPER_PIN_1, 0)
        GPIO.output(STEPPER_PIN_2, 0)
        GPIO.output(STEPPER_PIN_3, 1)
        GPIO.output(STEPPER_PIN_4, 0)
    elif(dir) and (step_number == 3):
        GPIO.output(STEPPER_PIN_1, 0)
        GPIO.output(STEPPER_PIN_2, 0)
        GPIO.output(STEPPER_PIN_3, 0)
        GPIO.output(STEPPER_PIN_4, 1)
    elif(not dir) and (step_number == 0):
        GPIO.output(STEPPER_PIN_1, 0)
        GPIO.output(STEPPER_PIN_2, 0)
        GPIO.output(STEPPER_PIN_3, 0)
        GPIO.output(STEPPER_PIN_4, 1)
    elif(not dir) and (step_number == 1):
        GPIO.output(STEPPER_PIN_1, 0)
        GPIO.output(STEPPER_PIN_2, 0)
        GPIO.output(STEPPER_PIN_3, 1)
        GPIO.output(STEPPER_PIN_4, 0)
    elif(not dir) and (step_number == 2):
        GPIO.output(STEPPER_PIN_1, 0)
        GPIO.output(STEPPER_PIN_2, 1)
        GPIO.output(STEPPER_PIN_3, 0)
        GPIO.output(STEPPER_PIN_4, 0)
    elif(not dir) and (step_number == 3):
        GPIO.output(STEPPER_PIN_1, 1)
        GPIO.output(STEPPER_PIN_2, 0)
        GPIO.output(STEPPER_PIN_3, 0)
        GPIO.output(STEPPER_PIN_4, 0)

    step_number = step_number + 1
    if(step_number > 3):
        step_number = 0

if __name__ == "__main__":
    while(1):
        OneStep(0)
        sleep(0.002)