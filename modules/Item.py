from dataclasses import dataclass

@dataclass
class Item:
    _ID: int
    _name: str
    _descr: str
    _type: str
    _coin: str  # Money Type (Real, BTC, Dólar)

    def getID(self) -> None:
        return self.ID 
    
    def getName(self) -> None:
        return self.name
    
    def getDesc(self) -> None:
        return self.descr
    
    def getType(self) -> None:
        return self._type
    
    def getCoin(self) -> None:
        return self.coin

    def __str__(self):
        return (
            f"[RECEITA]\n"
            f"ID       : {self.ID}\n"
            f"Nome     : {self.name}\n"
            f"Descrição: {self.descr}\n"
            f"Moeda    : {self.coin}"
        )
