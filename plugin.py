#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Copyright (c) 2018, Bruce Olivier
# All rights reserved.

import os
import sqlite3
from sqlite3 import Error
from supybot import utils, plugins, ircutils, callbacks
from supybot.commands import wrap, optional, getopts
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

    def wz(self, irc, msg, args, text):
        """- Calls the weather"""
        irc.reply(f'args: {args}')

    wz = wrap(wz, [optional('text')])

    def setweather(self, irc, msg, args, units, text):
        """- Sets the weather for a user to the db."""

        userinfo = {
            'host': msg.host,
            'nick': msg.nick
        }

        irc.reply(f"user: {msg.args[0]}")

    setweather = wrap(setweather, ['int', 'text'])


class User:
    """
    A users info stored in the db.
    """

    def __init__(self, irc, userinfo):
        self.conn = self._connect()
        self.irc = irc
        if userinfo:
            for key, value in userinfo.items():
                setattr(self, key, value)

    def getinfo(self):
        pass

    def setinfo(self):
        pass

    def _connect(self):
        fullpath = os.path.dir(os.path.abspath(__file__))
        db = f'{fullpath}/data/apxiuweather.db'

        """
        Doing a check to see if there is a file or not.
        If not, create a database in exception.
        """
        try:
            with open(db) as f:
                pass

            print('Connecting to the SQLite3 database...')
            conn = sqlite3.connect(db)

            return conn

        except IOError as e:
            print(e)
            self.irc.reply('No database found. Creating a new database...')
            self._create_database()

        except Error as e:
            print(e)

    def _create_database(self):
        pass


Class = APIXUWeather

# vim:set shiftwidth=4 softtabstop=4 expandtab textwidth=79:
