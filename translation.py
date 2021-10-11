from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

class Translation(object):

    START_TEXT = """
Hey {}

I am Fastest Url Uploader Bot. 
Just send me the url to get started !

Made With 💕 By @Tellybots_4u
"""
    HELP_TEXT = """
<b>Link to Media or File</b>
- Send a link for upload to telegram file or media.

<b>Set Thumbnail</b>
- Send a photo to make it as permanent thumbnail.

<b>Deleting Thumbnail</b>
- Send /delthumb to deleting thumbnail.

<b>Show Thumbnail</b>
- Send /showthumb to view custom thumbnail.
"""
    ABOUT_TEXT = """
**🤖 Bot :** URL Uploader\n
**🧒 Creator :** [Vivek](https://telegram.me/vivektvp)\n
**📡 Channel :** [Vk Projects](https://telegram.me/VKPROJECTS)\n
**🎉 Credits :** Everyone in this journey\n
**⚗️ Language :** [Python3](https://python.org)\n
**📚 Library :** [Pyrogram v1.2.0](https://pyrogram.org)\n
**💫 Server :** [Heroku](https://heroku.com)\n
"""
    START_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('⛔ Help', callback_data='help'),
        InlineKeyboardButton('👲 About', callback_data='about'),
        ],[
        InlineKeyboardButton('Close🔐', callback_data='close')
        ]]
    )
    HELP_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('👲 About', callback_data='about'),
        InlineKeyboardButton('Close 🔐', callback_data='close')
        ]]
    )
    ABOUT_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('🏡 Home', callback_data='home'),
        InlineKeyboardButton('Close 🔐', callback_data='close')
        ]]
    )
    FORMAT_SELECTION = """<b>Select the desired format For Uploading:</b> <a href='{}'>file size might be approximate</a>
    
Send your custum thumbnail if required.
You can use /delthumb to delete the auto-generated thumbnail."""
    CHECKING_LINK = "<code>Analysing Your Link</code>⏳"
    BANNED_USER_TEXT = "<code>You are Banned!</code>"
    SET_CUSTOM_USERNAME_PASSWORD = """If you want to download premium videos, provide in the following format:
URL | newfilename | username | password"""
    DOWNLOAD_START = "<code>Downloading To My server Please Wait...</code>"    
    UPLOAD_START = "<code>Uploading into Telegram...</code>"
    AFTER_SUCCESSFUL_UPLOAD_MSG_WITH_TS = "Downloaded in {} seconds. \n\nUploaded in {} seconds."
    RCHD_TG_API_LIMIT = "Downloaded in {} seconds.\nDetected File Size: {}\nSorry. But, I cannot upload files greater than 1.95GB due to Telegram API limitations."
    CUSTOM_CAPTION_UL_FILE = "<b>Join :-</b> @Tellybots_4u"
    SLOW_URL_DECED = "Gosh that seems to be a very slow URL. Since you were screwing my home, I am in no mood to download this file. Meanwhile, why don't you try this:==> https://shrtz.me/PtsVnf6 and get me a fast URL so that I can upload to Telegram, without me slowing down for other users."
    NO_VOID_FORMAT_FOUND = "<code>{}</code>"
    REPORT_SITE_TEXT = "<code>Sorry not uploading in this site here because this site is reporting site.</code>"
    SOMETHING_WRONG = "<code>Something Wrong. Try again.</code>"
    FORCE_SUBSCRIBE_TEXT = "<code>Plz Join my Updates Channel to use me 🧒....</code>"
    FREE_USER_LIMIT_Q_SZE = "Sorry Friend, Free users can only 1 request per {} minutes. Please try again after {} seconds later."
