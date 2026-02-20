import os

BASE_PATH = os.path.dirname(__file__)

APP_START_PATH = os.getcwd()

class Route():
    def __init__(self, route, view):
        self.route = route
        self.view = view



