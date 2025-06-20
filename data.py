from dataclasses import dataclass, field

@dataclass
class data:
    modules_local = ["modules","data"]
    json_data: dict = field(default_factory=dict)
    Debug:bool = False
    show_saldo: bool = False
    data_json_path = r"data\data.json"

    json_formart = """"""
