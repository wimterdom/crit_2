import pyperclip
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding

with open("private_key.pem", "rb") as private_key_file:
        private_key = serialization.load_pem_private_key(
            private_key_file.read(),
            password=None,
            backend=default_backend()
        )

with open("public_key.pem", "rb") as key_file:
		public_key = serialization.load_pem_public_key(
        	key_file.read(),
        	backend=default_backend()
    )

print("Please input data you want decode: ")
data = input()

decrypted_value = private_key.decrypt(
                    data,
                    padding.OAEP(
                        mgf=padding.MGF1(algorithm=hashes.SHA256()),
                        algorithm=hashes.SHA256(),
                        label=None
                    )
                )
print("Decoded data: ", decrypted_value.decode())
#6c734d17bfeb2267c946cacb0f65b990f7dbe4f94d24ff35fe2155c98d6755b9051d17ce684bde566c8e8386da56ab80c2d41908d453c6668ddc478c0bb5da4a52ca4482feab6e29cfd91f7d3d8c3e9ef4c9b08b06fe1fc428168e6abbf4848c938256765c93cf746419ceca03af912d3d3c270ef8abdcf93b88320e351fd59d8e07113949b284846bcc909d1aec8f8e2fcf88d3cf4fd22d8cf0ef6b8125b78e4191aefca1e9f63b81db79d9bbab521488cb66a98d9d3470f9a81edd3981c5b4f2ea882ce07539ce9dc3daac0f306a465fcfa9f4f168b5d6f3af812de4031a23f85138506783726c8aefa6f0d4e204f908e12c5f5d54d45bd53cf884d1a988de