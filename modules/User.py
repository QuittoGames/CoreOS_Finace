from dataclasses import dataclass, field
from decimal import Decimal,InvalidOperation
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
from modules.Cripitografy import Critografy
import json

@dataclass
class User:
    saldo:Decimal = (0.0)
    name:str = ""
    aplicacoes: list = field(default_factory=list)
    receita: list = field(default_factory=list)
    gastos: list = field(default_factory=list)
    extrato: list = field(default_factory=list)
    lucro: Decimal = (0.0)

    #Const
    NOT_ATTR_JSON :tuple = (
            "__class__", "__dict__", "__doc__", "__module__", "__weakref__",
            "__annotations__", "__dataclass_fields__", "__dataclass_params__",
            "__init__", "__str__", "__repr__", "__eq__", "__ne__", "__lt__", "__le__",
            "__gt__", "__ge__", "__format__", "__getattribute__", "__setattr__",
            "__delattr__", "__init_subclass__", "__new__", "__reduce__", "__reduce_ex__",
            "__sizeof__", "__subclasshook__", "__match_args__", "__getstate__",
            "__replace__", "__dir__", "addItem", "saveUserInJson", "set_values",
            "setNameGUI", "getSaldo","lucro","NOT_ATTR_JSON", "__hash__","__static_attributes__","__firstlineno__"
        )

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


        #Open File Json
        tool.openJson(data_local,fernet)

        raw_saldo = data_local._json_data.get("saldo")

        try:
            self.saldo = Decimal(str(raw_saldo))
        except (InvalidOperation, TypeError, ValueError):
            if data_local.Debug:
                print(f"[WARN] Saldo inválido no JSON ({raw_saldo}), usando 0.0")
            self.saldo = Decimal("0.0")

        # self.name = str(data_local._json_data["name"])
        self.name = Critografy.decrypt_value(data_local._json_data["name"], fernet)
        if data_local.Debug:
            print(">>>> TESTE DESCRIPTOGRAFIA")

            criptografado = data_local._json_data.get("name")
            descriptografado = Critografy.decrypt_value(criptografado, fernet)
            print(f"Name Original: {criptografado}")
            print(f"Name Decrypt : {descriptografado}")
            return
        #For in Json
        #Refactor for mutiple funcs
        try:
            self.aplicacoes = [Aplicao(
                _name=str(ap["name"]),
                _taxa_juros=ap["taxa_juros"],
                _type=ap["type"],
                _moeda=ap["moeda"],
                _min_aporte=Decimal(str(ap["min_aporte"])),
                _prazo_meses=ap["prazo_meses"],
                _liquidez=ap["liquidez"],
            )for ap in data_local._json_data["aplicacoes"]if ap is not None] 
        except (InvalidOperation, ValueError, TypeError) as E:
            self.aplicacoes = []
            if data_local.Debug:print(f"[WARN] Aplicação inválida ignorada, Erro: {E}")

        try:
            self.gastos = [Item(
                _ID = Item.generete_nunber(data_local=data_local),
                _name = ap["name"],
                _descr = ap["descr"],
                _type = ap["type"],
                _coin = ap["coin"],
                _value = ap["value"],
            ) for ap in data_local._json_data["gastos"]if ap is not None]
        except (InvalidOperation, ValueError, TypeError) as E:
            self.gastos = []
            if data_local.Debug:print(f"[WARN] Gastos Item inválida ignorada, Erro: {E}")

        try:
            self.receita = [Item(
                _ID = Item.generete_nunber(data_local=data_local),
                _name = ap["name"],
                _descr = ap["descr"],
                _type = ap["type"],
                _coin = ap["coin"],
                _value = ap["value"],
            ) for ap in data_local._json_data["receita"] if ap is not None]
        except (InvalidOperation, ValueError, TypeError) as E:
            self.receita = []
            if data_local.Debug:print(f"[WARN] Receita inválida ignorada, Erro: {E}")
            
        self.extrato = self.receita + self.gastos if self.receita and self.gastos else []
    
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
            if (str(data_local._json_data["name"]).strip().lower()) in ("", "none"):
                dialog = NameDialog()
                if dialog.exec() == QDialog.Accepted:
                    self.name = dialog.getName()
                    # self.name = data_local.json_data["name"]
        except Exception as E:
            print(f"Erro Al inicar Login GUI, Erro: {E}")

    #Nao foi possivel aplicar em um for portanto teve quer feito na mao
    def saveUserInJson(self, data_local: data) -> None:
        try:
            data_local._json_data["name"] = self.name
            data_local._json_data["saldo"] = str(self.saldo)  # Decimal → string

            data_local._json_data["aplicacoes"] = [
                {
                    "name": ap._name,
                    "taxa_juros": ap._taxa_juros,
                    "type": ap._type,
                    "moeda": ap._moeda,
                    "min_aporte": str(ap._min_aporte),
                    "prazo_meses": ap._prazo_meses,
                    "liquidez": ap._liquidez
                } for ap in self.aplicacoes
            ]

            data_local._json_data["receita"] = [
                {
                    "id": it._ID,
                    "name": it._name,
                    "descr": it._descr,
                    "type": it._type,
                    "coin": it._coin,
                    "value": it._value
                } for it in self.receita
            ]

            data_local._json_data["gastos"] = [
                {
                    "id": it._ID,
                    "name": it._name,
                    "descr": it._descr,
                    "type": it._type,
                    "coin": it._coin,
                    "value": it._value
                } for it in self.gastos
            ]

            if data_local.Debug:
                print(f"[DEBUG] Json Name: {data_local._json_data['name']}")
                print(f"[DEBUG] Json Saldo: {data_local._json_data['saldo']}")
                print(f"[DEBUG] Json Aplicacoes: {len(data_local._json_data['aplicacoes'])} entradas")
        except Exception as E:
            raise Exception(f"Erro ao salvar usuário no JSON: {E}")
