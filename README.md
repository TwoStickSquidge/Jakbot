# 'Jak Bot
A Discord bot that sends Soyjaks

<img src="https://github.com/user-attachments/assets/f98e399f-8922-45ce-ad70-c259d8fe6ef5" width=500>

## Commands
### General Commands (Accessible by every user)
* !soy            - Sends a randomly selected soyjak from the downloads folder.
* !submitsoy      - Allows users to send a soyjak (or up to 10 in a single message) to the forReview folder for an admin to manually approve it.
* !help           - Displays a list of commands.
* !soycount       - Sends a message saying how many soyjaks are in the downloads folder.

### Admin Commmands (Only accessible by users whose usernames appear in soymins.txt)
* !updatesoy      - Makes sure that Jak Bot is pulling from the most recently updated downloads folder.
* !reviewsoys     - Sends all of the images in the forReview folder.
* !approvesoys    - Approves the images in the forReview folder, moving them to the downloads folder so that they can be sent with the !soy command. By default approves all of the images, adding the file names separated by spaces in the paramaters will approve only those specific files.

## Requirements
To run your own instance of 'Jak Bot you need a token.txt file containing your Discord API token, as well as a soymins.txt file containing the usernames of whoever you want to be able to approve soys on your own instance of the bot.

