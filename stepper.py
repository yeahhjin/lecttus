# ~ import RPi.GPIO as GPIO
# ~ import time
# ~ from RpiMotorLib import RpiMotorLib

# ~ # 핀 정의
# ~ DIR_PIN = 20
# ~ STEP_PIN = 21
# ~ GPIO_PINS = (14, 15, 18)  # MS1, MS2, MS3 핀 → 모두 LOW = Full step

# ~ # GPIO 설정
# ~ GPIO.setmode(GPIO.BCM)
# ~ GPIO.setwarnings(False)

# ~ # 모터 객체 생성
# ~ motor = RpiMotorLib.A4988Nema(DIR_PIN, STEP_PIN, GPIO_PINS, "A4988")

# ~ try:
    # ~ while True:
        # ~ print("▶️ 시계방향 60도 회전")
        # ~ motor.motor_go(clockwise=True,
                       # ~ steps=34,             # 60도 = 약 34스텝
                       # ~ stepdelay=2/34,       # 2초 동안 회전
                       # ~ verbose=False,
                       # ~ initdelay=0.05)
        # ~ time.sleep(1)

        # ~ print("◀️ 반시계방향 60도 회전")
        # ~ motor.motor_go(clockwise=False,
                       # ~ steps=34,
                       # ~ stepdelay=2/34,
                       # ~ verbose=False,
                       # ~ initdelay=0.05)
        # ~ time.sleep(1)

# ~ except KeyboardInterrupt:
    # ~ print("\n[INFO] 종료됨. GPIO 정리 중...")
    # ~ GPIO.cleanup()
import RPi.GPIO as GPIO
import time

IN1 = 12
IN2 = 16
IN3 = 20
IN4 = 21

GPIO.setmode(GPIO.BCM)
GPIO.setup(IN1, GPIO.OUT)
GPIO.setup(IN2, GPIO.OUT)
GPIO.setup(IN3, GPIO.OUT)
GPIO.setup(IN4, GPIO.OUT)

# 8-step full sequence
seq = [
    [1,0,0,1],
    [1,0,0,0],
    [1,1,0,0],
    [0,1,0,0],
    [0,1,1,0],
    [0,0,1,0],
    [0,0,1,1],
    [0,0,0,1]
]

def move_steps(delay, steps, direction=1):
    sequence = seq if direction == 1 else list(reversed(seq))
    for i in range(steps//8):
        for step in sequence:
            GPIO.output(IN1, step[0])
            GPIO.output(IN2, step[1])
            GPIO.output(IN3, step[2])
            GPIO.output(IN4, step[3])
            time.sleep(delay)
    stop_motor()

def stop_motor():
    GPIO.output(IN1,GPIO.LOW)
    GPIO.output(IN2,GPIO.LOW)
    GPIO.output(IN3,GPIO.LOW)
    GPIO.output(IN4,GPIO.LOW)
    
    

            
            
                
try:
    delay = 0.005  # 느리게 테스트
    steps_120 = [134,140,137]
    steps_360 = 411
    
    
    
    while True:
        for i, steps_count in enumerate(steps_120):
             
            move_steps(delay, steps_count,direction=1)
            time.sleep(10)
        
        move_steps(delay, steps_360, direction=-1)
        time.sleep(10)
    
except KeyboardInterrupt:
    print("중단됨")

finally:
    GPIO.cleanup()

