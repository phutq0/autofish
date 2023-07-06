import cv2
from core import command
import re
import time


class Button:
    def __init__(self, name: str = None, x: int = -1, y: int = -1, adb_name: str = None, debug=False):
        if name is not None:
            if not isinstance(name, str):
                raise ValueError("[ERROR]: Name must be string")
        if not isinstance(x, int):
            raise ValueError("[ERROR]: X coordinate must be integer")
        if not isinstance(y, int):
            raise ValueError("[ERROR]: Y coordinate must be integer")
        if adb_name is not None:
            if not isinstance(adb_name, str):
                raise ValueError("[ERROR]: Adb name must be string")
        self.name = name
        self.x = x
        self.y = y
        self.adb_name = adb_name
        self.debug = debug

    def press(self):
        if self.x == -1 or self.y == -1:
            raise ValueError("[ERROR] Can not find button's position")
        if self.debug:
            if not self.adb_name:
                raise ValueError("[ERROR] Can not find emulator")
            result = command("adb devices")
            if not self.adb_name in result:
                raise ValueError("[ERROR] Can not find emulator")
        command(f"adb -s {self.adb_name} shell input tap {self.x} {self.y}")

    def long_press(self, duration: int):
        if not isinstance(duration, int):
            raise ValueError("[ERROR]: Duration must be integer")
        if self.x == -1 or self.y == -1:
            raise ValueError("[ERROR] Can not find button's position")
        if self.debug:
            if not self.adb_name:
                raise ValueError("[ERROR] Can not find emulator")
            result = command("adb devices")
            if not self.adb_name in result:
                raise ValueError("[ERROR] Can not find emulator")
        command(
            f"adb -s {self.adb_name} shell input touchscreen swipe {self.x} {self.y} {self.x} {self.y} {duration}"
        )

    def get_position_on_screen(self):
        return self.x, self.y


class Input:
    def __init__(self, name: str = None, x: int = -1, y: int = -1):

        self.name = name
        self.x = x
        self.y = y

    def clear():
        pass

    def type(s: str):
        pass


class Emulator:
    """
        Emulator Instance
    """

    def __init__(self, port, host: str = "localhost", name: str = None):
        if not isinstance(port, (str, int)):
            raise ValueError("[ERROR]: Port must be string or integer")
        if name is not None:
            if not isinstance(name, str):
                raise ValueError("[ERROR]: Name must be string")

        self.host = host
        self.port: str = str(port)
        self.name = name
        self.adb_name = f"{host}:{port}"
        self.button: dict[str, Button] = {}

    def connect(self):
        result = command(f"adb connect {self.adb_name}")
        ok1 = f"connect to {self.adb_name}"
        ok2 = f"connected to {self.adb_name}"
        if ok1 in result or ok2 in result:
            return True
        else:
            raise ValueError("[ERROR]: Can not connect to emulator")

    def disconnect(self):
        try:
            result = command(f"adb disconnect {self.adb_name}")
            ok = f"disconnected {self.adb_name}"
            if ok in result:
                return True
            else:
                raise ValueError("[ERROR]: No such emulator")
        except:
            raise ValueError("[ERROR]: No such emulator")

    def is_connected(self):
        result = command("adb devices")
        return self.adb_name in result

    def get_screen_dimension(self) -> tuple[int, int]:
        connected = self.check_is_connected()
        if not connected:
            raise ValueError("[ERROR]: No such emulator")
        result = command(f"adb -s {self.adb_name} shell wm size")
        result = re.findall(r'\d+x\d+', result)
        if result:
            x, y = result[0].split("x")
            return int(x), int(y)
        else:
            raise ValueError("[ERROR]: No such emulator")

    def get_screen_width(self) -> int:
        x, _ = self.get_screen_dimension()
        return x

    def get_screen_height(self) -> int:
        _, y = self.get_screen_dimension()
        return y

    def add_button(self, name: str, button: Button) -> None:
        if not isinstance(name, str):
            raise ValueError("[ERROR]: Button name must be string")
        if not isinstance(button, Button):
            raise ValueError("[ERROR]: Button must be Button")
        if not name:
            raise ValueError("[ERROR]: Invalid button name")
        if name in self.button:
            raise ValueError("[ERROR]: Button name had been existed")
        button.adb_name = self.adb_name
        self.button[name] = button
