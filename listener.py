from PyQt5.QtCore import QThread, pyqtSignal

from pynput.mouse import Listener as mListener
from pynput.mouse import Controller as mCtrl
from pynput.keyboard import Listener as kListener

class HandlingListener(QThread):
    mouseSignal = pyqtSignal(str)
    keySignal = pyqtSignal(str)
    
    def __init__(self):
        super().__init__()
        self.stop_requested = False
        self._mouse = mCtrl()
        self._record = {}
        self._msg = ""
        self._vkList = list(range(96, 106))
              
    def run(self):
        def on_move(x, y):
            x, y = self._mouse.position
            self._msg = f"position:{x}/{y}"
            self.mouseSignal.emit(self._msg)
            # self._record[self._costTime] = self._msg
                
        def on_click(x, y, button, pressed):
            x, y = self._mouse.position
            if pressed:
                self._msg = f"pressed:{x}/{y}/{button}"
                self.mouseSignal.emit(self._msg)
                # self._record[self._costTime] = self._msg
            else:
                self._msg = f"released:{x}/{y}/{button}"
                self.mouseSignal.emit(self._msg)
                # self._record[self._costTime] = self._msg
                    
        def on_scroll(x, y, dx, dy):
            x, y = self._mouse.position
            self._msg = f"scrolled:{x}/{y}/{dx}/{dy}"
            self.mouseSignal.emit(self._msg)
            # self._record[self._costTime] = self._msg
        
        def on_press(key):
            try:
                if key.vk in self._vkList: key.char = key.vk - 96 
                
                # self._record[self._costTime] = f"key_pressed:{key.char}"
                self._msg = f"key_pressed:{key.char}"
                self.keySignal.emit(self._msg)
            except:
                # self._record[self._costTime] = f"key_pressed:{key}"
                self._msg = f"key_pressed:{key}"
                self.keySignal.emit(self._msg)
            
        def on_release(key):
            try:
                if key.vk in self._vkList: key.char = key.vk - 96 
                
                # self._record[self._costTime] = f"key_pressed:{key.char}"
                self._msg = f"key_released:{key.char}"
                self.keySignal.emit(self._msg)
            except:
                # self._record[self._costTime] = f"key_pressed:{key}"
                self._msg = f"key_released:{key}"
                self.keySignal.emit(self._msg)
        
        self.mouse_listener = mListener(on_click=on_click, on_move=on_move, on_scroll=on_scroll)
        self.keyboard_listener = kListener(on_press=on_press, on_release=on_release)
        
        with self.mouse_listener, self.keyboard_listener:
            self.exec_()
        
    def stop(self):
        # self.stopped = True
        if hasattr(self, 'mouse_listener'):
            self.mouse_listener.stop()
        if hasattr(self, 'keyboard_listener'):
            self.keyboard_listener.stop()