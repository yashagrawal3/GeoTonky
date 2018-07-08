#! /usr/bin/env python
# -*- coding: utf-8 -*-

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
import sugargame
import sugargame.canvas
import pygame
from sugar3.activity import activity


import Proyecto

class HelloWorldActivity(activity.Activity):

    def __init__(self, handle):
        activity.Activity.__init__(self, handle)

        # Change the following number to change max participants
        self.max_participants = 1
        
        self.game = Proyecto.main
        self.game.canvas = sugargame.canvas.PygameCanvas(
                self,
                main=self.game,
                modules=[pygame.display, pygame.font])
        self.set_canvas(self.game.canvas)
        self.game.canvas.grab_focus()

    def read_file(self, file_path):
        pass
        
    def write_file(self, file_path):
        pass
