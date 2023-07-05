
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

    def __init__(self, port: str, host: str = "localhost", name: str = None):
        self.host = host
        self.port = port
        self.name = name
        self.adb_name = f"{host}:{port}"
