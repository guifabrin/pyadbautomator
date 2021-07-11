import time

from pyadbautomator.main import PyAdbAutomator

if __name__ == '__main__':
    py_adb_automator = PyAdbAutomator('com.android.chrome', 5)
    py_adb_automator.open()
    url_bar = py_adb_automator.first('resource-id', 'com.android.chrome:id/url_bar')
    if url_bar:
        url_bar.text('https://github.com/guifabrin')
    py_adb_automator.enter()
    time.sleep(10)
    py_adb_automator.close()
