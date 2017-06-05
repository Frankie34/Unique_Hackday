import RPi.GPIO
import time
import pykeyboard

R,G,B,X=15,18,14,12

btnR,btnG,btnB,btnX=21,20,16,17

RPi.GPIO.setmode(RPi.GPIO.BCM)

RPi.GPIO.setup(R,RPi.GPIO.OUT)
RPi.GPIO.setup(G,RPi.GPIO.OUT)
RPi.GPIO.setup(B,RPi.GPIO.OUT)
RPi.GPIO.setup(X,RPi.GPIO.OUT)

RPi.GPIO.setup(btnR, RPi.GPIO.IN, pull_up_down=RPi.GPIO.PUD_UP)
RPi.GPIO.setup(btnG, RPi.GPIO.IN, pull_up_down=RPi.GPIO.PUD_UP)
RPi.GPIO.setup(btnB, RPi.GPIO.IN, pull_up_down=RPi.GPIO.PUD_UP)
RPi.GPIO.setup(btnX, RPi.GPIO.IN, pull_up_down=RPi.GPIO.PUD_up)

button_1 = PyKeyboard()
button_2 = PyKeyboard()
button_3 = PyKeyboard()
button_4 = PyKeyboard()

try:

    RPi.GPIO.output(R, True)
    RPi.GPIO.output(G, True)
    RPi.GPIO.output(B, True)
    while True:
        time.sleep(0.01)
        if (RPi.GPIO.input(btnR) == 0):
            RPi.GPIO.output(R, False)
            button_1.press_key('W')
        else:
            RPi.GPIO.output(R, True)
            button_1.release_key('W')
        if (RPi.GPIO.input(btnG) == 0):
            RPi.GPIO.output(G, False)
            button_2.press_key('S')
        else:
            RPi.GPIO.output(G, True)
            button_1.release_key('S')
        if (RPi.GPIO.input(btnB) == 0):
            RPi.GPIO.output(B, False)
            button_3.press_key('A')
        else:
            RPi.GPIO.output(B, True)
            button_1.release_key('A')
        if (RPi.GPIO.input(btnX) == 0):
            RPi.GPIO.output(X, True)
            button_4.press_key('D')
        else:
            RPi.GPIO.output(X, True)
            button_1.release_key('Dz')

except KeyboardInterrupt:
    pass

RPi.GPIO.cleanup()




