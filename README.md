# sbVirtualDisplay (💻) [![](https://img.shields.io/pypi/v/sbvirtualdisplay.svg)](https://pypi.python.org/pypi/sbvirtualdisplay)

A customized [pyvirtualdisplay](https://github.com/ponty/PyVirtualDisplay) for use with [SeleniumBase](https://github.com/seleniumbase/SeleniumBase) automation.

## Usage example:

```python
from sbvirtualdisplay import Display

display = Display(visible=0, size=(1440, 1880))
display.start()

# Run browser tests in a headless environment

display.stop()
```

### Or as a context manager:

```python
with Display(visible=0, size=(1440, 1880)):
    # Run browser tests in a headless environment
    ...
```

## When to use:

If you need to run browser tests on a headless machine (such as a Linux backend), and you can't use a browser's headless mode (such as Chrome's headless mode), then this may help. For example, Chrome does not allow extensions in headless mode, so if you need to run automated tests on a headless Linux machine and you need to use Chrome extensions, then this will let you run those tests using a virtual display.


## More info:

* [Xvfb](https://en.wikipedia.org/wiki/Xvfb) is required for this to work.
