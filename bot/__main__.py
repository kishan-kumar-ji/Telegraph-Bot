from . import app, OWNER_ID

async def main():
        await app.start()
        await app.send_message("Wooho! Bot Started😍",user_id=OWNER_ID)
        await app.idle()
        await app.stop()

if __name__ == "__main__":
    app._loop.run_until_complete(main())