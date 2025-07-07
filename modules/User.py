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
from cryptography.fernet import Fernet
from modules.Item import Item   
from UI.Setname import NameDialog
from PySide6.QtWidgets import QDialog
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
        try:
            if tool.installer(data_local):
                print("[WARN] Instalaço Completa")
        except PermissionError as E:
            print(E)

        local_path = data_local.setEnvPath() #Adiciona o valor do path local
        data_local.data_json_path = os.path.join(local_path,"data.json")
        
        key = data_local.getKey() 
        if isinstance(key, str):key = key.encode() 
        fernet = Fernet(key=key)

        with open(data_local.data_json_path, "rb") as file:
            data_local.json_data = json.loads(file.read())
            # if data_local.Debug: print("DEBUG saldo:", data_local.json_data.get("saldo"),type(data.json_data.get("saldo")))
            data_local.json_data = tool.decrypt_value(value_local=data_local.json_data, fernet=fernet)     # ← CONVERTE de string JSON para dict

        self.saldo = Decimal(str(data_local.json_data["saldo"]))
        self.name = str(data_local.json_data["name"])
        #For in Json
        self.aplicaçoes = [Aplicao(
            _name=ap["name"],
            _taxa_juros=ap["taxa_juros"],
            _type=ap["type"],
            _moeda=ap["moeda"],
            _min_aporte=Decimal(str(ap["min_aporte"])),
            _prazo_meses=ap["prazo_meses"],
            _liquidez=ap["liquidez"],
        )for ap in data_local.json_data["aplicacoes"]]

        self.gastos = [Item(
            _ID = Item.generete_nunber(data_local=data_local),
            _name = ap["name"],
            _descr = ap["descr"],
            _type = ap["type"],
            _coin = ap["coin"],
            _value = ap["value"],
        ) for ap in data_local.json_data["gastos"]]

        self.receita = [Item(
            _ID = Item.generete_nunber(data_local=data_local),
            _name = ap["name"],
            _descr = ap["descr"],
            _type = ap["type"],
            _coin = ap["coin"],
            _value = ap["value"],
        ) for ap in data_local.json_data["receita"]]

        self.extrato = self.receita + self.gastos
    
        self.lucro = sum(Decimal(str(i._value)) for i in self.receita) - sum(Decimal(str(i._value)) for i in self.gastos)
        return
    
    def getSaldo(self,data_local:data) -> str:
        if data_local.show_saldo:
            return str(self.saldo)
        return "".join(["*" for i in range(len(str(self.saldo)))])

    def addItem(self,Item:Item) -> None: # Neste caso o else e nessesario
        if Item.getType == "Receita":
            self.receita.append(Item)
        else:
            self.gastos.append(Item)
        self.extrato.append(Item)

    def setNameGUI(self,data_local:data):
        try:
            if str(self.name).strip().lower() in ("", "none"):
                dialog = NameDialog()
                if dialog.exec() == QDialog.Accepted:
                    self.name = dialog.getName()
                    data_local.json_data["name"] = self.name
        except Exception as E:
            print(f"Erro Al inicar Login GUI, Erro: {E}")