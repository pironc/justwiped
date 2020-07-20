# importing the libraries (discord.py and beautiful soup)
import discord
from discord.ext import commands
import requests
from bs4 import BeautifulSoup
import time
from datetime import datetime
import re

client = commands.Bot(command_prefix = '/')
client.remove_command("help")

@client.event
async def on_ready():
    print("The bot is ready")

    # Checking what channel to send the message to
    channel = client.get_channel(your channel ID)

    # Oldserver and curserver are compared to know if a new server has wiped. Some print functions
    # are just used for the debugging, however you can remove them if you don't want to have them running in your terminal.

    # You can also remove the 7th line (datetime, not time as it's used for the sleep method!!)
    # since it's used to print the current time with the current and old server in your terminal.

    oldserver = "n/a"

    # This while loop is used to check every X seconds (just modify the time.sleep() lines) in order to loop the wipe checker
    while (1):
        # Fetching the URL to know which website to search on.
        # You can modify it to another just-wiped link with custom filters.
        url="https://just-wiped.net/rust_servers"

        # Make a GET request to fetch the raw HTML content
        html_content = requests.get(url).text

        # Parse the html content
        soup = BeautifulSoup(html_content, "lxml")
    
        curserver = soup.find("div", attrs={"class": "servers"})
        players = soup.find("div", attrs={"class": "info i-player"}).find("div", attrs={"class": "value"})

        t = time.localtime()
        current_time = time.strftime("%H:%M:%S", t)
        curserver = soup.find("a", attrs={"class": "name"})
        curserver = curserver.text
        print("[", current_time, "] Cur server : ", curserver.partition("\n")[0])
        print("[", current_time, "] Old server : ", oldserver.partition("\n")[0], "\n")

        # The if statement is used to check if the latest-checked server is also the current server shown on the list.
        # If not, it will send a message with the name of the server and some other informations.
        if (curserver != oldserver):
            oldserver = curserver
            t = time.localtime()
            current_time = time.strftime("%H:%M:%S", t)
            print("[", current_time, "] (curserver != oldserver) Old server : ", oldserver.partition("\n")[0])
            print("[", current_time, "] (curserver != oldserver) New server : ", curserver.partition("\n")[0])
            await channel.send("```Latest wipe : {}``````Player(s) : {}```".format(re.sub('BP Wipe', '', curserver), players.text.strip().partition("\n")[0]))
        time.sleep(30)

# You will need to have a bot and its token, then just simply put it in the quotes
client.run('your bot token')
