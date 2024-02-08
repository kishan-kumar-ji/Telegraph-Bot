# Telegraph Bot

The **Telegraph Bot** allows users to upload media (photos, videos, etc.) to telegra.ph. It's a switch bot built using Python.

## Features

- Upload media files to telegra.ph.
- Share content easily with others.
- Simple and user-friendly interface.

## Deployment Options

1. **Local Machine Deployment**:
    - Clone this repository to your local machine.
    - Install the required dependencies using

        ```
        pip3 install -r requirements.txt
        ```
    - Run your bot using `python -m bot`.

## Configuration (config.env)

- `BOT_TOKEN` - bot token from switch
- `BOT_USERNAME` = username of the bot
- `OWNER_ID` = id of owner `int`
- `DATABASE_URL` = connection url from MongoDB
- `DATABASE_NAME` = database name from MongoDB, Default: Cluster0

Rename `sample_config.env` to `config.env`