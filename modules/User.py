from dataclasses import dataclass
from decimal import Decimal
from Gasto import Gasto
from Receita import Recita 

@dataclass
class User:
    saldo:Decimal = 0.0
    aplicaçoes = []
    receita = []
    gastos = []
    extrato = []
