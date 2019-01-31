# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Feb 26 2014)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import _version as mwhois_info

###########################################################################
## Class AboutDialog
###########################################################################


class AboutDialog(wx.Dialog):
    def __init__(self, parent):
        wx.Dialog.__init__(self, parent, id=wx.ID_ANY, title=u"About - %s" % mwhois_info.__name__, pos=wx.DefaultPosition,
                           size=wx.DefaultSize, style=wx.CLOSE_BOX | wx.DEFAULT_DIALOG_STYLE | wx.STAY_ON_TOP)

        self.SetSizeHintsSz(wx.DefaultSize, wx.DefaultSize)

        bSizer2 = wx.BoxSizer(wx.VERTICAL)

        bSizer5 = wx.BoxSizer(wx.VERTICAL)

        self.m_bitmap2 = wx.StaticBitmap(self, wx.ID_ANY, wx.Bitmap(u"images/mwhois.ico", wx.BITMAP_TYPE_ANY),
                                         wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer5.Add(self.m_bitmap2, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        bSizer2.Add(bSizer5, 0, wx.EXPAND, 5)

        bSizer6 = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText1 = wx.StaticText(self, wx.ID_ANY, mwhois_info.__name__, wx.DefaultPosition, wx.DefaultSize,
                                           0)
        self.m_staticText1.Wrap(-1)
        bSizer6.Add(self.m_staticText1, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        bSizer2.Add(bSizer6, 0, wx.EXPAND, 5)

        bSizer20 = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText5 = wx.StaticText(self, wx.ID_ANY, mwhois_info.__version__, wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText5.Wrap(-1)
        bSizer20.Add(self.m_staticText5, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        bSizer2.Add(bSizer20, 1, wx.EXPAND, 5)

        bSizer7 = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText2 = wx.StaticText(self, wx.ID_ANY, mwhois_info.__description__,wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText2.Wrap(-1)
        bSizer7.Add(self.m_staticText2, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        bSizer2.Add(bSizer7, 0, wx.EXPAND, 5)

        bSizer10 = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText3 = wx.StaticText(self, wx.ID_ANY, u"Copyright © %s" % mwhois_info.__copyright__, wx.DefaultPosition,
                                           wx.DefaultSize, 0)
        self.m_staticText3.Wrap(-1)
        bSizer10.Add(self.m_staticText3, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        bSizer2.Add(bSizer10, 0, wx.EXPAND, 5)

        bSizer11 = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText4 = wx.StaticText(self, wx.ID_ANY, mwhois_info.__website__,
                                           wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText4.Wrap(-1)
        bSizer11.Add(self.m_staticText4, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        bSizer2.Add(bSizer11, 0, wx.EXPAND, 5)

        bSizer12 = wx.BoxSizer(wx.HORIZONTAL)

        bSizer13 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_button9 = wx.Button(self, wx.ID_ANY, u"License", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer13.Add(self.m_button9, 0, wx.ALL, 5)

        self.m_button5 = wx.Button(self, wx.ID_ANY, u"Website", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer13.Add(self.m_button5, 0, wx.ALL, 5)

        bSizer12.Add(bSizer13, 1, wx.EXPAND, 5)

        bSizer14 = wx.BoxSizer(wx.VERTICAL)

        self.m_button10 = wx.Button(self, wx.ID_ANY, u"Close", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer14.Add(self.m_button10, 0, wx.ALL | wx.ALIGN_RIGHT, 5)

        bSizer12.Add(bSizer14, 1, wx.EXPAND, 5)

        bSizer2.Add(bSizer12, 0, wx.EXPAND, 5)

        self.SetSizer(bSizer2)
        self.Layout()
        bSizer2.Fit(self)

        self.Centre(wx.BOTH)

        # Connect Events
        self.m_button9.Bind(wx.EVT_BUTTON, self.show_license)
        self.m_button5.Bind(wx.EVT_BUTTON, self.open_project_url)
        self.m_button10.Bind(wx.EVT_BUTTON, self.close_dialog)

    def __del__(self):
        pass


    # Virtual event handlers, overide them in your derived class
    def show_license(self, event):
        event.Skip()

    def open_project_url(self, event):
        event.Skip()

    def close_dialog(self, event):
        event.Skip()


###########################################################################
## Class LicenseDialog
###########################################################################

class LicenseDialog(wx.Dialog):
    def __init__(self, parent):
        wx.Dialog.__init__(self, parent, id=wx.ID_ANY, title="%s - %s" % (mwhois_info.__license__, mwhois_info.__name__),
                           pos=wx.DefaultPosition, size=wx.Size(600, 400),
                           style=wx.CLOSE_BOX | wx.DEFAULT_DIALOG_STYLE | wx.STAY_ON_TOP)

        self.SetSizeHintsSz(wx.DefaultSize, wx.DefaultSize)

        bSizer15 = wx.BoxSizer(wx.VERTICAL)

        bSizer16 = wx.BoxSizer(wx.VERTICAL)

        self.m_textCtrl1 = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize,
                                       wx.TE_MULTILINE | wx.TE_READONLY | wx.TE_RICH)
        bSizer16.Add(self.m_textCtrl1, 1, wx.ALL | wx.EXPAND, 5)

        bSizer15.Add(bSizer16, 1, wx.EXPAND, 5)

        bSizer17 = wx.BoxSizer(wx.VERTICAL)

        self.m_button11 = wx.Button(self, wx.ID_ANY, u"Close", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer17.Add(self.m_button11, 0, wx.ALL | wx.ALIGN_RIGHT, 5)

        bSizer15.Add(bSizer17, 0, wx.EXPAND, 5)

        self.SetSizer(bSizer15)
        self.Layout()

        self.Centre(wx.BOTH)

        # Connect Events
        self.m_button11.Bind(wx.EVT_BUTTON, self.close_license)

    def __del__(self):
        pass

    # Virtual event handlers, overide them in your derived class
    def close_license(self, event):
        event.Skip()


###########################################################################
## Class ErrorDialog
###########################################################################

class ErrorDialog(wx.Dialog):
    def __init__(self, parent):
        wx.Dialog.__init__(self, parent, id=wx.ID_ANY, title=u"Error Handler", pos=wx.DefaultPosition,
                           size=wx.Size(600, 400), style=wx.DEFAULT_DIALOG_STYLE)

        self.SetSizeHintsSz(wx.DefaultSize, wx.DefaultSize)

        bSizer14 = wx.BoxSizer(wx.VERTICAL)

        bSizer15 = wx.BoxSizer(wx.VERTICAL)

        self.m_textCtrl_error = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize,
                                            wx.TE_MULTILINE | wx.TE_READONLY | wx.TE_RICH2)
        bSizer15.Add(self.m_textCtrl_error, 1, wx.ALL | wx.EXPAND, 5)

        bSizer14.Add(bSizer15, 1, wx.EXPAND, 5)

        bSizer16 = wx.BoxSizer(wx.VERTICAL)

        self.m_button5 = wx.Button(self, wx.ID_ANY, u"Close", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer16.Add(self.m_button5, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        bSizer14.Add(bSizer16, 0, wx.EXPAND, 5)

        self.SetSizer(bSizer14)
        self.Layout()

        self.Centre(wx.BOTH)

        # Connect Events
        self.m_button5.Bind(wx.EVT_BUTTON, self.close_error_dialog)

    def __del__(self):
        pass

    # Virtual event handlers, overide them in your derived class
    def close_error_dialog(self, event):
        event.Skip()


