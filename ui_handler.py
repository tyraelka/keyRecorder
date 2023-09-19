from PyQt5 import QtWidgets, QtGui, QtCore
from ui_v2 import Ui_mainWindow

from controller import HandlingController
from listener import HandlingListener
from sleeper import HandlingSleeper
from datetime import datetime

from tkinter import filedialog
import pickle
import os
import time

class MainWindow_controller(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_mainWindow()
        self.ui.setupUi(self)
        self.setup_control()
        self._timeStart = time.time()
        self.inputThread = None
        self.executeThread = None
        self.sleepThread = None
        self.record_file = None
        self.frequency = 1
        self.executeToggle = False
        self.ui.edit_assign.setDateTime(datetime.now())
        self.ui.edit_daily.setDateTime(datetime.now())

    def setup_control(self):
        self.ui.btn_record.clicked.connect(self.toggleRecord)
        self.ui.btn_select_file.clicked.connect(self.get_record_file)
        self.ui.btn_execute.clicked.connect(self.eventExecute)
    
    @property
    def _costTime(self):
        return round(time.time() - self._timeStart, 3)   
    
    def on_mouse_event(self, event: str):
        self._record[self._costTime] = event
        self.ui.text_status.append(str(self._msgIdx) + ". " + event)
        self._msgIdx += 1
    
    def on_keyboard_event(self, event: str):
        self._record[self._costTime] = event
        self.ui.text_status.append(str(self._msgIdx) + ". " + event)
        self._msgIdx += 1
    
    def toggleRecord(self):
        if self.ui.btn_record.text() == "Record":
            self.ui.btn_execute.setDisabled(True)
            self.ui.btn_select_file.setDisabled(True)
            self.ui.text_status.setText("")
            self._msgIdx = 1
            self._record = {}
            self.ui.btn_record.setText("Stop")
            if not self.inputThread:
                self.inputThread = HandlingListener()
                self.inputThread.mouseSignal.connect(self.on_mouse_event)
                self.inputThread.keySignal.connect(self.on_keyboard_event)            
            self.inputThread.start()
        else:
            self.ui.btn_record.setText("Record")
            if self.inputThread:
                self.inputThread.stop()
                self.inputThread = None
            self.dataPretreat()
            self.saveEvent()
            self.ui.btn_execute.setDisabled(False)
            self.ui.btn_select_file.setDisabled(False)
            
    def dataPretreat(self):
        """
        更新原始資料(self._record) 轉換成以時間差為key的字典結構
        
        Args:
            data (dict): 原始資料集
        """
        # Sort data
        # event_record = {key: self._record[key] for key in sorted(self._record)}
        # self._record.popitem() # drop last two
        # self._record.popitem() # drop last one
        
        cost_list = list(self._record.keys()) # 原始資料 key 屬 time.time() 時間序
        wait_list = [round(cost_list[i+1] - cost_list[i], 3) for i in range(len(cost_list) - 1)] # 計算時間差
        wait_list.insert(0, 0) # 維持原陣列長度
        res = {}
        for i, t in enumerate(wait_list):
            key = f"{i}_{t}" # 避免出現相同的時間差導致錯誤
            res[key] = list(self._record.values())[i]
        self._record = res
    
    def saveEvent(self):                       
        # dump to pickle
        if not os.path.exists("./records"): os.mkdir("records")
        nowTime = datetime.now()
        nowTime = nowTime.strftime("%Y-%m-%d %H-%M-%S")
        file_name = nowTime + " record.pkl"
        with open("./records/" + file_name, "wb") as file:
            pickle.dump(self._record, file)
        self.record_file = "./records/" + file_name
        self.ui.label_file_path.setText("file path: " + self.record_file)    
            
    def get_record_file(self):
        prefix = "file path: "
        self.record_file = filedialog.askopenfilename(initialdir="./records", title="Path Records", filetypes=[("pickle", "*.pkl")])
        self.ui.label_file_path.setText(prefix + self.record_file)
    
    def eventExecute(self):
        self.spin_times = self.ui.spin_times.value()
        if not self.executeToggle:
            self.get_frequency()
            self.ui.btn_execute.setText("Stop")
            self.ui.btn_record.setDisabled(True)
            self.ui.btn_select_file.setDisabled(True)
            self.executeToggle = True
            self.stop_signal = False
            if self.frequency == 1:
                self.toggleExecute()
            elif self.frequency == 2:
                if not self.sleepThread:
                    self.sleepThread = HandlingSleeper(self.time_assign.toPyDateTime())
                    self.sleepThread.wakeup_signal.connect(self.on_handler_sleep)
                self.sleepThread.start()
            elif self.frequency == 3:
                if not self.sleepThread:
                    self.sleepThread = HandlingSleeper(self.time_assign.toPyDateTime(), True)
                    self.sleepThread.wakeup_signal.connect(self.on_handler_sleep)
                self.sleepThread.start()
        else:
            self.executeToggle = False
            self.stop_signal = True
            self.on_handler_finished()
            if self.sleepThread:
                self.sleepThread.quit()
                self.sleepThread = None
            if self.executeThread:
                self.executeThread.quit()
                self.executeThread = None
        
    def toggleExecute(self):
        if self.record_file:
            if not self.executeThread:
                self.executeThread = HandlingController(self.record_file, self.spin_times)
                self.executeThread.controller_event.connect(self.on_handler_event)
                self.executeThread.finished_event.connect(self.on_handler_finished)
            self.ui.text_status.setText("")
            self.executeThread.start()
            if self.frequency != 3: self.stop_signal = True

    def on_handler_event(self, event: str):
        self.ui.text_status.append(event)
        
    def on_handler_finished(self):
        if self.executeThread: 
            self.executeThread.wait()
            self.executeThread.quit()
            self.executeThread = None
        if self.stop_signal:
            self.executeToggle = False
            self.ui.btn_record.setDisabled(False)
            self.ui.btn_select_file.setDisabled(False)
            self.ui.btn_execute.setText("Execute")
        
    def on_handler_sleep(self, event: str):
        if event == "Finished":
            if self.sleepThread:
                self.sleepThread.quit()
                self.sleepThread = None
            if self.executeThread:
                self.executeThread.quit()
                self.executeThread = None
            self.toggleExecute()
        elif event == "Daily":
            self.toggleExecute()
        
    def get_frequency(self):
        if self.ui.radio_one.isChecked() == True:
            self.frequency = 1 # one time
        elif self.ui.radio_assign.isChecked() == True:
            self.frequency = 2 # assinged time
            self.time_assign = self.ui.edit_assign.dateTime()
        elif self.ui.radio_daily.isChecked() == True:
            self.frequency = 3 # daily
            self.time_assign = self.ui.edit_daily.dateTime()
        