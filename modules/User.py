from dataclasses import dataclass
from decimal import Decimal
import os
import sys
sys.path.append(os.path.abspath(".."))
from data import data

@dataclass
class User:
    saldo:Decimal = 0.0
    aplicaçoes = []
    receita = []
    gastos = []
    extrato = []

    async def set_values(data_local: data):
        pass