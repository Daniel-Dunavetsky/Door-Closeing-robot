from asyncio import sleep
from gpiozero import Motor
i = 0
motor1 = Motor(4,14)

motor1.forward()

while i > 30:
    motor1.forward()
    i = i+1