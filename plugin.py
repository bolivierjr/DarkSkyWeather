#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Copyright (c) 2018, Bruce Olivier
# All rights reserved.

import sqlite3
from typing import Dict
from supybot import utils, plugins, ircutils, callbacks
from supybot.commands import wrap, optional
try:
    from supybot.i18n import PluginInternationalization
    _ = PluginInternationalization('APIXUWeather')
except ImportError:
    # Placeholder that allows to run the plugin on a bot
    # without the i18n module
    def _(x): return x


class APIXUWeather(callbacks.Plugin):
    """A weather script that uses APIXU's api.
    """
    threaded = True

    def wz(self, irc: irc, msg, args)->str:
        """- Calls the weather"""
        irc.reply(f'Hello, World')

    wz = wrap(wz)

    def setweather(self, irc, msg, args, text):
        """- Sets the weather for a user to db."""

        irc.reply(f'hi, {msg}')

    setweather = wrap(setweather, [optional('text')])


class User:
    """
    A users info stored in the db.
    """

    def __init__(self, userinfo=None):
        self.userinfo = userinfo
        self._connect()

    def _connect(self):
        pass


Class = APIXUWeather

# vim:set shiftwidth=4 softtabstop=4 expandtab textwidth=79:
