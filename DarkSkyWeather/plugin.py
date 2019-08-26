#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Copyright (c) 2018, Bruce Olivier
# All rights reserved.

import sys
import logging
from typing import List
from .utils.user import UserInfo
from supybot import utils, plugins, ircutils, callbacks
from supybot.commands import wrap, optional, getopts

try:
    from supybot.i18n import PluginInternationalization

    _ = PluginInternationalization("APIXUWeather")
except ImportError:
    # Placeholder that allows to run the plugin on a bot
    # without the i18n module
    def _(x):
        return x


logging.basicConfig(stream=sys.stdout, level=logging.INFO)
log = logging.getLogger(__name__)


class DarkSkyWeather(callbacks.Plugin):
    """A weather script that uses APIXU's api.
    """

    threaded = True

    def wz(self, irc, msg, args: List, text: str):
        """- Calls the weather"""
        userinfo = {"host": msg.host, "nick": msg.nick}
        userinfos = UserInfo(**userinfo)
        log.info(f"{type(msg)}")
        irc.reply(f"host is {msg}")

    wz = wrap(wz, [optional("text")])

    def setweather(self, irc, msg, args, units: int, text: str):
        """- Sets the weather for a user to the db."""

        userinfo = {
            "host": msg.host,
            "nick": msg.nick,
            "units": units,
            "location": text,
        }

        irc.reply(f"user: {msg.args[0]}")

    setweather = wrap(setweather, ["int", "text"])


Class = DarkSkyWeather
