import discord
import random

# Zmienna intencje przechowuje uprawnienia bota
intents = discord.Intents.default()
# Włączanie uprawnienia do czytania wiadomości
intents.message_content = True
# Tworzenie bota w zmiennej klienta i przekazanie mu uprawnień
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Zalogowaliśmy się jako {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('!info'):
        await message.channel.send("Śmieci i kolory ich koszy:" +
                                   " Papier - Niebieski,"
                                   " Metale i tworzywa sztuczne - Żółty,"
                                   " Szkło - Żielony,"
                                   " Odpady bio - Brązowy,"
                                   " Odpady zmieszane - Czarny")
    if message.content.startswith("!konsekwencje"):
        await message.channel.send("1. można odszymać mandat w wyskości 500zł za niesegregowanie śmieci," +
                                   " 2. zużywanie większej ilości surowców co powoduje ich braku,"
                                   " 3.zanieczyszczenie środowiska wokół nas.,"
                                   " 4.brak segregacji powoduje wymieranie niektórych gatównków zwierząt")
    
    if message.content.startswith("!zapobieganie"):
        await message.channel.send("Jak zapobiedz temu zanieczyszczeniu środowiska itp.:" +
                                    " Zegregowanie śmieci,"
                                    " Czytanie e-booków zamiast zwykłych książek,"
                                    " Korzystanie z wersji cyfrowych i zużywanie mniej surowców mnieralnych")
        
client.run("Your Discord bot token!")
