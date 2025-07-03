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

    json_formart = """
{
  "name": null,
  "saldo": 0,
  "aplicacoes": [
    {
      "name": null,
      "taxa_juros": 0,
      "type": null,
      "moeda": null,
      "min_aporte": 0,
      "prazo_meses": 0,
      "liquidez": null
    }
  ],
  "receita": [
    {
      "id": null,
      "name": null,
      "descr": null,
      "type": null,
      "coin": null,
      "value": 0
    }
  ],
  "gastos": [
    {
      "id": null,
      "name": null,
      "descr": null,
      "type": null,
      "coin": null,
      "value": 0
    }
  ]
}
"""
    
    #Getters
    #In Dev
    def getKey(self) -> str:
        try:
            path = os.path.join("data", ".env", "key.key")
            if not os.path.exists(path):
                path = os.path.join(os.getenv("APPDATA"), "CoreOS_Finace", "data") # Appdata Local App
                  
            if not os.path.isfile(path):
                if self.Debug:print(f"[WARN] Arquivo de chave não encontrado em: {path}")
                return "" 
        
            with open(path, "rb") as file:
                self._key_json = file.read()
                if self.Debug: print("[NOTIFY] Key retrieved successfully")
                return self._key_json
        except FileNotFoundError as E:
            raise FileNotFoundError ("[ERROR] File Not Found in path")