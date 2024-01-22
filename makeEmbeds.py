import discord
from discordbot_utils import *
import datetime

#creating the embedded changelog message with the details posted by the user
def makeEmbeddedChangelog(change_what, change_where, change_why, change_note, authorAvatar, author):
    embed = discord.Embed(
            title='Changelog',
            description='_ _',
            color=discord.Color.blue()
    )
    embed.add_field(name='What changed', value=change_what, inline=False)
    embed.add_field(name='Where', value=change_where, inline=False)
    embed.add_field(name='Why', value=change_why, inline=False)

    if change_note != '':
        embed.add_field(name='Note', value=change_note, inline=False)

    embed.set_footer(text=author, icon_url=authorAvatar)
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/1113256006512807997/1115279669315510373/image.png")

    return embed

#creating the embedded Archive DM based on the user's orginal message
def makeEmbeddedArchiveDM(messageByUser, guildID, channelID, messageID):
    messageLink = "https://discord.com/channels/" + guildID + "/" + channelID + "/" + messageID
    archive_embed = discord.Embed(
        title='Archive',
        description='',
        color=discord.Color.blue()
    )
    archive_embed.add_field(name='*You posted the following change in <#1115217957660917800> successfully: \n_ _*', value="```" + messageByUser + "```", inline=False)
    archive_embed.add_field(name='_ _', value='*If you made a mistake while posting, please delete ' + messageLink + ' and put your template in <#1115217957660917800> again.*')
    archive_embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/1115018548859895991/1115352400195240008/medieval_book.png")
    archive_embed.set_footer(text='Bot created by \nniclas01', icon_url='https://cdn.discordapp.com/attachments/1113256006512807997/1115279535898890290/COGGERS.gif')
    return archive_embed

def makeEmbeddedPlayerLeft(member_id, member_profile_picture, member_name):
    embed = discord.Embed(
            title="A user left the server:",
            description="",
            color=discord.Color.red()
    )
    embed.add_field(name="User", value=member_name, inline=True)
    embed.add_field(name="User ID", value="" + str(member_id), inline=True)
    embed.set_thumbnail(url=member_profile_picture)
    return embed

def makeEmbeddedPlayerBanned(member_id, member_profile_picture, member_name, bannedBy, reason):
    embed = discord.Embed(
            title="A user has been banned:",
            description="",
            color=discord.Color.red()
    )
    embed.add_field(name="User", value=member_name, inline=True)
    embed.add_field(name="User ID", value="" + str(member_id), inline=True)
    embed.add_field(name="Banned by:", value="<@" + str(bannedBy) + ">", inline=True)
    embed.add_field(name="Reason", value=reason, inline=False)
    embed.set_thumbnail(url=member_profile_picture)
    return embed

def makeEmbeddedPlayerKicked(member_id, member_profile_picture, member_name, kickedBy, reason):
    embed = discord.Embed(
            title="A user has been kicked:",
            description="",
            color=discord.Color.red()
    )
    embed.add_field(name="User:", value=member_name, inline=True)
    embed.add_field(name="User ID", value="" + str(member_id), inline=True)
    embed.add_field(name="Kicked by", value="<@" + str(kickedBy) + ">", inline=True)
    embed.add_field(name="Reason", value=reason, inline=False)
    embed.set_thumbnail(url=member_profile_picture)
    return embed

def makeEmbeddedPlayerTimeout(member_id, member_profile_picture, member_name, timedoutBy, reason, unix_timedoutUntil):
    embed = discord.Embed(
            title="A user has been timed-out:",
            description="",
            color=discord.Color.red()
    )
    embed.add_field(name="User", value=member_name, inline=True)
    embed.add_field(name="User ID", value="" + str(member_id), inline=True)
    embed.add_field(name="Timed-out by", value="<@" + str(timedoutBy) + ">", inline=True)
    embed.add_field(name="Timed-out until", value=unix_timedoutUntil, inline=False)
    embed.add_field(name="Reason", value=reason, inline=False)
    embed.set_thumbnail(url=member_profile_picture)
    return embed


