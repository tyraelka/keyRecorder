from PyQt5.QtCore import QThread, pyqtSignal

from datetime import datetime
import time

class HandlingSleeper(QThread):
    wakeup_signal = pyqtSignal(str)
    def __init__(self, target_time: datetime, daily=False):
        super().__init__()
        self.target_time = target_time
        self.daily = daily
        self.executable = True
        
    def run(self):
        while True:
            if self.isInterruptionRequested(): break
            if not self.daily:
                if datetime.now() < self.target_time:
                    time.sleep(60)
                else:
                    self.wakeup_signal.emit("Finished")
                    break
            else:
                now = datetime.now()
                if (now.hour == self.target_time.hour) and \
                    (now.minute == self.target_time.minute):
                    self.wakeup_signal.emit("Daily")
                    time.sleep(60)
                else:
                    time.sleep(60)

        