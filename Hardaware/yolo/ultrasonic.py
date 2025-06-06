"""
This Raspberry Pi code was developed by newbiely.com
This Raspberry Pi code is made available for public use without any restriction
For comprehensive instructions and wiring diagrams, please visit:
https://newbiely.com/tutorials/raspberry-pi/raspberry-pi-ultrasonic-sensor-piezo-buzzer
"""


import RPi.GPIO as GPIO
import time

# GPIO pin numbers for the ultrasonic sensor
TRIG_PIN = 23
ECHO_PIN = 24

# GPIO pin number for the piezo buzzer
BUZZER_PIN = 6

# Threshold distance in centimeters
THRESHOLD_DISTANCE_CM = 120

def get_distance():
    GPIO.output(TRIG_PIN, GPIO.HIGH)
    time.sleep(0.00001)
    GPIO.output(TRIG_PIN, GPIO.LOW)

    while GPIO.input(ECHO_PIN) == 0:
        pulse_start = time.time()

    while GPIO.input(ECHO_PIN) == 1:
        pulse_end = time.time()

    pulse_duration = pulse_end - pulse_start
    speed_of_sound = 34300  # Speed of sound in cm/s
    distance = (pulse_duration * speed_of_sound) / 2
    return distance


GPIO.setmode(GPIO.BCM)

GPIO.setup(TRIG_PIN, GPIO.OUT)
GPIO.setup(ECHO_PIN, GPIO.IN)
GPIO.setup(BUZZER_PIN, GPIO.OUT)

GPIO.output(TRIG_PIN, GPIO.LOW)
GPIO.output(BUZZER_PIN, GPIO.LOW)

def ultrasonic2():
    try:
        while True:
            distance = get_distance()
            print(f"Distance: {distance:.2f} cm")

            if distance < THRESHOLD_DISTANCE_CM:
                GPIO.output(BUZZER_PIN, GPIO.HIGH)  # Turn the buzzer on
            else:
                GPIO.output(BUZZER_PIN, GPIO.LOW)   # Turn the buzzer off

    except KeyboardInterrupt:
        GPIO.cleanup()

ulrasonic2()
