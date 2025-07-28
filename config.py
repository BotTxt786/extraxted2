#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) ACE 

import os

class Config(object):
    # get a token from @BotFather
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
    API_ID = int(os.environ.get("API_ID", "21702672"))
    API_HASH = os.environ.get("API_HASH", "9ef8c573a89dc23477b8709741e6b520")
    AUTH_USERS = "-1002190083770"

