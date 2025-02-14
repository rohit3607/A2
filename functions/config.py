from decouple import config


class Var:
    # Version
    __version__ = "v0.0.8"

    # Telegram Credentials
    API_ID = config("API_ID", default=22469064, cast=int)
    API_HASH = config("API_HASH", default="c05481978a217fdb11fa6774b15cba32")
    BOT_TOKEN = config("BOT_TOKEN", default="7542241757:AAFgeHI2tr518Hbh8DOvLIfeCpQj0udfk-Y")
    SESSION = config("SESSION", default=None)

    # Database Credentials
    MONGO_SRV = config(
        "MONGO_SRV",
        default="mongodb+srv://rohitplayer87089:rohit870@cluster0.4wt927p.mongodb.net/?retryWrites=true&w=majority"
    )

    # Channels Ids
    BACKUP_CHANNEL = config("BACKUP_CHANNEL", default=-1002370816678, cast=int)
    MAIN_CHANNEL = config("MAIN_CHANNEL", default=-1002370816678, cast=int)
    LOG_CHANNEL = config("LOG_CHANNEL", default=-1002370816678, cast=int)
    CLOUD_CHANNEL = config("CLOUD_CHANNEL", default=-1002370816678, cast=int)
    FORCESUB_CHANNEL = config("FORCESUB_CHANNEL", default=-1002370816678, cast=int)
    OWNER = config("OWNER", default=0, cast=int)

    # Other Configs
    THUMB = config(
        "THUMBNAIL",
        default="https://graph.org/file/ad1b25807b81cdf1dff65.jpg"
    )
    FFMPEG = config("FFMPEG", default="ffmpeg")
    CRF = config("CRF", default="27")
    SEND_SCHEDULE = config("SEND_SCHEDULE", default=True, cast=bool)
    RESTART_EVERDAY = config("RESTART_EVERDAY", default=True, cast=bool)
    LOG_ON_MAIN = config("LOG_ON_MAIN", default=False, cast=bool)
    FORCESUB_CHANNEL_LINK = config(
        "FORCESUB_CHANNEL_LINK",
        default="https://t.me/+tKRLKu4T6Kc4N2E1",
        cast=str
    )

    # Dev Configs
    DEV_MODE = config("DEV_MODE", default=False, cast=bool)