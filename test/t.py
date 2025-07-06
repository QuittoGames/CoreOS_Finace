import os

install_path = os.path.join(os.getenv("APPDATA"), "CoreOS_Finace", "data") # Appdata Local App
key_path = os.path.join(install_path, ".env","key.key")

print(os.getenv("APPDATA"))
print(install_path)
print(key_path)