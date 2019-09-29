from .definition import *


class Pin:
    def __init__(self, pin, mode=OUT, value=LOW):
        self.pin = pin
        self.mode = mode
        self.value = value
        self.ready = False

    def set(self, value):
        self.value = value
        if check_rpi():
            GPIO.output(self.pin, value)

    def high(self):
        self.set(HIGH)

    def low(self):
        self.set(LOW)

    def reverse(self):
        if self.value == HIGH:
            self.low()
        else:
            self.high()

    def is_high(self):
        return self.value == HIGH

    def is_low(self):
        return self.value == LOW

    def change_mode(self, mode):
        if self.mode == mode:
            return
        self.mode = mode
        self.ready = False
        self.setup()

    def setup(self):
        if self.ready:
            if check_rpi():
                GPIO.setup(self.pin, self.mode)
            self.ready = True


PIN_TABLE = {
    0: Pin(0),
    1: Pin(1),
    2: Pin(2),
    3: Pin(3),
    4: Pin(4),
    5: Pin(5),
    6: Pin(6),
    7: Pin(7),
    8: Pin(8),
    9: Pin(9),
    10: Pin(10),
    11: Pin(11),
    12: Pin(12),
    13: Pin(13),
    14: Pin(14),
    15: Pin(15),
    16: Pin(16),
    17: Pin(17),
    18: Pin(18),
    19: Pin(19),
    20: Pin(20),
    21: Pin(21),
    22: Pin(22),
    23: Pin(23),
    24: Pin(24),
    25: Pin(25),
    26: Pin(26),
    27: Pin(27),
}
