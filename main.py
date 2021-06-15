import asyncio
import websockets
from  encryptor import EncryptionHandler

class Main:

    def __init__(self):
        self.zones = {}
        self.clients = {}
        self.zone_device_password = "TEST"
        self.encryption_handler = EncryptionHandler()
        self.encryption_handler.init_with_key()
    
    def handle_client():
        pass

    def handle_zone():
        pass
        
    def start_server(self):
        loop = asyncio.get_event_loop()
        loop.run_until_complete(
            websockets.serve(self.check_declaration,self.host,self.port,ping_interval=None))
        loop.run_forever()