def makeEmbeddedDeletedMessage(useravatar, username, userid, deleter, content, hasImages, channel):
    embed = discord.Embed(
            title="Message deleted:",
            description="",
            color=discord.Color.green()
    )



    embed.add_field(name="User", value=username, inline=True)
    embed.add_field(name="User ID", value=str(userid), inline=True)
    embed.add_field(name="Original Message", value=content, inline=False)
    embed.add_field(name="Channel", value="<#" + str(channel) + ">", inline=False)
    embed.add_field(name="Deleted by", value=deleter, inline=False)
    if hasImages == True:
        embed.add_field(name="Images:", value="True, but cannot access picture due to Discord's API limitations.", inline=False)
    embed.set_thumbnail(url=useravatar)
    return embed


#creating the preview message
def makeEmbeddedEventPreview(event_name, event_description, event_time, event_max_participants, picture, event_id, authorAvatar, author):
    embed = discord.Embed(
            title="Preview: " + event_name,
            description=event_description,
            color=discord.Color.orange()
    )
    embed.add_field(name='When does the Event start?', value=event_time, inline=False)
    embed.add_field(name='How many players can participate?', value=event_max_participants, inline=False)
    embed.add_field(name='Player signups:', value="", inline=False)
    embed.add_field(name='_ _', value="_ _", inline=False)
    embed.add_field(name='_ _', value="Please confirm that your message is correct and can be published: ✅", inline=False)
    embed.add_field(name='_ _', value="Event-ID: " + str(event_id), inline=False)
    if picture != '':
        embed.set_thumbnail(url=picture)
    else:
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/1105866058151247894/1113984822226976900/Chapel_of_the_9.png")

    embed.set_footer(text=author, icon_url=authorAvatar)

    return embed

def makeEmbeddedEventPublic(newEventChannelID, event_name, event_description, event_time, event_max_participants, picture, event_id, authorAvatar, author):
    embed = discord.Embed(
            title=event_name,
            description=event_description,
            color=discord.Color.green()
    )
    embed.add_field(name='_ _', value="_ _", inline=False)
    embed.add_field(name='When does the Event start?', value=event_time, inline=False)
    embed.add_field(name='How many players can participate?', value=event_max_participants, inline=False)
    embed.add_field(name='Player signups:', value="", inline=False)
    embed.add_field(name='_ _', value="_ _", inline=False)
    embed.add_field(name='_ _', value="If you want to signup, please press: 📝\nIf you want to signout press: ❌", inline=False)
    embed.add_field(name='_ _', value="Event-Channel: " + "<#" + str(newEventChannelID) + ">" + "\n*(only visible if you signed up)*", inline=False)
    embed.add_field(name='_ _', value="Event-ID: " + str(event_id), inline=False)
    if picture != '':
        embed.set_thumbnail(url=picture)
    else:
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/1105866058151247894/1113984822226976900/Chapel_of_the_9.png")

    embed.set_footer(text=author, icon_url=authorAvatar)

    return embed

def editEmbeddedEventPublic(newEventChannelID, event_name, event_description, event_time, event_max_participants, player0, picture, event_id, authorAvatar, author):
    embed = discord.Embed(
            title=event_name,
            description=event_description,
            color=discord.Color.green()
    )
    embed.add_field(name='_ _', value="_ _", inline=False)
    embed.add_field(name='When does the Event start?', value=event_time, inline=False)
    embed.add_field(name='How many players can participate?', value=event_max_participants, inline=False)
    embed.add_field(name='Player signups:', value=player0, inline=False)
    embed.add_field(name='_ _', value="_ _", inline=False)
    embed.add_field(name='_ _', value="If you want to signup, please press: 📝\nIf you want to signout press: ❌", inline=False)
    embed.add_field(name='_ _', value="Event-Channel: " + "<#" + str(newEventChannelID) + ">" + "\n*(only visible if you signed up)*", inline=False)
    embed.add_field(name='_ _', value="Event-ID: " + str(event_id), inline=False)
    if picture != '':
        embed.set_thumbnail(url=picture)
    else:
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/1105866058151247894/1113984822226976900/Chapel_of_the_9.png")

    embed.set_footer(text=author, icon_url=authorAvatar)
    
    return embed

