import RPi.GPIO as GPIO
import time

# 핀 번호 정의
ENA_PIN = 25
IN1_PIN = 8
IN2_PIN = 7

# GPIO 설정
GPIO.setmode(GPIO.BCM)
GPIO.setup(ENA_PIN, GPIO.OUT)
GPIO.setup(IN1_PIN, GPIO.OUT)
GPIO.setup(IN2_PIN, GPIO.OUT)

def actuator_full_down():
    print('액추에이터 하강 시작')
    GPIO.output(ENA_PIN, GPIO.HIGH)    # 모터에 전원 공급
    GPIO.output(IN1_PIN, GPIO.LOW)     # IN1 LOW
    GPIO.output(IN2_PIN, GPIO.HIGH)    # IN2 HIGH → 하강 방향
    time.sleep(20)                      # 작동 시간 (초)
    GPIO.output(ENA_PIN, GPIO.LOW)     # 모터 정지
    GPIO.output(IN1_PIN, GPIO.LOW)
    GPIO.output(IN2_PIN, GPIO.LOW)
    print('액추에이터 하강 완료')

# 함수 실행 (테스트용)
if __name__ == "__main__":
    try:
        actuator_full_down()
    finally:
        GPIO.cleanup()  # GPIO 핀 정리
    
