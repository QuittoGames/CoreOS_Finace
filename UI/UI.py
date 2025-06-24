from dataclasses import dataclass,field
from PySide6.QtCore import * 
from PySide6.QtWidgets import * 
from PySide6.QtGui import * 

@dataclass
class UI:
    window_width: int = 800
    window_height: int = 600

    fontTilteSize:int = 17

    colors:dict = field(default_factory=lambda: {
        "black":"#202121",
        "black_second":"#333333",
        "black_third":"#333333",
        "blue":"#1438E9",
        "blue_second":"#0655FF",
        "green": "#1F8A70",           # verde principal forte e elegante
        "green_second": "#1AE421",    # verde secundário mais vibrante
        "white":"#ECECEE",
    })

    def getCenter(self):
        screen = QGuiApplication.primaryScreen().availableGeometry()
        screen_width = screen.width()
        screen_height = screen.height()
        x = (screen_width - self.window_width) // 2
        y = (screen_height - self.window_height) // 2
        return x, y, self.window_width, self.window_height
    

    def getColors(self) -> dict:
        return self.colors
    
    
    def getStyleCSS(self) -> str:
        return """
        /* Estilo global para toda a aplicação/janela */
        :root {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            font-size: 14px;
            color: #ECECEE;           /* cor do texto */
            background-color: {#202121;} /* cor de fundo */
        }

        /* Para o widget principal (QWidget) */
        QWidget {
            background-color: #202121;
            color: #ECECEE;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            font-size: 14px;
        }
    """
