from data import data
from tool import tool
import asyncio
import sys
from PySide6.QtWidgets import QApplication, QWidget

data_local = data()
app = QApplication(sys.argv)

class Main(app):
    @staticmethod
    def Start():
        pass

def main():
    pass


if __name__ == "__main__":
    main()
    asyncio.run(Main.Start())