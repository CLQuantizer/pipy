from gpiozero import LED
from time import sleep

# declare the ligts
l = []
for num in [17, 16, 21, 20, 12, 24, 23, 18]:
    l.append(LED(num))

def display(i: int, lights):
    for (j,led) in enumerate(lights):
        if 2**j&i==2**j:
            led.on()
        else:
            led.off()
while True:
    for i in range(124):
        display(i, l)
        sleep(0.3)
