from cryptography.fernet import Fernet

with open('key.key', 'rb') as key_file:
    key = key_file.read()
cipher = Fernet(key)
with open('script.py', 'rb') as file:
    encrypted_file = file.read()

decrypted_file = cipher.decrypt(encrypted_file)
exec(decrypted_file)
