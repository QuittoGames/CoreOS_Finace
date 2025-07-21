from dataclasses import dataclass
import base64
from cryptography.fernet import Fernet

@dataclass
class Critografy:
    
    @staticmethod
    def is_encrypted(value: str) -> bool:
        try:
            # Verifica se é uma string base64 válida e longa o suficiente
            decoded = base64.urlsafe_b64decode(value.encode())
            return value.endswith("==") and len(decoded) > 60  # comprimento típico de token Fernet
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
    def decrypt_value(value_local, fernet: Fernet):
        if isinstance(value_local, str):
            try:
                enc_bytes = base64.urlsafe_b64decode(value_local.encode())
                dec = fernet.decrypt(enc_bytes).decode()

                # Tenta converter para número se possível
                try:
                    return int(dec)
                except ValueError:
                    try:
                        return float(dec)
                    except ValueError:
                        return dec
            except Exception:
                return value_local
        elif isinstance(value_local, list):
            return [Critografy.decrypt_value(v, fernet) for v in value_local]
        elif isinstance(value_local, dict):
            return {k: Critografy.decrypt_value(v, fernet) for k, v in value_local.items()}
        return value_local
