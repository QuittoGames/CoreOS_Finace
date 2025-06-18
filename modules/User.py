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
    
    async def set_values(self,data_local: data):
        path = os.path.join(data.data_json_path)
        if not os.path.exists(path=path):tool.create_json(path)

        with open(data.data_json_path, "r+") as file:
            data.json_data = file.read()
            data.json_data = json.loads(data.json_data)  # ← CONVERTE de string JSON para dict

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
        ) for ap in data.json_data["gastos"]]

        self.receita = [Item(
            _ID = Item.generete_nunber(),
            _name = ap["name"],
            _descr = ap["descr"],
            _type = ap["type"],
            _coin = ap["coin"],
        ) for ap in data.json_data["receita"]]

        self.extrato = self.receita + self.gastos
        return
    
    def getExtrato(self):
        print("=" * 50)
        print("📄  EXTRATO FINANCEIRO".center(50))
        print("=" * 50)
        print(f"💰  Saldo atual: R$ {self.saldo:.2f}".center(50))
        print("-" * 50)

        categorias = [
            ("📈 RECEITAS", self.receita),
            ("📉 GASTOS", self.gastos),
            ("📊 APLICAÇÕES", self.aplicaçoes)
        ]

        for titulo, lista in categorias:
            print(f"\n{titulo}")
            print("─" * 50)

            if not lista:
                print("  ⚠️  Nenhum item cadastrado.\n")
                continue

            for item in lista:
                print("┌" + "─" * 48 + "┐")
                for attr, value in item.__dict__.items():
                    nome = attr[1:] if attr.startswith("_") else attr
                    print(f"│ {nome.capitalize():<15}: {str(value):<29}│")
                print("└" + "─" * 48 + "┘")

        print("=" * 50)


        