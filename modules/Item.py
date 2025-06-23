from dataclasses import dataclass
from random import randint
from tool import tool
from data import data
from decimal import Decimal

@dataclass
class Item:
    _ID: int
    _name: str
    _descr: str
    _type: str
    _coin: str  # Money Type (Real, BTC, Dólar)
    _value: Decimal = (0.0)

    def getID(self) -> str:
        return self.ID 
    
    def getName(self) -> str:
        return self.name
    
    def getDesc(self) -> str:
        return self.descr
    
    def getType(self) -> str:
        return self._type
    
    def getCoin(self) -> str:
        return self.coin
    
    def getValue(self):
        return self._value
    
    @classmethod
    def generete_nunber(self) -> int:
        IDs = []
        for i in ["receita", "gastos"]:
            if i in data.json_data:
                IDs += [i["id"] for i in data.json_data[i]] # Sum Arry [0,1,2,3] + [4,5,6,7] = [0,1,2,3,4,5,6,7] sim quase niguem lembra disso
        
        while True:
            id_local = randint(0,1000)
            if tool.binary_search(array = IDs, target = id_local):
                return id_local

    def __str__(self):
        return (
            f"[RECEITA]\n"
            f"ID       : {self.ID}\n"
            f"Nome     : {self.name}\n"
            f"Descrição: {self.descr}\n"
            f"Moeda    : {self.coin}"
        )
