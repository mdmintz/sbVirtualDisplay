import time
from sbvirtualdisplay import Display


def test_unit():
    display = Display(visible=0, size=(1440, 1880))
    display.start()
    time.sleep(2)
    display.stop()
