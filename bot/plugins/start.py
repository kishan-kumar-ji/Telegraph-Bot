from swibots import BotContext, CommandEvent, MessageEvent
from swibots import InlineMarkup, InlineKeyboardButton, Message
import os

from .. import app,LOGGER
from ..database import add_user
from ..helper import START_MSG, HELP_MSG, OUTPUT_MSG
from .telegraph import upload

@app.on_command("start")
async def start(ctx: BotContext[CommandEvent]):
    message = ctx.event.message
    user = message.user
    await add_user(user.id, user.name)
    
    await message.reply_text(START_MSG.format(user.username))


@app.on_command("help")
async def help(ctx: BotContext[CommandEvent]):
    message = ctx.event.message
    user = message.user
    await add_user(user.id, user.name)
    await message.reply_text(HELP_MSG)


@app.on_message()
async def getme(ctx: BotContext[MessageEvent]):
    message = ctx.event.message
    user = message.user
    await add_user(user.id, user.name)

    if not (message.is_media or message.document):
        return
    type = message.media_info.media_type
    if type not in [1,2,7]:
        return
    
    msg = await message.reply_text("Proccessing...🔃")
    file_path = await message.download()
    try:
        file = await upload(file_path)

        markup = InlineMarkup(
            [
                [
                    InlineKeyboardButton("Telegraph",url=file[0]),
                    InlineKeyboardButton("Graph", url=file[1])
                ]
            ]
        )
        await msg.edit_text(OUTPUT_MSG.format(file[0],file[1]),inline_markup=markup)
    except Exception as e:
        await msg.edit_text("<b>Couldn't Process</b>\n\nCheck whether your file is corrupted\n\nif this couldn't solve contact developer")
        LOGGER.warn(f"Error while Uploading: {e}")
    finally:
        os.remove(file_path)
        LOGGER.info(f"Deleted: {file_path}")
