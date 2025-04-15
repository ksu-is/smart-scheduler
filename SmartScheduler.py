import sys
import inspect
import numpy as np
import pickle
from PyQt5 import QtWidgets
from Designs import mainDesign
from Models import Widgets
from Models import ScheduleWidgets, ScheduleView
from UI import ColorMap
from PyPulse import PulseInterface
class MainApp(QtWidgets.QMainWindow, mainDesign.Ui_MainWindow):
    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self)
 self.current_schedule_type = None
        self.schedule = dict()
        self.schedule_headers = []
# add the reward map
        self.valence_map = Widgets.ValveMapWidget(self.valveMapContents)
        self.valveMapContents.layout().addWidget(self.valence_map)
# populate schedule types
        self.schedule_types = dict()
 for name, obj in inspect.getmembers(ScheduleWidgets):
