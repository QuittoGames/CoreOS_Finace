from dataclasses import dataclass, field
from decimal import Decimal
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from data import data
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from tool import tool
from time import sleep
from modules.Aplicao import Aplicao
from modules.Item import Item
import json

@dataclass
class User:
    saldo:Decimal = (0.0)
    name:str = ""
    aplicaçoes: list = field(default_factory=list)
    receita: list = field(default_factory=list)
    gastos: list = field(default_factory=list)
    extrato: list = field(default_factory=list)
    lucro: Decimal = (0.0)
    
    async def set_values(self,data_local: data):
        path = os.path.join(data.data_json_path)
        if not os.path.exists(path=path):tool.create_json(path)
        key = data_local.getKey()

        with open(data.data_json_path, "r+") as file:
            data.json_data = file.read()
            raw_dict = json.loads(data.json_data)
            if data_local.Debug: print("DEBUG saldo:", type(data.json_data.get("saldo")))
            data.json_data = tool.decrypt_value(value_local=raw_dict,fernet=key)     # ← CONVERTE de string JSON para dict

        self.saldo = Decimal(str(data.json_data["saldo"]))
        self.name = str(data.json_data["name"])
        #For in Json
        self.aplicaçoes = [Aplicao(
            _name=ap["name"],
            _taxa_juros=ap["taxa_juros"],
            _type=ap["type"],
            _moeda=ap["moeda"],
            _min_aporte=Decimal(str(ap["min_aporte"])),
            _prazo_meses=ap["prazo_meses"],
            _liquidez=ap["liquidez"],
        )for ap in data.json_data["aplicacoes"]]

        self.gastos = [Item(
            _ID = Item.generete_nunber(),
            _name = ap["name"],
            _descr = ap["descr"],
            _type = ap["type"],
            _coin = ap["coin"],
            _value = ap["value"],
        ) for ap in data.json_data["gastos"]]

        self.receita = [Item(
            _ID = Item.generete_nunber(),
            _name = ap["name"],
            _descr = ap["descr"],
            _type = ap["type"],
            _coin = ap["coin"],
            _value = ap["value"],
        ) for ap in data.json_data["receita"]]

        self.extrato = self.receita + self.gastos
    
        self.lucro = sum(Decimal(str(i._value)) for i in self.receita) - sum(Decimal(str(i._value)) for i in self.gastos)
        return
    
    def getSaldo(self,data_local:data) -> str:
        if data_local.show_saldo:
            return str(self.saldo)
        return "".join(["*" for i in range(len(str(self.saldo)))])
