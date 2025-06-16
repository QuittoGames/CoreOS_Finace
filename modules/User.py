from dataclasses import dataclass
from decimal import Decimal

@dataclass
class User:
    saldo:Decimal = 0.0
    aplicaçoes = []
    receita = []
    gastos = []
    extrato = []
