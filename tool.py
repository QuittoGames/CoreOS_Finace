import os
import platform
from dataclasses import dataclass
import sys
import subprocess
from data import data
from random import randint
from cryptography.fernet import Fernet
import base64

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
    
    def menu(data_local:data,user):
        tool.clear_screen()   
        print("_"*30 + "Core OS Finace" + "_"*30)
        print(f"Ola: {user.name}")
        print(f"Saldo: {tool.hide_money(data_local,user)}")
        print("_"*60)
        print("1. View Extrato")
        print("2. Config")
        print("3. Exit")

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

    def decrypt_value(value_local, fernet: Fernet) -> dict:
        if isinstance(value_local, str):
            try:
                enc_bytes = base64.urlsafe_b64decode(value_local.encode())
                dec = fernet.decrypt(enc_bytes).decode()
                # Tenta converter pra número, se possível
                if dec.isdigit():
                    return int(dec)
                try:
                    return float(dec)
                except:
                    return dec
            except Exception:
                return value_local
        elif isinstance(value_local, list):
            return [tool.decrypt_value(v, fernet) for v in value_local]
        elif isinstance(value_local, dict):
            return {k: tool.decrypt_value(v, fernet) for k, v in value_local.items()}
        return value_local

    def installer(data_local:data) -> bool:
        install_path = os.path.join(os.getenv("APPDATA"), "CoreOS_Finace", "data") # Appdata Local App
        data_json_path = os.path.join(install_path, "data.json")
        key_path = os.path.join(install_path, ".env", "key.key")
        try:
            if not os.path.exists(install_path):
                os.makedirs(install_path, exist_ok=True)
                
                if not os.path.exists(data_json_path) and not os.path.exists(key_path):
                    #New Fernet Key
                    new_fernet_key = Fernet.generate_key().strip().decode()
                    fernet = Fernet(new_fernet_key)
                    
                    with open(key_path, "w") as key:
                        key.write(new_fernet_key.decode())

                    #New Json data File
                    with open(install_path, "w") as file:
                        file.write(data_local.json_formart)
                        data_local.data_json_path = data_json_path
                        tool.encrypt_value(data_local.data_json_path,data_local,fernet)

                    os.makedirs(key_path,os.path.dirname(key_path) ,exist_ok=True)
                    #Camanda de segurança para ter varias keys diferentes
                return True
        except ValueError as E:
            raise ValueError(f"[ERROR] Path Not Fund, Path: {install_path}")
        except PermissionError as E:
            raise PermissionError("[SUDO] Sudo Warn")
        return False
    
    def encrypt_value(value,data_local:data, fernet:Fernet):
        if isinstance(value, (str, int, float)):
            text = str(value)
            enc = fernet.encrypt(text.encode())
            return base64.urlsafe_b64encode(enc).decode()
        elif isinstance(value, list):
            return [tool.encrypt_value(v) for v in value]
        elif isinstance(value, dict):
            return {k: tool.encrypt_value(v) for k, v in value.items()}
        else:
            return value

                