def makeEmbeddedEventCreatedDM(messageByUser, guildID, eventChannelID, eventMessageID, eventTextChannelID):
    eventMessageLink = "https://discord.com/channels/" + str(guildID) + "/" + str(eventChannelID) + "/" + str(eventMessageID)
    eventTextChannelLink = "https://discord.com/channels/" + str(guildID) + "/" + str(eventTextChannelID)
    eventCreated_embed = discord.Embed(
        title='Event-Management',
        description='',
        color=discord.Color.blue()
    )
    eventCreated_embed.add_field(name='Your Event has been created', value="Don't forget to sign yourself up.", inline=False)
    eventCreated_embed.add_field(name='Your Event:', value=eventMessageLink, inline=True)
    eventCreated_embed.add_field(name='Your Event-Channel:', value=eventTextChannelLink, inline=True)
    eventCreated_embed.add_field(name='_ _', value='*If you made a mistake while posting, please delete ' + eventMessageLink + ' and repost your template.', inline=False)
    eventCreated_embed.add_field(name='*This was your template:*', value="```" + messageByUser + "```", inline=False)
    eventCreated_embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/1115018548859895991/1115352400195240008/medieval_book.png")
    eventCreated_embed.set_footer(text='Bot created by \nniclas01', icon_url='https://cdn.discordapp.com/emojis/1115655349966479440.gif?size=96&quality=lossless')
    return eventCreated_embed

def makeEmbeddedEventJoinedDM(guildID, eventChannelID, eventMessageID, eventTextChannelID):
    eventMessageLink = "https://discord.com/channels/" + str(guildID) + "/" + str(eventChannelID) + "/" + str(eventMessageID)
    eventTextChannelLink = "https://discord.com/channels/" + str(guildID) + "/" + str(eventTextChannelID)
    eventCreated_embed = discord.Embed(
        title='Event-Management',
        description='',
        color=discord.Color.blue()
    )
    eventCreated_embed.add_field(name='You joined an Event', value="_ _", inline=False)
    eventCreated_embed.add_field(name='You joined:', value=eventMessageLink, inline=True)
    eventCreated_embed.add_field(name='Your Event-Channel:', value=eventTextChannelLink, inline=True)
    eventCreated_embed.add_field(name='_ _', value='*If you want to sign out, react with ❌ to* ' + eventMessageLink, inline=False)
    eventCreated_embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/1115018548859895991/1115352400195240008/medieval_book.png")
    eventCreated_embed.set_footer(text='Bot created by \nniclas01', icon_url='https://cdn.discordapp.com/emojis/1115655349966479440.gif?size=96&quality=lossless')
    return eventCreated_embed

def makeEmbeddedEventLeftDM(guildID, eventChannelID, eventMessageID):
    eventMessageLink = "https://discord.com/channels/" + str(guildID) + "/" + str(eventChannelID) + "/" + str(eventMessageID)
    eventCreated_embed = discord.Embed(
        title='Event-Management',
        description='',
        color=discord.Color.blue()
    )
    eventCreated_embed.add_field(name='You left an Event', value="_ _", inline=False)
    eventCreated_embed.add_field(name='You left::', value=eventMessageLink, inline=True)
    eventCreated_embed.add_field(name='Event-Channel:', value="Your access to the event-channel has been removed.", inline=True)
    eventCreated_embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/1115018548859895991/1115352400195240008/medieval_book.png")
    eventCreated_embed.set_footer(text='Bot created by \nniclas01', icon_url='https://cdn.discordapp.com/emojis/1115655349966479440.gif?size=96&quality=lossless')
    return eventCreated_embed

def makeEmbeddedEventFullDM():
    eventFull_embed = discord.Embed(
        title='Event-Management',
        description='',
        color=discord.Color.blue()
    )
    eventFull_embed.add_field(name='Event is full.', value="_ _", inline=False)
    eventFull_embed.add_field(name='', value="Sorry, but the event you tried to join is currently full.\nPlease wait for the next one or wait for open slots.\n\n Alternatively, you could suggest a new event in <#1105681410880188477>.", inline=False)
    eventFull_embed.add_field(name='Need help?', value="If you're having any issues please contact the Justicars/Moderators", inline=False)
    eventFull_embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/1115018548859895991/1115352400195240008/medieval_book.png")
    eventFull_embed.set_footer(text='Bot created by \nniclas01', icon_url='https://cdn.discordapp.com/emojis/1115655349966479440.gif?size=96&quality=lossless')
    return eventFull_embed

