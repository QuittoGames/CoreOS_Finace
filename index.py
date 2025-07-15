from data import data
from tool import tool
import asyncio
import sys
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from modules.User import User
from UI.UI import UI
from time import sleep    
from UI.Sidebar import SideBar
from UI.MainContent import MainContent
from PySide6.QtGui import QIcon
from cryptography.fernet import Fernet
import os
import qasync

data_local = data()
user = User()
UI_local = UI()

class Main(QMainWindow):
    def __init__(self, UI_local: UI, user: User, data_local: data):
        super().__init__()
        if data_local.Debug:print("[DEBUG] Criando janela Main()")
        
        self.UI_local = UI_local
        self.user = user
        self.data_local = data_local
        self.sidebar_visible = True
        
        self.init_ui()
        
    def init_ui(self):
        self.setWindowTitle("Core OS Finance")
        self.setGeometry(*self.UI_local.getCenter())
        self.setStyleSheet(self.UI_local.getStyleCSS())
        
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        main_layout = QHBoxLayout(central_widget)
        main_layout.setSpacing(0)
        main_layout.setContentsMargins(0, 0, 0, 0)
        
        # Sidebar
        self.sidebar = SideBar(central_widget, self.UI_local)
        main_layout.addWidget(self.sidebar)
        
        # Área do conteúdo principal
        content_area = QFrame()
        content_layout = QVBoxLayout(content_area)
        content_layout.setSpacing(0)
        content_layout.setContentsMargins(0, 0, 0, 0)
        
        # Header com toggle button
        header = self.create_header()
        content_layout.addWidget(header)
        
        # Conteúdo principal — passa UI_local, user e data_local
        self.main_content = MainContent(content_area, self.UI_local,user, self.data_local)
        content_layout.addWidget(self.main_content)
        
        main_layout.addWidget(content_area)
        
        self.show()
    
    def create_header(self):
        header = QFrame()
        header.setFixedHeight(50)
        header.setStyleSheet(f"""
            QFrame {{
                background-color: {self.UI_local.getColors()["black"]};
                border-bottom: 1px solid rgba(255, 255, 255, 0.1);
            }}
        """)
        
        layout = QHBoxLayout(header)
        layout.setContentsMargins(20, 0, 20, 0)
        layout.addStretch()
        
        return header
    
    def toggle_sidebar(self):
        if self.sidebar_visible:
            self.sidebar.hide()
            self.sidebar_visible = False
        self.sidebar.show()
        self.sidebar_visible = True

    def closeEvent(self, event):
        try:
            key = data_local.getFernet()
            key = Fernet(key)
            user.saveUserInJson(data_local)
            print(data_local._json_data)
            tool.save_json(data_local,key)
            if data_local.Debug: 
                print("[DEBUG] save_json executado")
                print(f"[DEBUG] Salvando arquivo em: {data_local.data_json_path}")
                print(f"Name:  {user.name}")
        except Exception as E:
            print(f"[ERROR] Erro al salvar json data, Erro: {E}")
        return super().closeEvent(event)

async def main() -> None:
    try:
        if not data_local.Debug:
            asyncio.create_task(tool.verify_modules())
        asyncio.create_task(tool.add_path_modules(data_local))
        await asyncio.create_task(user.set_values(data_local=data_local))
        # tool.exit_signal(loop , data_local) #CLI Exit control
    except PermissionError as E:
        print(E) # The raise return str
        sleep(5)
        tool.rebootApp()
        
if __name__ == "__main__":
    app = QApplication(sys.argv)    
    app.setWindowIcon(QIcon(r"icons\CoreOSFinace_icon.png"))
    asyncio.run(main())   
    user.setNameGUI(data_local) # Verfica via func direta (funçao que exec açao de modo imperativo) o name e pede para setalo
    window = Main(UI_local=UI_local,user=user,data_local=data_local)
    loop = qasync.QEventLoop(app)
    asyncio.set_event_loop(loop)
    window.show()
    
    with loop: #Mantem emquanto loop roda
        sys.exit(loop.run_forever())
