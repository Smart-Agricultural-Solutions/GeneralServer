
from cryptography.fernet import Fernet
class EncryptionHandler:
    def __init__(self):
        self.client_keys = {}
	def init_with_key(self):
		with open("privatekey.txt" , "rb" ) as file:
			self.key = file.read()
			self.f= Fernet(self.key)
	def make_key(self):
	    key = Fernet.generate_key()
		self.key = key
		self.f = Fernet(self.key)
		return key

    def add_key_for_client(self,name,key):
        self.client_keys[name] =key

    def post_handshake_decrypt(self,name,message):
        decryptor =Fernet(self.client_keys[name])
        return decryptor.decrypt(message)

    def post_handshake_encrypt(self,name,message):
        decryptor =Fernet(self.client_keys[name])
        return decryptor.encrypt(message)

	def decrypt(self , message):
		return self.f.decrypt(message)

	def encrypt(self , message):
		return self.f.encrypt(message)