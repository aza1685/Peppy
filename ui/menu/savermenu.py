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

from ui.menu.menu import Menu
from ui.factory import Factory
from util.keys import CURRENT, KEY_SCREENSAVER, ORDER_SCREENSAVER_MENU, GENRE, NAME
from util.util import SCREENSAVER_ITEMS, CLOCK, LOGO, SLIDESHOW, VUMETER
from util.config import USAGE, USE_VOICE_ASSISTANT

class SaverMenu(Menu):
    """ Screensaver Menu class. Extends base Menu class """
    
    def __init__(self, util, bgr=None, bounding_box=None):
        """ Initializer
        
        :param util: utility object
        :param bgr: menu background
        :param bounding_box: bounding box
        """
        self.factory = Factory(util)
        m = self.factory.create_saver_menu_button
        Menu.__init__(self, util, bgr, bounding_box, 1, 4, create_item_method=m)
        self.config = util.config
        current_saver_name = self.config[KEY_SCREENSAVER][NAME]
        self.savers = util.load_menu(SCREENSAVER_ITEMS, GENRE)
        
        if self.config[USAGE][USE_VOICE_ASSISTANT]:
            self.savers[CLOCK].voice_commands = [util.voice_commands["VA_CLOCK"].strip()]
            self.savers[LOGO].voice_commands = [util.voice_commands["VA_LOGO"].strip()]
            self.savers[SLIDESHOW].voice_commands = [util.voice_commands["VA_SLIDESHOW"].strip()]
            self.savers[VUMETER].voice_commands = [util.voice_commands["VA_INDICATOR"].strip()]
        
        self.set_items(self.savers, 0, self.change_saver, False, self.config[ORDER_SCREENSAVER_MENU])
        self.current_saver = self.savers[current_saver_name]
        self.item_selected(self.current_saver)
        
    def get_saver_by_index(self, index):
        """ Return screensaver specified by its index
        
        :param index: screensaver index in the map of screensavers
        
        :return: screensaver
        """
        return self.savers[index]

    def change_saver(self, state):
        """ Change screensaver event listener
        
        :param state: button state
        """
        if not self.visible:
            return
        
        self.config[KEY_SCREENSAVER][NAME] = state.name        
        self.notify_listeners(state)
        