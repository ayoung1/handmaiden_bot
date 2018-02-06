import discord
import asyncio

class Handmaiden:
    def __init__(self, token):
        self.client = discord.Client()
        self.token = token

    def run(self):
        self.client.run(self.token)

