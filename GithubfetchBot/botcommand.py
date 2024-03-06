from botsetup import bot,logger,TOKEN

def run_bot()->None:
  
  
  @bot.event
  async def on_ready():
    logger.info(f'user:{bot.user.name}  (ID:{bot.user.id}) has connected to Discord!')
  
  @bot.command(
    help="Responds with 'Pong!' and the latency in milliseconds."
  )
  async def ding(ctx):
    await ctx.send(f'Pong! {round(bot.latency*1000)}ms')
    
  @bot.command()
  async def add(ctx,a:int,b:int):
    await ctx.send(f'{a}+{b}={a+b}')
    
  bot.run(TOKEN,root_logger=True)
    
    