from dataclasses import dataclass
from decimal import Decimal

@dataclass
class Aplicao:
    _name: str
    _taxa_juros: Decimal
    _type: str
    _moeda: str
    _min_aporte: Decimal
    _prazo_meses: int
    _liquidez: Decimal

    # Getters
    def getName(self) -> None: return self._name
    def getTaxaJuros(self) -> None: return self._taxa_juros
    def getType(self) -> None: return self._type
    def getMoeda(self) -> None: return self._moeda
    def getMinAporte(self) -> None: return self._min_aporte
    def getPrazoMeses(self) -> None: return self._prazo_meses
    def getLiquidez(self)-> None : return self._liquidez

    # Seters
    def setMinAporte(self, min_aporte:Decimal):self._min_aporte = min_aporte

    # Exibição
    def __str__(self):
        return (
            f"[APLICAÇÃO FINANCEIRA]\n"
            f"Nome        : {self._name}\n"
            f"Tipo        : {self._type}\n"
            f"Moeda       : {self._moeda}\n"
            f"Taxa Juros  : {self._taxa_juros:.2f}% ao ano\n"
            f"Min. Aporte : {self._moeda} {self._min_aporte:.2f}\n"
            f"Prazo       : {self._prazo_meses} meses\n"
            f"Liquidez    : {self._liquidez}"
        )
