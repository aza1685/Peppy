# Copyright 2016-2017 Peppy Player peppy.player@gmail.com
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

from ui.screen.screen import Screen, PERCENT_TOP_HEIGHT
from ui.menu.genremenu import GenreMenu
from util.util import KEY_GENRE
from ui.factory import Factory

class RadioGenreScreen(Screen):
    """ Radio Genre Screen. Extends base Screen class """
    
    def __init__(self, util, listeners):
        """ Initializer
        
        :param util: utility object
        :param listener: screen menu event listener
        """
        Screen.__init__(self, util, KEY_GENRE, PERCENT_TOP_HEIGHT)
        self.genre_menu = GenreMenu(util, (0, 0, 0), self.layout.CENTER)
        self.genre_menu.add_listener(listeners[KEY_GENRE])
        self.add_menu(self.genre_menu)
        
        factory = Factory(util)        
        factory.create_home_player_buttons(self, self.layout.BOTTOM, listeners)