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
if inspect.isclass(obj):
self.scheduleTypesCombo.addItem(name)
self.schedule_types[name] = obj
 # populate schedule types
        self.schedule_types = dict()
        for name, obj in inspect.getmembers(ScheduleWidgets):
            if inspect.isclass(obj):
                self.scheduleTypesCombo.addItem(name)
                self.schedule_types[name] = obj

        # initialise schedule model
        self.scheduleView.setModel(ScheduleView.ScheduleModel([], [[]]))

        # add function bindings
        self.actionSave.triggered.connect(self.save_schedule)

        self.generateScheduleButton.clicked.connect(self.generate)

        self.scheduleTypesCombo.activated.connect(self.select_schedule_type)

        self.scheduleView.selectionModel().selectionChanged.connect(self.draw_pulse)

    def generate(self):
        # get the schedule data and headers
        self.schedule, self.schedule_headers = self.current_schedule_type.generate_schedule(self.valence_map.get_valence_map())

        # post to the schedule view
        self.schedule_model = ScheduleView.ScheduleModel(self.schedule_headers, self.schedule, parent=self)
        self.scheduleView.setModel(self.schedule_model)
        self.scheduleView.selectionModel().selectionChanged.connect(self.draw_pulse)

    def select_schedule_type(self):
        schedule_name = self.scheduleTypesCombo.currentText()

        if self.current_schedule_type is not None:
            self.scheduleParamsContents.layout().removeWidget(self.current_schedule_type)
            self.current_schedule_type.deleteLater()
