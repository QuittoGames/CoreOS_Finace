from dataclasses import dataclass
import base64
from cryptography.fernet import Fernet

@dataclass
class Critografy:
    
    def is_encrypted(value: str) -> bool:
        try:
            # Tenta decodificar como base64 e ver se é um token válido do Fernet
            base64.urlsafe_b64decode(value.encode())
            return value.endswith("==") and len(value) > 100
        except Exception:
            return False
    
    @staticmethod
    def encrypt_value(value, fernet: Fernet):
        if isinstance(value, (str, int, float)):
            text = str(value)
            if isinstance(value, str) and Critografy.is_encrypted(value):
                return value  # Já está criptografado
            enc = fernet.encrypt(text.encode())
            return base64.urlsafe_b64encode(enc).decode()
        elif isinstance(value, list):
            return [Critografy.encrypt_value(v, fernet) for v in value]
        elif isinstance(value, dict):
            return {k: Critografy.encrypt_value(v, fernet) for k, v in value.items()}
        
        
    @staticmethod
    def decrypt_value(value_local, fernet: Fernet) -> dict:
        if isinstance(value_local, str):
            try:
                enc_bytes = base64.urlsafe_b64decode(value_local.encode())
                dec = fernet.decrypt(enc_bytes).decode()
                # Tenta converter pra número, se possível
                if dec.isdigit():
                    return int(dec)
                try:
                    return float(dec)
                except:
                    return dec
            except Exception:
                return value_local
        elif isinstance(value_local, list):
            return [Critografy.decrypt_value(v, fernet) for v in value_local]
        elif isinstance(value_local, dict):
            return {k: Critografy.decrypt_value(v, fernet) for k, v in value_local.items()}
        return value_local