import wx
import logging
from main import MainGUI


class Log():

    def __init__(self, dtype):
        self.dtype = dtype
        logging.basicConfig(level=self.dtype)
        self.logger = logging.getLogger(__name__)
        self.logger.debug('main constructor: __init__()')

""" Main run """
if __name__ == "__main__":
    Log(logging.INFO)
    app = wx.App(False)
    frame = MainGUI(None)
    frame.Show(True)
    app.MainLoop()
