import vk_api
import config

class Helpers:
    def __init__(self):
        self.vk = vk_api.VkApi(token=f"{config.BOT_TOKEN}")
        self.api = self.vk.get_api()
    
    async def get_user_name(self, event):
        user_info  = self.api.users.get(user_ids=event.from_id)
        sender_name = user_info[0]['first_name']
        return sender_name