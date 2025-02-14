import discord
from graph import plt
from discord.ext import commands

prefix = ';'

intents = discord.Intents.default()
bot = commands.Bot(command_prefix=prefix, intents=intents)
intents.message_content = True

graph_help = f"seperate shit with pipe |\n" \
             f"{prefix}graph sin(x)\n" \
             f"{prefix}graph sin(x)|cos(x)\n\n" \
             f"you can add a range of x values:\n" \
             f"{prefix}graph sin(x)|1,2\n" \
             f"you can also add a range of y values:\n" \
             f"{prefix}graph sin(x)|1,2,3,4\n" \

class CustomHelpCommand(commands.DefaultHelpCommand):
    def __init__(self):
        super().__init__()
        self.no_category = "Commands"

    async def send_bot_help(self, mapping):
        embed = discord.Embed(
            title="Send Help",
            description="graphy bot graphs graphs thank you\nsource code at https://github.com/KreconyMakaron/graphy",
            color=discord.Color.green()
        )

        for cog, commands_list in mapping.items():
            command_names = [command.name for command in commands_list]
            if command_names:
                cog_name = cog.qualified_name if cog else self.no_category
                embed.add_field(
                    name=cog_name,
                    value=", ".join(f"`{prefix}{name}`" for name in command_names),
                    inline=False
                )

        embed.set_footer(text=f"Use {prefix}help <command> for more details.")

        await self.get_destination().send(embed=embed)

bot.help_command = CustomHelpCommand()

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")

@bot.command(help=graph_help, brief="graphs a funcion duh")
async def graph(ctx, *, formula: str = ""):
    if formula == "":
        await ctx.send("no graph provided womp womp")
        return

    try:
        p, f, xlim, ylim = plt(formula)
        p.save('image.png')

        embed = discord.Embed(
            title=f"Graph of {f}",
            description=f"{'' if xlim is None else f' x = [{xlim[0]}, {xlim[1]}]'}{'' if ylim is None else f' y = [{ylim[0]}, {ylim[1]}]'}",
            color=discord.Color.blue()
        )

        file = discord.File("./image.png", filename="image.png")
        embed.set_image(url="attachment://image.png")
        await ctx.send(file=file, embed=embed)
    except Exception as e:
        await ctx.send(f'shit: {e}')
        return

bot.run(open('token').read())
