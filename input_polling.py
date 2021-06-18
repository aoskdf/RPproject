import RPi.GPIO as GPIO

switch= 10

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

GPIO.setup(Switch, GPIO.IN,pull_up_down=GPIO.PUD_DOWN)

while True:
    flag=0

    if GPIO.input(Switch) == GPIO.HIGH:
        print("Button was pushed!")
    else:
        print("Button was not pushed!")
    time.sleep(1)
