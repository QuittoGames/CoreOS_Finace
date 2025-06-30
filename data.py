from dataclasses import dataclass, field
import os

@dataclass
class data:
    modules_local = ["modules","data","UI"]
    json_data: dict = field(default_factory=dict)
    Debug:bool = True
    show_saldo: bool = False
    data_json_path = r"data\data.json"
    _key_json:str = ""

    json_formart = """"""
    
    #Getters
    #In Dev
    def getKey(self) -> str:
        try:
            path = os.path.join("data", ".env", "key.key")
            if not os.path.exists(path):raise FileNotFoundError("File Not Exit")
    
            with open(path, "rb") as file:
                self._key_json = file.read()
                return self._key_json
        except FileNotFoundError as E:
            raise FileNotFoundError ("File Not Found in path")