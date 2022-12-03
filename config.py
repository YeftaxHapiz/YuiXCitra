# Copyright (c) 2021 Itz-fork

import os

class Config(object):
    APP_ID = int(os.environ.get("APP_ID, "7938961"))
    API_HASH = os.environ.get("API_HASH", "7de246ac831880656921b5a7a3b74274")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5781258361:AAGEWikwZNVFdsJnEPqPbHktccrratn4enU")
    OWNER_ID = int(os.environ.get("OWNER_ID", "1362925817"))
    # Chat bot's name
    CHAT_BOT_NAME = os.environ.get("CHAT_BOT_NAME", "Citra")
    # Your OpenAI API key
    OPENAI_KEY = os.environ.get("OPENAI_KEY", "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")
    # Your ARQ API Key
    ARQ_API_URL = "http://arq.hamker.dev"
    ARQ_KEY = os.environ.get("ARQ_KEY", "DZPJFE-WMKRKR-YLYICM-CEZFRF-ARQ")
    # Default Chatbot engine you want to use after OpenAI
    DEFAULT_CHATBOT = os.environ.get("DEFAULT_CHATBOT", "affiliateplus")