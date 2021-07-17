# sbVirtualDisplay
A modified version of pyvirtualdisplay for optimized SeleniumBase performance.

## Usage:

```python
from sbvirtualdisplay import Display

display = Display(visible=0, size=(1440, 1880))
display.start()

...

display.stop()
```
