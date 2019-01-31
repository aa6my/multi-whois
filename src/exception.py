#!/usr/bin/env python

import wx
import controller


class GUIException(Exception):

    def __init__(self, window, error):
        self.error = error
        self._window_obj = window
        Exception.__init__(self, 'Error: %s' % self.error)
        wx.PostEvent(self._window_obj, controller.ResultEvent(self._window_obj.GUI_EVT_ERROR_ID, str(error)))
        pass


class GeneralException(Exception):

    def __init__(self, error):
        self.error = error
        Exception.__init__(self, 'Error: %s' % self.error)
        pass