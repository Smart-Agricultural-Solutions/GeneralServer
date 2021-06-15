import asyncio
import json
import websockets
from websockets.auth import Credentials
from  encryptor import EncryptionHandler

class Main:

    def __init__(self):
        self.zones = {}
        self.clients = {}
        self.zone_device_password = "TEST"
        self.encryption_handler = EncryptionHandler()
        self.encryption_handler.init_with_key()
        self.attempts = {}
    
    async def handle_client():
        pass

    async def handle_zone():
        pass

    async def is_authed():
        pass

    def is_banned(self,ip):
        if ip in self.attempts:
            if self.attempts[ip] > 3:
                return True
            else:
                return False
        return False

    async def shake_hands(self,websocket):
        hand_shake_data = await websocket.recv()
        decrypted_data = EncryptionHandler.decrypt(hand_shake_data)
        credentials = json.dumps(decrypted_data)
        if self.is_authed(credentials) == True:
            pass
    
    def start_server(self):
        loop = asyncio.get_event_loop()
        loop.run_until_complete(
            websockets.serve(self.shake_hands,self.host,self.port,ping_interval=None))
        loop.run_forever()