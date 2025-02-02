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

Bot = commands.Bot(command_prefix='!',intents=intents, help_command=None)

@Bot.command()
async def help(ctx, *args, **kwargs):
    await ctx.send(content="## 'Jak Bot is here to help!\n```!help\tDisplays this help message\n!soy\tGenerates a random soyjak\n!submitsoy\tAllows you to submit a 'jak to be generated (With admin approval)\n!soycount\tShows how many possible 'jaks we I can currently generate```", ephemeral=True)

@Bot.command()
async def soy(ctx, *args, **kwargs):
        if (len(image_names) > 0):
            random_image = random.choice(image_names)
            img = random_image
        else:
              img = image_names[0]

        chadChance = random.randint(1, 2000)
        if chadChance == 777:
            await ctx.send(content="Nope, that guy's too based.", file=discord.File("Chad.png"))
        else:
            await ctx.send(file=discord.File(img))

@Bot.command()
async def submitsoy(ctx, *args, **kwargs):

    if(len(ctx.message.attachments) > 0):
        i = 0
        subCnt = 0
        while i < len(ctx.message.attachments):
            filename = ctx.message.attachments[i].filename
    
            if (ctx.message.attachments[i].content_type[0:5] == "image" and ctx.message.attachments[i].size < 8000001):
                await ctx.message.attachments[i].save(os.path.join(submission_folder, filename))
                # await ctx.send("Soyjak submitted!")
                subCnt += 1
            elif (ctx.message.attachments[i].content_type[0:5] != "image"):
                await ctx.send("File type not supported: " + ctx.message.attachments[i].content_type)
            elif (ctx.message.attachments[i].size >= 8000001):
                 await ctx.send("Error: File size greater than 8MB")
            else:
                 await ctx.send("Unknown error when submitting.")
            i += 1
        if subCnt > 0:
            await ctx.send(f"{subCnt} soyjaks submitted!")
    else:
        await ctx.send("No file attached.")

@Bot.command()
async def updatesoy(ctx, *args, **kwargs):
    if (ctx.author.name in soymins):
        image_names = []
        update_images()
        await ctx.send("'Jaks Updated!")
    else:
        await ctx.send("You do not have permission to use that command.")

@Bot.command()
async def approvesoys(ctx, *args, **kwargs):
    t = 0
    specFileError = []
    specFileResult = []
    msgContent = ""
    if(ctx.author.name in soymins):
        if len(args) == 0:
            for filename in os.listdir(submission_folder):
                shutil.move(os.path.join(submission_folder, filename), os.path.join(download_folder, filename))
                t += 1
            update_images()
            if t > 0:
                await ctx.send(f"All {t} 'jaks approved!")
            else:
                await ctx.send("There were no 'jaks awaiting approval.")
        elif len(args) > 0:
            for specfile in args:
                if specfile in os.listdir(submission_folder):
                    shutil.move(os.path.join(submission_folder, specfile), os.path.join(download_folder, specfile))
                    specFileResult.append(specfile)
                else: 
                    specFileError.append(specfile)
            if len(specFileResult) > 0:
                msgContent += f"Approved 'jaks: {" & ".join(specFileResult)}"
            else:
                msgContent += "No 'jaks approved."
            if len(specFileError) > 0:
                msgContent += f"{'\n'}'Jaks {'"' + " & ".join(specFileError) + '"'} were not found."
            await ctx.send(content=msgContent)
    else:
        await ctx.send("You do not have permission to use that command.")


@Bot.command()
async def reviewsoys(ctx, *args, **kwargs):
    soysToReview = []
    sentMsgs = 0
    if(ctx.author.name in soymins):
        if len(os.listdir(submission_folder)) > 0:
            for filename in os.listdir(submission_folder):
                if len(soysToReview) < 10:
                    soysToReview.append(discord.File(os.path.join(submission_folder, filename)))
                elif len(soysToReview) == 10:
                    await ctx.send(files=soysToReview)
                    soysToReview.clear()
                    sentMsgs += 1
                else:
                    await ctx.send("An Error occured.")
            if len(soysToReview) > 0:
                await ctx.send(files=soysToReview)
            await ctx.send(f"There are {len(soysToReview) + (sentMsgs * 10)} soyjaks awaiting review.")
        else:
            await ctx.send("There are no soyjaks awaiting review.")
        # await ctx.send(file=discord.File(os.path.join(submission_folder, filename)))

@Bot.command()
async def soycount(ctx, *args, **kwargs):
    cnt = 0
    for filename in os.listdir(download_folder):
        cnt += 1
    await ctx.send(f"We have {cnt} 'jaks!")

token = ""
with open("token.txt") as file:
    token = file.read()

Bot.run(token)