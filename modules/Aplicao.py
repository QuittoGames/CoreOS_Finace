from dataclasses import dataclass
from decimal import Decimal

@dataclass
class Aplicao:
    _name: str
    _taxa_juros: Decimal
    _tipo: str
    _moeda: str
    _min_aporte: Decimal
    _prazo_meses: int
    _liquidez: str

    # Getters
    def get_name(self): return self._name
    def get_taxa_juros(self): return self._taxa_juros
    def get_tipo(self): return self._tipo
    def get_moeda(self): return self._moeda
    def get_min_aporte(self): return self._min_aporte
    def get_prazo_meses(self): return self._prazo_meses
    def get_liquidez(self): return self._liquidez

    # Exibição
    def __str__(self):
        return (
            f"[APLICAÇÃO FINANCEIRA]\n"
            f"Nome        : {self._name}\n"
            f"Tipo        : {self._tipo}\n"
            f"Moeda       : {self._moeda}\n"
            f"Taxa Juros  : {self._taxa_juros:.2f}% ao ano\n"
            f"Min. Aporte : {self._moeda} {self._min_aporte:.2f}\n"
            f"Prazo       : {self._prazo_meses} meses\n"
            f"Liquidez    : {self._liquidez}"
        )
