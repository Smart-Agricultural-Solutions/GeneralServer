import asyncio
import json

class ClientHandler:
    def __init__(self,websocket,name,super_user_status,parent):
        self.websocket = websocket
        self.name = name
        self.super_user = super_user_status
        self.parent = parent

    async def listen_for_request(self):
            try:
                await asyncio.wait_for(self.websocket.recv() ,5)
            except:
                pass

    async def gather_zone_data(self):
        zones = self.parent.zones.keys()
        holder = []
        for zone in zones:
            await zone.send("basic_data")
            data = await zone.recv()
            holder.append(data)
        encrypted_data = self.parent.encryption_handler.post_handshake_encrypt(self.name,json.loads(holder))
        self.websocket.send(encrypted_data)
