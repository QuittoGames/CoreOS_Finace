from data import data
from tool import tool
import asyncio
import sys
from PySide6.QtWidgets import QApplication, QWidget, QMainWindow

data_local = data()
app = QApplication(sys.argv)

class Main(QMainWindow):
    @staticmethod
    def Start():
        tool.clear_screen()
        print("oi")
        app.quit()

async def main() -> None:
    asyncio.create_task(tool.verify_modules())
    asyncio.create_task(tool.add_path_modules(data_local))
    return


if __name__ == "__main__":
    asyncio.run(main())
    Main.Start()