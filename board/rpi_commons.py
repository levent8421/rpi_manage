try:
    from RPi import GPIO
except ImportError:
    GPIO = None


def check_rpi():
    return GPIO is not None


# init gpio mode
if check_rpi():
    GPIO.setmode(GPIO.BCM)
