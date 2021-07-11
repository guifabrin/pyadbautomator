import subprocess
import time
import xml.etree.ElementTree as ET
import xml.dom.minidom


def __find_between(s, first, last):
    try:
        start = s.index(first) + len(first)
        end = s.index(last, start)
        return first + s[start:end] + last
    except ValueError:
        return ""


def get_root(seconds_delay=0) -> object:
    time.sleep(seconds_delay)
    xml_result = subprocess.check_output("adb exec-out uiautomator dump /dev/tty").decode("utf-8")
    xml_string = __find_between(xml_result, "<hierarchy", "</hierarchy>")
    dom = xml.dom.minidom.parseString(xml_string)
    pretty_xml_as_string = dom.toprettyxml()
    print(pretty_xml_as_string)
    return ET.fromstring(xml_string)


class PyAdbNode:
    element = NotImplementedError
    automator = NotImplementedError

    def __init__(self, element, automator):
        self.element = element
        self.automator = automator

    def click(self):
        init, end = self.element.attrib['bounds'].split('][')
        bound_a, bound_b = init.replace('[', '').split(',')
        bound_c, bound_d = end.replace(']', '').split(',')
        bound_x = (int(bound_a) + int(bound_c)) / 2
        bound_y = (int(bound_b) + int(bound_d)) / 2
        subprocess.call("adb shell input tap " + str(bound_x) + " " + str(bound_y), shell=True)
        self.automator.update()

    def text(self, string):
        self.click()
        subprocess.call("adb shell input text \"" + string + "\"", shell=True)
        self.automator.update()

    def get_attr(self, attrib):
        return self.element.attrib[attrib]


class PyAdbAutomator:
    package = NotImplementedError
    seconds_delay = NotImplementedError
    _root = NotImplementedError

    def __init__(self, package, seconds_delay=0):
        self.package = package
        self.seconds_delay = seconds_delay

    def open(self):
        subprocess.call("adb shell monkey -p " + self.package + " -c android.intent.category.LAUNCHER 1", shell=True)
        self.update()

    def close(self):
        subprocess.call("adb shell am force-stop " + self.package, shell=True)
        self.update()

    def enter(self):
        subprocess.call("adb shell input keyevent 66", shell=True)

    def update(self):
        self._root = get_root(self.seconds_delay)

    def select(self, attrib, value, root=None) -> list:
        if root is None:
            root = self._root
        filtered = filter(lambda node: node.attrib[attrib] == value, root.findall('.//*'))
        mapped = map(lambda node: PyAdbNode(node, self), filtered)
        return list(mapped)

    def first(self, attrib, value, root=None):
        nodes = self.select(attrib, value, root)
        if len(nodes) > 0:
            return nodes[0]
