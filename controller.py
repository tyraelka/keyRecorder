from pynput.mouse import Button
from pynput.mouse import Controller as mouseController

from pynput.keyboard import Key
from pynput.keyboard import Controller as keyController

from PyQt5.QtCore import QThread, pyqtSignal
import pickle
import time
import re

class HandlingController(QThread):
    controller_event = pyqtSignal(str)
    finished_event = pyqtSignal()
    def __init__(self, record_file, cycle_times) -> None:
        super().__init__()
        self._mouse = mouseController()
        self._key = keyController()
        self.record_file = record_file
        self.cycle_times = cycle_times
        self._btnMask = {
            "Button.left": Button.left,
            "Button.middle": Button.middle,
            "Button.right": Button.right
        }
        self._specialKeys = [
            "Key.cmd", "Key.ctrl", "Key.alt"
        ]
            
    @staticmethod
    def action_convert_to_dict(actionList: str):
        data_list = actionList.split("\n")
        res = {}
        for data in data_list:
            t, action = data.split(" ")
            res[t] = action
        return res
    
    def action_converter(self, actionPath: str):
        action, path = actionPath.split(":")
        # mouse
        if "/" in path: 
            path = path.split("/")
            path_x, path_y = int(path[0]), int(path[1])
            if action == "position":
                return (action, path_x, path_y)
            elif action == "scrolled":
                path_dx, path_dy = int(path[2]), int(path[3])
                return (action, path_dx, path_dy)
            elif action == "pressed":
                btn = path[2]
                return (action, btn)
            elif action == "released":
                btn = path[2]
                return (action, btn)
        # keyboard
        else:
            if action == "key_pressed" or action == "key_released":
                btn = path
                if "Key" in btn: # Special Keys
                    keyName = btn.strip("<>").split(":")[0].replace("Key.", "")
                    return (action, Key[keyName])
                else:
                    if btn != "'": btn = btn.strip("''")
                    return (action, btn)
        
    def action_execute(self, waiting_time, action_data, action_data2=None, tab_times=0):
        data = self.action_converter(action_data) # 轉換輸入資料格式
        waiting_time = float(waiting_time.split("_")[-1]) # 剔除Index取出時間(float)
        time.sleep(waiting_time)
        if not action_data2:
            action = data[0]
            if action == "position":
                self._mouse.position = (data[1], data[2])
            elif action == "scrolled":
                self._mouse.scroll(data[1], data[2])
            elif action == "pressed":
                self._mouse.press(self._btnMask[data[1]])
            elif action == "released":
                self._mouse.release(self._btnMask[data[1]])
            elif action == "key_pressed":
                self._key.press(data[1])
                # if data[1] != Key.shift:
                #     self._key.press(data[1])
                #     self._key.release(data[1])
            elif action == "key_released":
                self._key.release(data[1])
        else:
            data2 = self.action_converter(action_data2)
            if tab_times == 0:
                self._key.press(data[1])
                self._key.press(data2[1])
                self._key.release(data2[1])
                self._key.release(data[1])
            else:
                self._key.press(data[1]) # alt
                for _ in range(tab_times):
                    self._key.press(data2[1]) # tab
                    self._key.release(data2[1])
                self._key.release(data[1])
                      
    def getRecord(self):
        if self.record_file:
            with open(self.record_file, "rb") as file:
                self.event_record = pickle.load(file)
        else:
            self.event_record = None
    
    def run(self):
        # Get Data
        self.getRecord()
        if self.event_record:
            pattern = r"Key.[A-Za-z]+"
            for _ in range(self.cycle_times):
                record_iter = iter(self.event_record.items())
                for waiting_time, data in record_iter:
                    key_name = re.findall(pattern, data)
                    key_name = key_name[0] if len(key_name) > 0 else None
                    if self.isInterruptionRequested(): break
                    if key_name and key_name in self._specialKeys:
                        next_time, next_data = next(record_iter)
                        self.action_execute(waiting_time, data, next_data)
                        self.controller_event.emit(waiting_time + ": " + data)
                        self.controller_event.emit(waiting_time + ": " + next_data)
                    else:
                        self.action_execute(waiting_time, data)
                        self.controller_event.emit(waiting_time + ": " + data)
            self.finished_event.emit()
    
    def stop(self):
        self.finished_event.emit()
    
    def quit(self) -> None:
        return super().quit()