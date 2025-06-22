from data import data
from tool import tool
import asyncio
import sys
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from decimal import Decimal
from modules.User import User
from UI.UI import UI
from time import sleep    

data_local = data()
user = User()
app = QApplication(sys.argv)
UI_local = UI()

class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        
        #Windows
        self.setWindowTitle("Core OS Finace")
        self.setGeometry(*UI_local.getCenter()) # * Desempacota A Tuple
        self.setStyleSheet(UI_local.getStyleCSS())
        
        #Background
        self.setStyleSheet(f"background-color: {UI_local.getColors()["black"]};")

        #Top Bar
        top_bar = QFrame()
        layout_frame = QVBoxLayout(top_bar)

        welcome_title = QLabel(f"Bem Vindo, {user.name}")
        font = welcome_title.font()
        font.setPointSize(UI_local.fontTilteSize)
        welcome_title.setFont(font) 
        layout_frame.addWidget(welcome_title, alignment=Qt.AlignTop | Qt.AlignVCenter)
        
        layout_frame.setSpacing(5)
        
        #Saldo Top_Bar
        saldo_show = QLabel(f"Saldo: {user.getSaldo(data_local)}")
        saldo_font = saldo_show.font()
        saldo_font.setPointSize(UI_local.fontTilteSize - 5)
        saldo_show.setFont(saldo_font)
        layout_frame.addWidget(saldo_show, alignment=Qt.AlignTop | Qt.AlignVCenter)

        layout_frame.addStretch()  # empurra o saldo pro canto direito

        self.setCentralWidget(top_bar)  
        self.show()    
        app.quit()

async def main() -> None:
    if not data_local.Debug: asyncio.create_task(tool.verify_modules())
    asyncio.create_task(tool.add_path_modules(data_local))
    await asyncio.create_task(user.set_values(data_local= data_local))
    return

if __name__ == "__main__":
    asyncio.run(main())
    Main_Window = Main()
    sys.exit(app.exec())