
# PyAdbAutomator

PyAdbAutomator is a Python library for automating some android tasks using ADB interface

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install foobar.

```bash
pip install pyadbautomator
```

## Usage

```python
    py_adb_automator = PyAdbAutomator('com.android.chrome', 5)
    py_adb_automator.open()
    url_bar = py_adb_automator.first('resource-id', 'com.android.chrome:id/url_bar')
    if url_bar:
        url_bar.text('https://github.com/guifabrin')
    py_adb_automator.enter()
    time.sleep(10)
    py_adb_automator.close()
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)
