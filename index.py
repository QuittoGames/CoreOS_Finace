from data import data
from tool import tool
import asyncio
import sys
from PySide6.QtWidgets import QApplication, QWidget, QMainWindow
from decimal import Decimal
from modules.User import User
from time import sleep    

data_local = data()
user = User()
app = QApplication(sys.argv)

class Main(QMainWindow):
    @staticmethod
    def Start():
        tool.clear_screen()
        tool.menu(data_local,user)
        try:
            c = input("Digite Sua Opiçao: ").strip().lower()
            if c == "1":
                tool.clear_screen()
                user.getExtrato()
                s = input("Presione Qualquer Tecla Para sair: ")
                Main.Start()
                return
            else:
                Main.Start()
                return
        except Exception as E:
            print(f"Erro no input, Erro: {E}")
            Main.Start()
            return
        app.quit()

async def main() -> None:
    asyncio.create_task(tool.verify_modules())
    asyncio.create_task(tool.add_path_modules(data_local))
    await asyncio.create_task(user.set_values(data_local= data_local))
    return

if __name__ == "__main__":
    asyncio.run(main())
    Main.Start()