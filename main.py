import discord
from discord.ext import commands
import asyncio
import keep_alive
import os
import datetime
import random
from random import choice
import time
import config
import os
import sqlite3 
from discord.ext.commands import CommandOnCooldown, BucketType

intents = discord.Intents.default() #default intents
intents.all()

#main code starts here!
client = commands.Bot(command_prefix='$', intents=intents, case_insensitive=True, allowed_mentions=discord.AllowedMentions(everyone=True))#$ is your prefix
client.remove_command("help")


@client.group(invoke_without_command=True)
async def help(ctx):
  em = discord.Embed(title = "Help", description = "Type $help <command> for more info on a command.",color = ctx.author.color)
  em.add_field(name = "Moderation", value = "kick , ban , unban , clear , addrole , removerole , unlock , lock , massrole , massroleremove ")
  await ctx.send(embed = em)


  
@help.command()
async def kick(ctx):

  em = discord.Embed(title="Kick", description = "Kicks a member from the guild.",color = ctx.author.color)
  em.add_field( name = "**Syntax**", value = "$kick <member> [reason]")
  await ctx.send(embed = em)

@help.command()
async def ban(ctx):

  em = discord.Embed(title="Ban", description = "Bans a member from the guild.",color = ctx.author.color)
  em.add_field( name = "**Syntax**", value = "$ban <member> [reason]")
  await ctx.send(embed = em)

@help.command()
async def clear(ctx):

  em = discord.Embed(title="Clear", description = "Clears messages.",color = ctx.author.color)
  em.add_field( name = "**Syntax**", value = "$clear <amount>")
  await ctx.send(embed = em)


@help.command()
async def unban(ctx):

  em = discord.Embed(title="Unban", description = "Unbans a banned user in the guild. ",color = ctx.author.color)
  em.add_field( name = "**Syntax**", value = "$unban  <membername#discriminator>")
  await ctx.send(embed = em)

@help.command()
async def addrole(ctx):

  em = discord.Embed(title="Addrole", description = "Adds a role to a member of the guild. ",color = ctx.author.color)
  em.add_field( name = "**Syntax**", value = "$addrole <membermention> <rolename or mention>")
  await ctx.send(embed = em)

@help.command()
async def removerole(ctx):

  em = discord.Embed(title="Removerole", description = "Removed a role from a member of the giuld. ",color = ctx.author.color)
  em.add_field( name = "**Syntax**", value = "$removerole <membermention> <rolename or mention>")
  await ctx.send(embed = em)

@help.command()
async def massrole(ctx):

  em = discord.Embed(title="Massrole", description = "Gives a role to many users at same time. Might take some seconds to give role. ",color = ctx.author.color)
  em.add_field( name = "**Syntax**", value = "$massrole <role> <members> ")
  await ctx.send(embed = em)

@help.command()
async def massroleremove(ctx):

  em = discord.Embed(title="Massroleremove", description = "Removes a role from many users at same time. Might take some seconds to give role. ",color = ctx.author.color)
  em.add_field( name = "**Syntax**", value = "$massroleremove <role> <members> ")
  await ctx.send(embed = em)

@help.command()
async def lock(ctx):

  em = discord.Embed(title="Lock", description = "Locks a channel. ",color = ctx.author.color)
  em.add_field( name = "**Syntax**", value = "$lock")
  await ctx.send(embed = em)

@help.command()
async def unlock(ctx):

  em = discord.Embed(title="Unlock", description = "Unlocks a channel. ",color = ctx.author.color)
  em.add_field( name = "**Syntax**", value = "$unlock")
  await ctx.send(embed = em)

#whatever code you want to add, do it after this line

@client.event
async def on_ready():
    """This Event Gets Triggered When The Bot Successfully Connects To The Internet!"""
    print("The Bot Is Now Ready To Run!")
    
@client.command(aliases = ['k'])
@commands.has_permissions(kick_members=True)
async def kick(ctx, member : discord.Member, *, reason = None):
      if member.guild_permissions.kick_members:
          embed = discord.Embed(title="", description=f"{ctx.author.mention} The member is protected.", color = ctx.author.color)    
          embed.set_author(name="Kick")
          embed.set_footer(text=f"Requested By: {ctx.author.name}#{ctx.author.discriminator}", icon_url=ctx.author.avatar_url)
          await ctx.send(embed=embed)
      else:
          if member == ctx.author:
              embed = discord.Embed(title="", description=f"{ctx.author.mention} It's Not Wise To Kick Your Self", color = ctx.author.color)    
              embed.set_author(name="Kick")
              embed.set_footer(text=f"Requested By: {ctx.author.name}#{ctx.author.discriminator}", icon_url=ctx.author.avatar_url)
              await ctx.send(embed=embed)
          else:
              try:
                  await member.kick(reason=reason)
                  embed = discord.Embed(title="", description=f"`{member.name}#{member.discriminator}` Was Kicked From `{ctx.guild.name}` By {ctx.author.mention} With Reason: `{reason}` Successfully!", color = ctx.author.color)    
                  embed.set_author(name="Kick")
                  embed.set_footer(text=f"Requested By: {ctx.author.name}#{ctx.author.discriminator}", icon_url=ctx.author.avatar_url)
                  await ctx.send(embed=embed)
              except:
                  embed = discord.Embed(title="", description=f"{ctx.author.mention} You Don't Have Permission To Do This!", color = ctx.author.color)    
                  embed.set_author(name="Kick")
                  embed.set_footer(text=f"Requested By: {ctx.author.name}#{ctx.author.discriminator}", icon_url=ctx.author.avatar_url)
                  await ctx.send(embed=embed)

