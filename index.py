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

UI_local = UI()

class Main(QMainWindow):
    def __init__(self):
        super().__init__()

        #Layout Base
        main_layout = QVBoxLayout()
        main_layout.setSpacing(20)
        main_layout.setContentsMargins(30, 30, 30, 30)
    
        #Windows
        self.setWindowTitle("Core OS Finace")
        self.setGeometry(*UI_local.getCenter()) # * Desempacota A Tuple
        self.setStyleSheet(UI_local.getStyleCSS())
        
        #Background
        self.setStyleSheet(f"background-color: {UI_local.getColors()["black"]};")

        #Top Bar
        top_bar = QFrame()
        layout_top = QVBoxLayout(top_bar)

        welcome_title = QLabel(f"Bem Vindo, {user.name}")
        font = welcome_title.font()
        font.setPointSize(UI_local.fontTilteSize)
        welcome_title.setFont(font) 
        layout_top.addWidget(welcome_title, alignment=Qt.AlignTop | Qt.AlignVCenter)
        
        layout_top.setSpacing(5)
        
        #Saldo Top_Bar
        saldo_show = QLabel(f"Saldo: {user.getSaldo(data_local)}")
        saldo_font = saldo_show.font()
        saldo_font.setPointSize(UI_local.fontTilteSize - 5)
        saldo_show.setFont(saldo_font)
        layout_top.addWidget(saldo_show, alignment=Qt.AlignTop | Qt.AlignVCenter)

        layout_top.addStretch()  # empurra o saldo pro canto direito

        # Wingets 
        upper_money = QFrame()
        upper_money.setStyleSheet("""background: qlineargradient(
                x1: 0, y1: 0,
                x2: 1, y2: 0,
                stop: 0 #0655FF,
                stop: 1 #1438E9
            );
            border-radius: 5px;
        """)
        upper_money.setFixedSize(250, 50)

        # Criar layout dentro do upper_money
        layout_frame_content = QVBoxLayout(upper_money)
        layout_frame_content.setContentsMargins(5, 10, 0, 0)  # margens internas do frame
        layout_frame_content.setAlignment(Qt.AlignTop | Qt.AlignLeft)  # alinhamento

        lucro_label = QLabel(f"Lucro: {user.lucro}")
        lucro_font = lucro_label.font()
        lucro_font.setPointSize(UI_local.fontTilteSize - 4)
        lucro_label.setFont(lucro_font)

        # Adiciona o label no layout do upper_money
        layout_frame_content.addWidget(lucro_label)

        #Add Wingets In Layout
        main_layout.addWidget(top_bar)
        main_layout.addWidget(upper_money, alignment=Qt.AlignCenter)
        
        # Windows Class
        container = QWidget()
        container.setLayout(main_layout)
        self.setCentralWidget(container)
        self.show()    
        # app.quit()

async def main() -> None:
    if not data_local.Debug: asyncio.create_task(tool.verify_modules())
    asyncio.create_task(tool.add_path_modules(data_local))
    await asyncio.create_task(user.set_values(data_local= data_local))
    return

if __name__ == "__main__":
    app = QApplication(sys.argv)
    asyncio.run(main())
    Main_Window = Main()
    sys.exit(app.exec())