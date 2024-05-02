import discord
from discord.ext import commands
import os, shutil

import random

queue = []

image_names = []
download_folder = "downloads"
submission_folder = "forReview"
submission_names = []

soymins = []
with open("soymins.txt") as file:
    soymins = file.readlines()

def update_images():
        for filename in os.listdir(download_folder):
            image_names.append(os.path.join(download_folder, filename))

update_images()

intents = discord.Intents.all()

Bot = commands.Bot(command_prefix='!',intents=intents) 

@Bot.command()
async def soy(ctx, *args, **kwargs):
        if (len(image_names) > 0):
            random_image = random.choice(image_names)
            img = random_image
        else:
              img = image_names[0]

        await ctx.send(file=discord.File(img))

@Bot.command()
async def submitsoy(ctx, *args, **kwargs):

    if(len(ctx.message.attachments) > 0):
        i = 0
        while i < len(ctx.message.attachments):
            filename = ctx.message.attachments[i].filename
    
            if (ctx.message.attachments[i].content_type[0:5] == "image" and ctx.message.attachments[i].size < 8000001):
                await ctx.message.attachments[i].save(os.path.join(submission_folder, filename))
                await ctx.send("Soyjak submitted!")
            elif (ctx.message.attachments[i].content_type[0:5] != "image"):
                await ctx.send("File type not supported: " + ctx.message.attachments[i].content_type)
            elif (ctx.message.attachments[i].size >= 8000001):
                 await ctx.send("Error: File size greater than 8MB")
            else:
                 await ctx.send("Unknown error when submitting.")
            i += 1
    else:
        await ctx.send("No file attached.")

@Bot.command()
async def updatesoy(ctx, *args, **kwargs):
      image_names = []
      update_images()
      await ctx.send("Soys Updated!")

@Bot.command()
async def approvesoys(ctx, *args, **kwargs):
    if(ctx.author.name in soymins):
        for filename in os.listdir(submission_folder):
            shutil.move(os.path.join(submission_folder, filename), os.path.join(download_folder, filename))
        update_images()
        await ctx.send("Soys approved!")
    else:
        await ctx.send("You do not have permission to use that command")


@Bot.command()
async def reviewsoys(ctx, *args, **kwargs):
    if(ctx.author.name in soymins):
        for filename in os.listdir(submission_folder):
            await ctx.send(file=discord.File(os.path.join(submission_folder, filename)))

token = ""
with open("token.txt") as file:
    token = file.read()

Bot.run(token)
