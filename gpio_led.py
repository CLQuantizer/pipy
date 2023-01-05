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
def celebrate():
    for t in range(3):
        display(255, l)
        sleep(0.8)
        display(0, l)
        sleep(0.8)
    
while True:
    for i in range(256):
        display(i, l)
        if i==255:
            celebrate();
        else:
            sleep(0.15)
    # reverse the thing
    for j in range(256):
        display(255-j, l)
        if j==255:
            celebrate()
        else:
            sleep(0.15)

        
