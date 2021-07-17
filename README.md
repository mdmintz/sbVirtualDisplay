# sbVirtualDisplay
A modified version of [pyvirtualdisplay](https://github.com/ponty/PyVirtualDisplay) for optimized [SeleniumBase](https://github.com/seleniumbase/SeleniumBase) performance.

## Usage:

```python
from sbvirtualdisplay import Display

display = Display(visible=0, size=(1440, 1880))
display.start()

...

display.stop()
```
