from .rpi_commons import check_rpi, GPIO

# Pin
OUT = None
IN = None
LOW = None
HIGH = None


def __load_mock_definition():
    # pin
    global OUT
    global IN
    global LOW
    global HIGH
    OUT = 0x01
    IN = 0x02
    HIGH = 0x01
    LOW = 0x00


def __load_gpio_definition():
    # pin
    global OUT
    global IN
    global LOW
    global HIGH
    OUT = GPIO.OUT
    IN = GPIO.IN
    HIGH = GPIO.HIGH
    LOW = GPIO.LOW


if check_rpi():
    __load_gpio_definition()
else:
    __load_mock_definition()
