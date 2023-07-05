

class Emulator:
    def __init__(self, port, host="localhost", name=None):
        self.host = host
        self.port = port
        self.name = name
        self.adb_name = f"{host}:{port}"