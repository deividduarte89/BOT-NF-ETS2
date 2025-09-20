import discord
import asyncio
import warnings
import os

warnings.filterwarnings("ignore")

# -------------------- CONFIG --------------------
TOKEN = os.getenv("DISCORD_TOKEN")  # Agora o token é lido da variável de ambiente
DELAY_SECONDS = 5  # tempo de espera entre mensagens
# -------------------------------------------------

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f"Bot pronto como {client.user} (id: {client.user.id})")

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.attachments:
        for att in message.attachments:
            if att.filename.lower().endswith(".pdf"):
                # Mensagem inicial
                typing = await message.channel.send(f"📄 Processando `{att.filename}`...")
                
                # Simula validação passo a passo
                await asyncio.sleep(DELAY_SECONDS)
                await typing.edit(content=f"🔎 Validando informações da Nota Fiscal `{att.filename}`...")

                await asyncio.sleep(DELAY_SECONDS)
                await typing.edit(content=f"📡 Verificando junto à SEFAZ `{att.filename}`...")

                await asyncio.sleep(DELAY_SECONDS)
                await typing.edit(content=f"✅ Nota Fiscal `{att.filename}` liberada com Sucesso!")

# Inicia o bot
if TOKEN is None:
    print("Erro: a variável de ambiente DISCORD_TOKEN não está definida!")
else:
    client.run(TOKEN)
