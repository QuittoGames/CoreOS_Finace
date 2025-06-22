from dataclasses import dataclass
from PySide6.QtCore import * 
from PySide6.QtWidgets import * 
from PySide6.QtGui import * 

@dataclass
class UI:
    window_width: int = 800
    window_height: int = 600

    def getCenter(self):
        screen = QGuiApplication.primaryScreen().availableGeometry()
        screen_width = screen.width()
        screen_height = screen.height()
        x = (screen_width - self.window_width) // 2
        y = (screen_height - self.window_height) // 2
        return x, y, self.window_width, self.window_height