def makeEmbeddedWarnings(data):
    embed = discord.Embed(
            title='Warning-Management',
            description='_ _',
            color=discord.Color.red()
    )
    embed.add_field(name='User:', value="<@" + str(data["user_id"]) + ">", inline=True)
    embed.add_field(name='Warnings', value=len(data["warnings"]), inline=True)
    embed.add_field(name='_ _', value='_ _', inline=False)
    if len(data["warnings"]) != 0:
        embed.add_field(name='All Warnings', value="", inline=False)
        for i in range(len(data["warnings"])):
            embed.add_field(name='#' + str(i+1), value="", inline=False)
            embed.add_field(name='Reason:', value=data["warnings"][i]["1"], inline=True)
            embed.add_field(name='made by:', value="<@" + str(data["warnings"][i]["by"] + ">"), inline=True)
            if data["warnings"][i]["proof"] != "":
                embed.add_field(name='Proof:', value="" + str(data["warnings"][i]["proof"]), inline=False)
    else: 
        embed.add_field(name='All Warnings', value="User has no warnings! <3", inline=False)

    embed.set_footer(text='Bot created by \nniclas01', icon_url='https://cdn.discordapp.com/emojis/1115655349966479440.gif?size=96&quality=lossless')
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/1115018548859895991/1118990507054465186/Screenshot_1.png")

    return embed

def makeEmbeddedTimeOutDM(reason):
    embed = discord.Embed(
            title='',
            description='',
            color=discord.Color.red()
    )
    embed.add_field(name='You received a timeout!', value="", inline=False)
    embed.add_field(name='Reason:', value="" + str(reason), inline=False)
    embed.add_field(name='_ _', value="*Please contact a moderator if you think this was a mistake.*", inline=False)

    embed.set_footer(text='Bot created by \nniclas01', icon_url='https://cdn.discordapp.com/emojis/1115655349966479440.gif?size=96&quality=lossless')
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/1115018548859895991/1118990507054465186/Screenshot_1.png")

    return embed

def makeEmbeddedAddedWarningDM(newWarning):
    embed = discord.Embed(
            title='Warning-Management',
            description='_ _',
            color=discord.Color.red()
    )
    embed.add_field(name='You received a new warning!', value="", inline=False)
    embed.add_field(name='Reason:', value="" + str(newWarning[1]), inline=False)
    if newWarning["proof"] != "":
        embed.add_field(name='Proof:', value="" + str(newWarning["proof"]), inline=False)
    #embed.add_field(name='made by:', value="<@" + str(newWarning["by"] + ">"), inline=False)
    embed.add_field(name='_ _', value="*Please contact a moderator if you think this was a mistake.*", inline=False)

    embed.set_footer(text='Bot created by \nniclas01', icon_url='https://cdn.discordapp.com/emojis/1115655349966479440.gif?size=96&quality=lossless')
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/1115018548859895991/1118990507054465186/Screenshot_1.png")

    return embed

def makeEmbeddedRemovedWarningDM(removedWarning, removedBy):
    embed = discord.Embed(
            title='Warnings',
            description='_ _',
            color=discord.Color.red()
    )
    embed.add_field(name='A warning has been removed!', value="", inline=False)
    embed.add_field(name='Old Reason:', value="" + str(removedWarning["1"]), inline=False)
    embed.add_field(name='removed by:', value="<@" + str(removedBy) + ">", inline=False)
    embed.add_field(name='_ _', value="", inline=False)
    embed.add_field(name='_ _', value="*Please contact a moderator if you have questions.*", inline=False)

    embed.set_footer(text='Bot created by \nniclas01', icon_url='https://cdn.discordapp.com/emojis/1115655349966479440.gif?size=96&quality=lossless')
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/1115018548859895991/1118990507054465186/Screenshot_1.png")

    return embed

