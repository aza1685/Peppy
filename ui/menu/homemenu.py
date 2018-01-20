# Copyright 2016-2018 Peppy Player peppy.player@gmail.com
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

from ui.factory import Factory
from ui.menu.menu import Menu
from util.keys import CURRENT, MODE, ORDER_HOME_MENU, NAME, KEY_RADIO, KEY_AUDIO_FILES
from util.util import HOME_ITEMS, IMAGE_RADIO, IMAGE_AUDIOBOOKS, IMAGE_STREAM
from util.config import USAGE, USE_VOICE_ASSISTANT

class HomeMenu(Menu):
    """ Home Menu class. Extends base Menu class """
    
    def __init__(self, util, bgr=None, bounding_box=None):
        """ Initializer
        
        :param util: utility object
        :param bgr: menu background
        :param bounding_box: bounding box
        """   
        self.factory = Factory(util)
        self.config = util.config
        m = self.factory.create_home_menu_button
        Menu.__init__(self, util, bgr, bounding_box, 2, 2, create_item_method=m)
        
        if not self.config[CURRENT][MODE]:
            mode = KEY_RADIO
        else:
            mode = self.config[CURRENT][MODE]
        self.modes = util.load_menu(HOME_ITEMS, NAME)
        
        if self.config[USAGE][USE_VOICE_ASSISTANT]:
            r = [util.voice_commands["VA_RADIO"].strip(), util.voice_commands["VA_GO_RADIO"].strip()]
            f = [util.voice_commands["VA_FILES"].strip(), util.voice_commands["VA_GO_FILES"].strip(), util.voice_commands["VA_AUDIO_FILES"].strip()]
            a = [util.voice_commands["VA_AUDIOBOOKS"].strip(), util.voice_commands["VA_BOOKS"].strip(), util.voice_commands["VA_GO_BOOKS"].strip()]
            s = [util.voice_commands["VA_STREAM"].strip(), util.voice_commands["VA_GO_STREAM"].strip()]
            
            self.modes[IMAGE_RADIO].voice_commands = r
            self.modes[KEY_AUDIO_FILES].voice_commands = f
            self.modes[IMAGE_AUDIOBOOKS].voice_commands = a
            self.modes[IMAGE_STREAM].voice_commands = s
        
        self.set_items(self.modes, 0, self.change_mode, False, self.config[ORDER_HOME_MENU])
        self.current_mode = self.modes[mode.lower()]
        self.item_selected(self.current_mode) 
    
    def change_mode(self, state):
        """ Change mode event listener
        
        :param state: button state
        """
        if not self.visible:
            return
        state.previous_mode = self.current_mode.name
        self.current_mode = state
        self.config[CURRENT][MODE] = state.name
        self.notify_listeners(state)
