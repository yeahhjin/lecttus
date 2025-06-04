"""
This Raspberry Pi code was developed by newbiely.com
This Raspberry Pi code is made available for public use without any restriction
For comprehensive instructions and wiring diagrams, please visit:
https://newbiely.com/tutorials/raspberry-pi/raspberry-pi-actuator
"""

'''
import RPi.GPIO as GPIO
import time

# Constants
ENA_PIN = 25  # GPIO pin connected to the EN1 pin L298N
IN1_PIN = 8  # GPIO pin connected to the IN1 pin L298N
IN2_PIN = 7  # GPIO pin connected to the IN2 pin L298N

# Setup
GPIO.setmode(GPIO.BCM)
GPIO.setup(ENA_PIN, GPIO.OUT)
GPIO.setup(IN1_PIN, GPIO.OUT)
GPIO.setup(IN2_PIN, GPIO.OUT)
GPIO.output(ENA_PIN, GPIO.HIGH)

GPIO.output(IN1_PIN, GPIO.HIGH)
GPIO.output(IN2_PIN, GPIO.LOW)
time.sleep(10)
'''
"""
This Raspberry Pi code was developed by newbiely.com
Modified to measure time actuator takes to fully retract
"""

import RPi.GPIO as GPIO
import time

ENA_PIN = 25
IN1_PIN = 8
IN2_PIN = 7

GPIO.setmode(GPIO.BCM)
GPIO.setup(ENA_PIN, GPIO.OUT)
GPIO.setup(IN1_PIN, GPIO.OUT)
GPIO.setup(IN2_PIN, GPIO.OUT)

GPIO.output(ENA_PIN, GPIO.HIGH)

try:
	### select one way
    print("reverse 테스트")
    start_time = time.time()
    GPIO.output(IN1_PIN, GPIO.LOW)
    GPIO.output(IN2_PIN, GPIO.HIGH)
    #time.sleep(16)
    
    print("forward 테스트")
    start_time = time.time()
    GPIO.output(IN1_PIN, GPIO.HIGH)
    GPIO.output(IN2_PIN, GPIO.LOW)
    #time.sleep(16)
    
    # 무한 루프: 사용자 수동 종료 기다림
    while True:
        time.sleep(0.1)

except KeyboardInterrupt:
    end_time = time.time()
    elapsed = end_time - start_time
    print(f"\n[RESULT] 액추에이터가 최대한으로 밀리는 데 걸린 시간: {elapsed:.2f}초")


finally:
    GPIO.output(ENA_PIN, GPIO.LOW)
    GPIO.output(IN1_PIN, GPIO.LOW)
    GPIO.output(IN2_PIN, GPIO.LOW)
    GPIO.cleanup()


