from unittest import TestCase
from sbvirtualdisplay import Display


class Tests(TestCase):
    def test_unit(self):
        display = Display(visible=0, size=(1440, 1880))
        output = display.start()
        print(output)
        self.assertEqual(output.size[0], 1440)
        self.assertEqual(output.size[1], 1880)
        self.assertEqual(output.cmd[0], "Xvfb")
        display.stop()
