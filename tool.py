import os
import platform
from dataclasses import dataclass
import sys
import subprocess
from data import data
from random import randint

@dataclass
class tool:
    def clear_screen():
        if platform.system() == "Windows":
            os.system('cls')
        else:
            os.system('clear')

    async def verify_modules():
        try:
            # #Uso Do modules por txt
            req_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "requirements", "requirements.txt"))
            subprocess.run([sys.executable, "-m", "pip", "install", "-r", req_path], check=True)
        except Exception as E:
            print(f"Erro Na Verificaçao De Modulos, Erro: {E}")
            return
        
    async def add_path_modules(data_local:data):
        if data.modules_local == None:return
        try:
            for i in data.modules_local:
                sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), i)))
                if data_local.Debug:print(f"Module_local: {i}")
            return
        except Exception as E:
            print(f"Erro Al Adicionar Os Caminhos Brutos, Erro: {E}")
            return
    
    # In Dev
    def create_json(path:str) -> None:
        try:
            os.makedirs("data",exist_ok=True)
            data_json = os.path.join("data")
            with open(data_json , "w") as file:
                file.write(data.json_formart)
        except PermissionError:
            print("Erro: Sem permissão para criar arquivo ou pasta.")
        except FileNotFoundError:
            print("Erro: Pasta não encontrada.")
        except OSError as e:
            print(f"Erro do sistema: {e}")
        return
    
    def binary_search(array: list, target: int) -> int:
        low = 0
        high = len(array) - 1

        while low <= high:
            mid = (low + high) // 2
            guess = array[mid]

            if guess == target:
                return mid 
            elif guess < target:
                low = mid + 1 
            else:
                high = mid - 1 

        return None
