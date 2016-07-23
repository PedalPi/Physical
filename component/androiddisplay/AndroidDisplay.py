from component.display import Display
from component.androiddisplay.DisplayServer import DisplayServer


class AndroidDisplay(Display):
    server = None

    def __init__(self, host, port):
        self.server = DisplayServer()
        self.server.listen(port, host)

    def showEffect(self, effect):
        print(effect)

    def showParam(self, param):
        print(param)
