from data import data
from tool import tool
import asyncio
import sys
from PySide6.QtWidgets import QApplication, QWidget, QMainWindow
from decimal import Decimal
from modules.User import User

data_local = data()
user = User()
app = QApplication(sys.argv)

class Main(QMainWindow):
    @staticmethod
    def Start():
        tool.clear_screen()
        print(user.saldo)
        print(user.extrato)
        app.quit()

async def main() -> None:
    asyncio.create_task(tool.verify_modules())
    asyncio.create_task(tool.add_path_modules(data_local))
    await asyncio.create_task(user.set_values(data_local= data_local))
    return

if __name__ == "__main__":
    asyncio.run(main())
    Main.Start()