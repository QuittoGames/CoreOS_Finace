from dataclasses import dataclass
from random import randint
from tool import tool
from data import data

@dataclass
class Item:
    _ID: int
    _name: str
    _descr: str
    _type: str
    _coin: str  # Money Type (Real, BTC, Dólar)

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
    
    @classmethod
    def generete_nunber(cls) -> int:
        IDs = []
        for i in ["receita", "gastos"]:
            if i in data.json_data:
                IDs += [item["id"] for item in data.json_data[i]]

        while True:
            id_local = randint(0, 1000)
            if tool.binary_search(array=IDs, target=id_local):
                return id_local


    def __str__(self):
        return (
            f"[RECEITA]\n"
            f"ID       : {self.ID}\n"
            f"Nome     : {self.name}\n"
            f"Descrição: {self.descr}\n"
            f"Moeda    : {self.coin}"
        )
