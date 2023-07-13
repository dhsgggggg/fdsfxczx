from telethon import TelegramClient, events

# replace the values below with your own API ID, API Hash, and phone number
api_id = '27198560'
api_hash = '5f300eb6636fd8c30cd7da8cbf2c23ef'
phone_number = '6211037784:AAFEHEFovdUbCZ1qj2c_V9Plw7VpaFY1KsY'

with TelegramClient('my_bot', api_id, api_hash) as client:
    @client.on(events.NewMessage(pattern='/start'))
    async def start(event):
        await event.respond('Hello, World!')
        raise events.StopPropagation

    client.start()
    client.run_until_disconnected()
