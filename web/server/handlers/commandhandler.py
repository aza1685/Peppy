# Copyright 2019-2020 Peppy Player peppy.player@gmail.com
# 
# This file is part of Peppy Player.
# 
# Peppy Player is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# Peppy Player is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with Peppy Player. If not, see <http://www.gnu.org/licenses/>.

import os
import json

from util.config import SCREEN_INFO
from tornado.web import RequestHandler
from configparser import ConfigParser

class CommandHandler(RequestHandler):
    def initialize(self, peppy):
        self.peppy = peppy
        self.commands = {
            "reboot": self.peppy.reboot,
            "shutdown": self.peppy.shutdown
        }

    def get(self, command):
        if command == "ping":
            d = json.dumps("success")
            self.write(d)
            return

    def post(self, command):
        try:
            self.commands[command]()
        except:
            pass