def makeEmbeddedInvitedBy(inviter, joiner):
    embed = discord.Embed(
            title='',
            description='',
            color=discord.Color.yellow()
    )
    embed.add_field(name='A user joined the server:', value="", inline=False)
    embed.add_field(name='Invited user', value="" + str(joiner.name) + " " + str(joiner.id), inline=False)
    embed.add_field(name='Invited by', value="" + str(inviter.name) + " " + str(inviter.id), inline=False)
    embed.add_field(name='_ _', value="", inline=False)
    embed.set_footer(text='Bot created by \nniclas01', icon_url='https://cdn.discordapp.com/emojis/1115655349966479440.gif?size=96&quality=lossless')

def makeEmbeddedCourtFiling(court_data):
    embed = discord.Embed(
            title='New Court Filings',
            description='_ _',
            color=discord.Color.blue()
    )
    if court_data["payload"]["results"][0]["description"] == None or court_data["payload"]["results"][0]["description"] == "":
        embed.add_field(name='Description:', value="Not given", inline=False)
    else:
        embed.add_field(name='Description:', value=court_data["payload"]["results"][0]["description"], inline=False)
    embed.add_field(name='The following filings are new:', value="", inline=False)
    for i in range(len(court_data["payload"]["results"])):
        embed.add_field(name="Filing " + str(i+1), value=court_data["payload"]["results"][i]["recap_documents"][0]["description"], inline=False)
        if court_data["payload"]["results"][i]["recap_documents"][0]["absolute_url"] == None or court_data["payload"]["results"][i]["recap_documents"][0]["absolute_url"] == "":
            embed.add_field(name='', value="[Courtlistener-Link](https://www.courtlistener.com/docket/67193019/nexon-korea-corporation-v-ironmace-co-ltd/)", inline=True)
        else:
            embed.add_field(name='', value="[Courtlistener-Link](https://www.courtlistener.com" + str(court_data["payload"]["results"][i]["recap_documents"][0]["absolute_url"]) + ")", inline=True)
    
    embed.add_field(name='_ _', value="", inline=False)
    embed.add_field(name='_ _', value="*Please contact a moderator if you have questions.*", inline=False)

    embed.set_footer(text='Bot created by \nniclas01', icon_url='https://cdn.discordapp.com/emojis/1115655349966479440.gif?size=96&quality=lossless')
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/1115018548859895991/1118990507054465186/Screenshot_1.png")

    return embed

def makeEmbeddedCheckrolesMessage(matching_entries, user_id, desired_roles):
    embed = discord.Embed(
            title='Role-Management',
            description='_ _',
            color=discord.Color.green()
    )
    embed.add_field(name='Role(s) for user:', value="<@" + str(user_id) + ">", inline=False)
    for entry in matching_entries:
        role_added_at = datestrToDateUnix(entry.created_at.strftime('%Y-%m-%d %H:%M:%S'))
        role_name = next(role.name for role in entry.after.roles if role.name in desired_roles)
        responsible_user = entry.user
        embed.add_field(name='Role:', value="" + role_name, inline=True)
        embed.add_field(name='given at:', value=role_added_at, inline=True)
        embed.add_field(name='given by:', value="<@" + str(responsible_user.id) + ">", inline=True)

    embed.add_field(name='_ _', value="", inline=False)
    embed.add_field(name='_ _', value="*Please contact a moderator if you have questions.*", inline=False)

    embed.set_footer(text='Bot created by \nniclas01', icon_url='https://cdn.discordapp.com/emojis/1115655349966479440.gif?size=96&quality=lossless')
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/1115018548859895991/1120122424390844440/peepoTankard.png")

    return embed

