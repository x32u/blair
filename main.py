import discord
import jishaku 
import os 
import dotenv

from discord.ext       import commands

from tools.blare       import Blare

dotenv.load_dotenv()

token = "MTE2MTUyOTU5NzAxMjIyNjA5OQ.GQpPtq.4VT-V2syM1iVKlnDCqjZ814qkvxAsscbWvbkXo"

Blare(token=token)
