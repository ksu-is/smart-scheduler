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
