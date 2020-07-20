# justwiped
This discord bot will notify you every time a new Rust server has wiped from the website "just-wiped.net", with or without filters (cf. code comments)

If you want to run the bot yourself, you will have to modify the channel ID (you can know this by activating the Discord Developer mode (Options > Appearence) and right clicking on a channel to get its ID.

You will also need to create a bot on the Discord Developer website (https://discord.com/developers/applications) and add its token at the bottom of the code.

I made this bot to be able to know when the servers wiped according to my needs (for example duos, trios, 20+ players only, bp wiped or not, etc...). You can simply filter the server on the website, copy the link and paste it in the "url=..." area in the code.

I guess that's it. Just run it on a server so it will work indefinitly and notify you every time a server is available.

Current status :

- Working fine
- I will work on the "BP WIPE" text showing at the end of a BP wiped server, maybe hiding it or showing it on another line

- ~~The date & time are not very readable, I will try to edit them or just remove them as it's quite useless in my opinion~~
- The date and time is not that bad of an idea as the refresh time can vary from the filters that you want the bot to look for. Actually, the only time zone is UTC+2 (CET/CEST). I will try to see how I can include all of the timezones to match anyone's location.

- I will try to make the bot running for everyone, and be able to edit the channel from the bot itself (via commands) as well as a custom just-wiped link for custom filters according to other people, and to make sense I will share the link so people will be able to invite the bot to their servers and receive all of the informations. I'm not 100% sure how to do that as it probably needs a database to store every single channel ID, so maybe it will not work with channel IDs, but I don't know how yet.


# Remember, it's a WIP!!!

thanks
