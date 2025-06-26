import json
import base64
from cryptography.fernet import Fernet

# === Criação e carregamento da chave Fernet ===

# GERAÇÃO (somente 1x, e salve esse valor!)
# key = Fernet.generate_key()
# with open("chave.key", "wb") as f:
#     f.write(key)

# LEITURA da chave
with open("chave.key", "rb") as f:
    key = f.read()

fernet = Fernet(key)

# === JSON original ===
dados = {
    "name": "Quitto",
    "saldo": 190.50,
    "aplicacoes": [
        {
            "name": "CDB Banco X",
            "taxa_juros": 10.5,
            "type": "Renda Fixa",
            "moeda": "BRL",
            "min_aporte": 100.00,
            "prazo_meses": 12,
            "liquidez": 30
        }
    ],
    "receita": [
        {
            "id": 1,
            "name": "Salario",
            "descr": "Recebimento mensal",
            "type": "Receita",
            "coin": "BRL",
            "value": 5000
        }
    ],
    "gastos": [
        {
            "id": 2,
            "name": "Aluguel",
            "descr": "Despesa mensal",
            "type": "Gasto",
            "coin": "BRL",
            "value": 105
        }
    ]
}

# === Criptografar valores mantendo estrutura ===
def encrypt_value(value):
    if isinstance(value, (str, int, float)):
        text = str(value)
        enc = fernet.encrypt(text.encode())
        return base64.urlsafe_b64encode(enc).decode()
    elif isinstance(value, list):
        return [encrypt_value(v) for v in value]
    elif isinstance(value, dict):
        return {k: encrypt_value(v) for k, v in value.items()}
    else:
        return value

# === Descriptografar valores ===
def decrypt_value(value):
    if isinstance(value, str):
        try:
            enc_bytes = base64.urlsafe_b64decode(value.encode())
            dec = fernet.decrypt(enc_bytes).decode()
            # tenta converter pra número se der
            if dec.isdigit():
                return int(dec)
            try:
                return float(dec)
            except:
                return dec
        except Exception:
            return value
    elif isinstance(value, list):
        return [decrypt_value(v) for v in value]
    elif isinstance(value, dict):
        return {k: decrypt_value(v) for k, v in value.items()}
    return value

# # === CRIPTOGRAFAR e salvar no arquivo ===
# dados_criptografados = encrypt_value(dados)
# with open("data/data.json", "w") as f:
#     json.dump(dados_criptografados, f, indent=2)

print("✅ JSON criptografado salvo em 'data/data.json'.")

# === LER e DESCRIPTOGRAFAR ===
with open("data/data.json", "r") as f:
    dados_lidos = json.load(f)

dados_descriptografados = decrypt_value(dados_lidos)

print("\n🔓 JSON descriptografado:")
print(json.dumps(dados_descriptografados, indent=2))
