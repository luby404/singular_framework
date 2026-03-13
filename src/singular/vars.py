import os

STYLE = dict()
APP_START_PATH = os.getcwd()
BASE_PATH = os.path.dirname(__file__)



class Route():
    def __init__(self, route, view):
        self.route = route
        self.view = view



