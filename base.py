import cv2
from core import command


class Button:
    def __init__(self, name: str = None, x=0, y=0):
        self.name = name
        self.x = x
        self.y = y

    def press():
        pass


class Input:
    def __init__(self, name: str = None, x=0, y=0):
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
            raise ValueError("[ERROR]: $port must be string or integer")
        if name is not None:
            if not isinstance(name, str):
                raise ValueError("[ERROR]: $name must be string")

        self.host = host
        self.port: str = str(port)
        self.name = name
        self.adb_name = f"{host}:{port}"

    def connect(self):
        result = command(f"adb connect {self.adb_name}")
        ok1 = f"connect to {self.adb_name}"
        ok2 = f"connected to {self.adb_name}"
        if ok1 in result or ok2 in result:
            self.is_connected = True
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
                raise ValueError("[ERROR]: No such device")
        except:
            raise ValueError("[ERROR]: No such device")

    def check_is_connected(self):
        result = command("adb devices")
        return self.adb_name in result
