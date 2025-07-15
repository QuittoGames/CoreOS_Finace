from dataclasses import dataclass, field
import os
import json
import base64
from cryptography.fernet import Fernet


@dataclass
class data:
    modules_local = ["modules","data","UI"]
    _json_data: dict = field(default_factory=dict)
    Debug:bool = True
    show_saldo: bool = False
    data_json_path = r"data\data.json"
    path_local:str = ""
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
    def getKey(self) -> bytes:
        try:
            path = os.path.join(self.path_local,".env","key.key")
                  
            if not os.path.isfile(path):
                if self.Debug:print(f"[WARN] Arquivo de chave não encontrado em: {path}")
                return "" 
            
            with open(path, "rb") as file:
                self._key_json = file.read()
                if self.Debug: print("[NOTIFY] Key retrieved successfully")
                if len(self._key_json) != 44: 
                      print(f"[ERROR] Key inválida, tamanho esperado 44 bytes, mas tem {len(self._key_json)}")

                return self._key_json
        except FileNotFoundError as E:
            raise FileNotFoundError ("[ERROR] File Not Found in path")
        except PermissionError as E:
            raise PermissionError(["[SUDO] Permission Error"])
        
    def getFernet(self) -> str:
        return self._key_json
    
    """Verifica se o arquivo data.json existe na pasta local; 
    se existir, define o caminho local como padrão, 
    senão usa o caminho na pasta APPDATA do sistema.
    Trata erros de permissão e arquivo não encontrado."""
    def setEnvPath(self) -> str:
        try:
            appdata_path = os.path.join(os.getenv("APPDATA"), "CoreOS_Finace", "data")
            local_path = os.path.join(os.getcwd(), "data")
            
            if os.path.exists(local_path):
                self.path_local = local_path
            elif os.path.exists(appdata_path):
                self.path_local = appdata_path

            return self.path_local
        except PermissionError:
            raise PermissionError("[SUDO] Permission Error")
        except FileNotFoundError:
            raise FileNotFoundError("[ERROR] File Not Fond")


    def create_json(self,path:str) -> None:
        path = os.path.join(path,"data.json")
        try:
            os.makedirs(os.path.dirname(self.data_json_path), exist_ok=True)
            with open(path, "w", encoding="utf-8") as file:
                file.write(self.json_formart)
            return json.loads(self.json_formart)
        except PermissionError:
            print("Erro: Sem permissão para criar arquivo ou pasta.")
        except FileNotFoundError:
            print("Erro: Caminho não encontrado.")
        except OSError as e:
            print(f"Erro do sistema: {e}")


