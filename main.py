import nextcord
from nextcord.ext import commands
from lib import untitlable

token_file = open(
    "token.txt", 
    "r"
    )
token = token_file.read()
token_file.close()

bot = commands.Bot()
intents = nextcord.Intents.all()
test_servers = [937639594030153758]
@bot.event
async def on_ready():
    print(f"We have logged in as {bot.user}")

@bot.slash_command(
    description = "Generate a graph for the next 7 day weather for certain cordinates", 
    force_global = True, 
    dm_permission = True, 
    guild_ids=test_servers
)
async def weather(
    interaction: nextcord.Interaction, 
    latitude: str = nextcord.SlashOption(
        description = "The latitude of the city you want to get the weather status of.", 
        required = False
    ), 
    longitude: str = nextcord.SlashOption(
        description = "The longitude of the city you want to get the weather status of.", 
        required = False
    ),
):
        
    await interaction.response.defer()
    try:
        lat = float(latitude)
        lon = float(longitude)
    except e:
        print(e)
    status = untitlable(lat=latitude, lon=longitude)
    if status == True:
        await interaction.followup.send(file=nextcord.File("weather.png"))
    else:
        await interaction.followup.send("Invalid arguments")
bot.run(token)