from dataclasses import dataclass, field
from decimal import Decimal
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from data import data
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from tool import tool
from time import sleep
import json

@dataclass
class User:
    saldo:Decimal = (0.0)
    aplicaçoes: list = field(default_factory=list)
    receita: list = field(default_factory=list)
    gastos: list = field(default_factory=list)
    extrato: list = field(default_factory=list)
    
    async def set_values(self,data_local: data):
        path = os.path.join(data.data_json_path)
        if not os.path.exists(path=path):tool.create_json()

        with open(data.data_json_path, "r+") as file:
            data.json_data = file.read()
            data.json_data = json.loads(data.json_data)  # ← CONVERTE de string JSON para dict

        self.saldo = Decimal(str(data.json_data["saldo"]))
        return
        
        