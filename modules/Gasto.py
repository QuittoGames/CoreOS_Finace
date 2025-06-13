from dataclasses import dataclass
from decimal import Decimal
from Receita import Recita

@dataclass 
class Gasto(Recita):
    _value:Decimal

    def getValue(self):return self.value

    def setValue(self, value:Decimal):
        self._value = value

    def __str__(self):
        return (
            f"[GASTO]\n"
            f"ID       : {self.ID}\n"
            f"Nome     : {self.name}\n"
            f"Descrição: {self.descr}\n"
            f"Moeda    : {self.coin}\n"
            f"Valor    : {self.coin} {self.value:.2f}"
        )
