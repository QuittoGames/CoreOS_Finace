from data import data
from tool import tool
import asyncio
import sys
from PySide6.QtWidgets import *
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
        self.show()
        sleep(100)        
        app.quit()

async def main() -> None:
    if not data_local.Debug: asyncio.create_task(tool.verify_modules())
    asyncio.create_task(tool.add_path_modules(data_local))
    await asyncio.create_task(user.set_values(data_local= data_local))
    return

if __name__ == "__main__":
    asyncio.run(main())
    Main()