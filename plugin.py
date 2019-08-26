#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Copyright (c) 2018, Bruce Olivier
# All rights reserved.

import sys
import logging
from utils import UserData
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


class DarkSkyWeather(callbacks.Plugin):
    """A weather script that uses APIXU's api.
    """

    threaded = True

    def wz(self, irc, msg, args, text: str):
        """- Calls the weather"""

        userinfo = {"host": msg.host, "nick": msg.nick}

        irc.reply(f"irc type: {type(irc)}")

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