def makeEmbeddedTemplarDM():
    embed = discord.Embed(
            title='Role-Management',
            description='_ _',
            color=discord.Color.green()
    )
    embed.add_field(name="*Your dedication to the **Order of the 9th** did not go unseen. Thanks for being part of us.*", value="_ _", inline=False)
    embed.add_field(name='You received the following role:', value="Templar", inline=False)
    embed.add_field(name='New Permissions:', value="⦁ Create Events in https://discord.com/channels/1104622211068854363/1117510275516600491\n⦁ Create Discord-Invites", inline=False)
    embed.add_field(name='role given at:', value=datestrToDateUnix(str(datetime.datetime.utcnow())), inline=True)
    embed.add_field(name='_ _', value="", inline=False)
    embed.add_field(name='_ _', value="*Please contact a moderator if you have questions.*", inline=False)

    embed.set_footer(text='Bot created by \nniclas01', icon_url='https://cdn.discordapp.com/emojis/1115655349966479440.gif?size=96&quality=lossless')
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/1115018548859895991/1120122424390844440/peepoTankard.png")

    return embed

def makeEmbeddedDefenderDM():
    embed = discord.Embed(
            title='Role-Management',
            description='_ _',
            color=discord.Color.green()
    )
    embed.add_field(name='You received the following role:', value="Defender", inline=False)
    embed.add_field(name='New Permissions:', value="⦁ Access to new channels:\n #defenderchat https://discord.com/channels/1104622211068854363/1120944443076382902 \n#moderation https://discord.com/channels/1104622211068854363/1113252410765357076 \n#warnings https://discord.com/channels/1104622211068854363/1119244292335079588 \n⦁ bot-commands:\n in #warnings\n ``!getwarnings user_id``\n``!addwarning user_id reason``\n in #moderation:\n``!checkroles user_id``\n⦁Timeout other users", inline=False)
    embed.add_field(name='role given at:', value=datestrToDateUnix(str(datetime.datetime.utcnow())), inline=True)
    embed.add_field(name='_ _', value="", inline=False)
    embed.add_field(name='_ _', value="*Please contact a moderator if you have questions.*", inline=False)

    embed.set_footer(text='Bot created by \nniclas01', icon_url='https://cdn.discordapp.com/emojis/1115655349966479440.gif?size=96&quality=lossless')
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/1115018548859895991/1120122424390844440/peepoTankard.png")

    return embed

def makeEmbeddedCheckperms(data):
    embed = discord.Embed(
            title='Permission-Management',
            description='_ _',
            color=discord.Color.green()
    )
    embed.add_field(name='Role:', value=data["role_name"], inline=False)
    embed.add_field(name='Permissions:', value="⦁ addwarning = " + str(data["perms"][0]["addwarning"]) + "\n⦁ removewarning = " + str(data["perms"][0]["removewarning"]) + "\n⦁ checkwarning = " + str(data["perms"][0]["checkwarning"]) + "\n⦁ checkpermissions = " + str(data["perms"][0]["checkperms"]) + "\n⦁ changeperms = " + str(data["perms"][0]["changeperms"]), inline=False)
    embed.add_field(name='_ _', value="", inline=False)
    embed.add_field(name='_ _', value="*Please contact a moderator if you have questions.*", inline=False)

    embed.set_footer(text='Bot created by \nniclas01', icon_url='https://cdn.discordapp.com/emojis/1115655349966479440.gif?size=96&quality=lossless')
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/1115018548859895991/1120122424390844440/peepoTankard.png")

    return embed

def makeEmbeddedGraysunPing():
    embed = discord.Embed(
            title='Warning-Management',
            description='_ _',
            color=discord.Color.red()
    )
    embed.add_field(name='You broke a rule [9]', value="*Recognize that this is a place of rest and solitude. Do not ping, bother, or disturb Lord Graysun, or any of the Wardens, Senior Wardens, or Tavern Masters here, as this space is meant for tranquility and solace.*", inline=False)
    embed.add_field(name='Reason:', value="Pinging Graysun", inline=False)
    embed.add_field(name='Actions taken:', value="Timeout for 1h and added a warning", inline=False)
    embed.add_field(name="_ _", value="If you break this rule again, you will be removed from our Order.", inline=False)
    embed.add_field(name='_ _', value="*Please contact a moderator if you think this was a mistake.*", inline=False)

    embed.set_footer(text='Bot created by \nniclas01', icon_url='https://cdn.discordapp.com/emojis/1115655349966479440.gif?size=96&quality=lossless')
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/1115018548859895991/1118990507054465186/Screenshot_1.png")

    return embed