@client.command(aliases = ['b'])
@commands.has_permissions(ban_members=True)
async def ban(ctx, member : discord.Member, *, reason = None):
      if member.guild_permissions.ban_members:
          embed = discord.Embed(title="", description=f"{ctx.author.mention} The member is protected.", color = ctx.author.color)    
          embed.set_author(name="Ban")
          embed.set_footer(text=f"Requested By: {ctx.author.name}#{ctx.author.discriminator}", icon_url=ctx.author.avatar_url)
          await ctx.send(embed=embed)
      else:
          if member == ctx.author:
              embed = discord.Embed(title="", description=f"{ctx.author.mention} You can't ban yourself, baka!", color = ctx.author.color)    
              embed.set_author(name="Ban")
              embed.set_footer(text=f"Requested By: {ctx.author.name}#{ctx.author.discriminator}", icon_url=ctx.author.avatar_url)
              await ctx.send(embed=embed)
          else:
              try:
                  await member.ban(reason=reason)
                  embed = discord.Embed(title="", description=f"`{member.name}#{member.discriminator}` Was Banned From `{ctx.guild.name}` By {ctx.author.mention} With Reason: `{reason}` Successfully!", color = ctx.author.color)    
                  embed.set_author(name="Ban")
                  embed.set_footer(text=f"Requested By: {ctx.author.name}#{ctx.author.discriminator}", icon_url=ctx.author.avatar_url)
                  await ctx.send(embed=embed)
              except:
                  embed = discord.Embed(title="", description=f"{ctx.author.mention} You Don't Have Permission To Do This!", color = ctx.author.color)    
                  embed.set_author(name="Ban")
                  embed.set_footer(text=f"Requested By: {ctx.author.name}#{ctx.author.discriminator}", icon_url=ctx.author.avatar_url)
                  await ctx.send(embed=embed)


@client.command()
@commands.has_permissions(ban_members=True)
async def unban(ctx, *, member):
	banned_users = await ctx.guild.bans()
	
	member_name, member_discriminator = member.split('#')
	for ban_entry in banned_users:
		user = ban_entry.user
		
		if (user.name, user.discriminator) == (member_name, member_discriminator):
 			await ctx.guild.unban(user)
 			await ctx.channel.send(f"Unbanned: {user.mention}")


@client.command(aliases = ['ar'])
async def addrole(ctx,  user: discord.Member, role: discord.Role,):
  if ctx.author.guild_permissions.manage_roles:
    await user.add_roles(role)
    await ctx.send(f"Successfully given the role to {user.mention}.")


@client.command(aliases = ['rr'])
async def removerole(ctx, user: discord.Member, role: discord.Role):
  if ctx.author.guild_permissions.manage_roles:
    await user.remove_roles(role)
    await ctx.send(f"Successfully removed the role from {user.mention}")



@client.command(aliases = ['madd'])
async def massrole(ctx, role: discord.Role, members: commands.Greedy[discord.Member]):
    for m in members:
        await m.add_roles(role)
        await asyncio.sleep(1)  # You don't want to get ratelimited!
    await ctx.send("Given role to mentioned members!")

@client.command(aliases = ['mrem'])
async def massroleremove(ctx, role: discord.Role, members: commands.Greedy[discord.Member]):
    for m in members:
        await m.remove_roles(role)
        await asyncio.sleep(1)  # You don't want to get ratelimited!
    await ctx.send("Removed the role from mentioned members! ___If the role is not removed from the members, Either you do not have permission to use this command or you need to mention the members too!___")



@client.command(aliases= ['purge','delete','clean'])
@commands.has_permissions(manage_messages=True)
async def clear(ctx, amount = 2):
   await ctx.channel.purge(limit = amount)



@client.command(aliases = ['l'])
@commands.has_permissions(manage_channels=True)
async def lock(ctx, channel : discord.TextChannel=None):
    overwrite = ctx.channel.overwrites_for(ctx.guild.default_role)
    overwrite.send_messages = False
    await ctx.channel.set_permissions(ctx.guild.default_role, overwrite=overwrite)
    await ctx.send('Channel locked.')
@lock.error
async def lock_error(ctx, error):
    if isinstance(error,commands.CheckFailure):
        await ctx.send('You do not have permission to use this command!')

@client.command(aliases = ['ul'])
@commands.has_permissions(manage_channels=True)
async def unlock(ctx, channel : discord.TextChannel=None):
    overwrite = ctx.channel.overwrites_for(ctx.guild.default_role)
    overwrite.send_messages = True
    await ctx.channel.set_permissions(ctx.guild.default_role, overwrite=overwrite)
    await ctx.send('Channel unlocked.')
@unlock.error
async def unlock_error(ctx, error):
    if isinstance(error,commands.CheckFailure):
        await ctx.send('You do not have permission to use this command!')

keep_alive.keep_alive()
token = os.environ.get("TOKEN")
# Run the client on the server
client.run('ODgzOTQzNjIwMzAwOTA2NTI2.GEZGWr.y5amxXmeIpoQ3ERu8VbT5kQjLzJ0D5m0XoDvgA')
