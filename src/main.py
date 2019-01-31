#!/usr/bin/env python

import wx
import sys
import logging
import traceback

import mwhois.const as CONST
import mframe
from controller import SingleSearchThread, MultiSearchThread, LoadWordListFile
from util import WhoisClientUtil
from controller import GUIEvent
import exception


# Implementing MyFrame
class MainGUI(mframe.MyFrame):

    def __init__(self, parent):

        """
        MainGUI(mframe.MyFrame)
        """

        mframe.MyFrame.__init__(self, parent)

        logging.basicConfig(level=logging.INFO)
        self.logger = logging.getLogger(__name__)

        """Setup attributes"""
        self.s_worker = None
        self.m_worker = None
        self.l_worker = None
        self.history_select = False
        self.m_textctrl_domain.SetFocus()
        self.save_dialog = None
        self.dialog = wx.FileDialog(None, style=wx.OPEN)
        self.save_to_filename = None

        """Set icon"""
        ico = wx.Icon('images/mwhois.ico', wx.BITMAP_TYPE_ICO)
        self.SetIcon(ico)

        """Setup status icons"""
        green_image = 'images/green-circle.png'
        red_image = 'images/red-circle.png'
        yellow_image = 'images/yellow-circle.png'
        self.il = wx.ImageList(15, 15)
        self.green = self.il.Add(wx.Image(green_image, wx.BITMAP_TYPE_PNG).ConvertToBitmap())
        self.red = self.il.Add(wx.Image(red_image, wx.BITMAP_TYPE_PNG).ConvertToBitmap())
        self.yellow = self.il.Add(wx.Image(yellow_image, wx.BITMAP_TYPE_PNG).ConvertToBitmap())
        self.m_listctrl_multi.AssignImageList(self.il, wx.IMAGE_LIST_SMALL)


        """Setup post event Id's"""
        self.SINGLE_SEARCH_EVT_RESULT_ID = wx.NewId()
        self.MULTI_SEARCH_EVT_RESULT_ID = wx.NewId()
        self.SINGLE_SEARCH_EVT_ERROR_ID = wx.NewId()
        self.MULTI_SEARCH_EVT_ERROR_ID = wx.NewId()
        self.HISTORY_DISPLAY_EVT_ID = wx.NewId()
        self.CLEANUP_EVT_ID = wx.NewId()
        self.GUI_EVT_ERROR_ID = wx.NewId()

        """Bind post event functions """
        self.post_whois_search_result(self, self.do_whois_search_result)
        self.post_multi_whois_search_result(self, self.do_whois_multi_search_result)
        self.post_whois_search_error(self, self.do_whois_search_error)
        self.post_multi_whois_search_error(self, self.do_whois_multi_search_error)
        self.post_history_search(self, self.do_display_history_search)
        self.post_cleanup(self, self.do_cleanup)
        self.post_error(self, self.show_error_dialog)

        """Build GUIEvent Controller Instance"""
        self.guievt = GUIEvent(self)

        """ App Startup functions"""
        self.guievt.set_tld_list()

    """ Post event functions """
    def post_whois_search_result(self, win, func):
        """
        post_whois_search_result()
        """
        win.Connect(-1, -1, self.SINGLE_SEARCH_EVT_RESULT_ID, func)

    def post_multi_whois_search_result(self, win, func):
        """
        post_multi_whois_search_result()
        """
        win.Connect(-1, -1, self.MULTI_SEARCH_EVT_RESULT_ID, func)

    def post_whois_search_error(self, win, func):
        """
        post_whois_search_error()
        """
        win.Connect(-1, -1, self.SINGLE_SEARCH_EVT_ERROR_ID, func)

    def post_multi_whois_search_error(self, win, func):
        """
        post_multi_whois_search_error()
        """
        win.Connect(-1, -1, self.MULTI_SEARCH_EVT_ERROR_ID, func)

    def post_history_search(self, win, func):
        """
        post_history_search()
        """
        win.Connect(-1, -1, self.HISTORY_DISPLAY_EVT_ID, func)

    def post_cleanup(self, win, func):
        """
        post_cleanup()
        """
        win.Connect(-1, -1, self.CLEANUP_EVT_ID, func)

    def post_error(self, win, func):
        """
        post_cleanup()
        """
        win.Connect(-1, -1, self.GUI_EVT_ERROR_ID, func)

    """ UI events """

    def do_whois_search(self, event):

        self.m_button_single_search.Enable(False)
        self.m_textctrl_results.Clear()

        # if not self.m_textctrl_domain.GetValue():
        #     self.m_textctrl_results.SetValue('Please enter a domain')
        #     self.m_button_single_search.Enable(True)

        if not self.s_worker:
            self.s_worker = SingleSearchThread(self)
            self.s_worker.start()

    def do_whois_search_result(self, event):

        self.history_select = False
        self.m_textctrl_results.SetValue(event.data[0])
        self.m_textctrl_domain.Clear()
        self.m_combobox_whoisserver.Clear()
        self.m_button_single_search.Enable(True)
        self.m_combobox_whoisserver.SetValue('')

        if event.data[1] is CONST.DOMAIN_DEAD:
            self.m_static_is_alive.SetForegroundColour('Green')
            self.m_static_is_alive.SetLabel('Available')

        elif event.data[1] is CONST.DOMAIN_ALIVE:
            self.m_static_is_alive.SetForegroundColour(wx.RED)
            self.m_static_is_alive.SetLabel('Not Available')

        elif event.data[1] is CONST.DOMAIN_SEARCH_EXCEEDED:
            self.m_static_is_alive.SetForegroundColour(wx.RED)
            self.m_static_is_alive.SetLabel('Exceeded Limit')

        else:
            self.m_static_is_alive.SetForegroundColour('yellow')
            self.m_static_is_alive.SetLabel('Unknown')

        self.s_worker = None

    def do_whois_search_error(self, event):

        self.m_textctrl_domain.Clear()
        self.m_combobox_whoisserver.Clear()
        self.m_button_single_search.Enable(True)
        self.s_worker = None

    def do_multi_search(self, event):

        self.m_button_begin.Enable(False)
        self.m_button_stop_multi.Enable(True)
        self.m_listctrl_multi.ClearAll()

        """Setup multi display ctrl list columns"""
        self.m_listctrl_multi.InsertColumn(0, 'Status', width=150)
        self.m_listctrl_multi.InsertColumn(1, 'Domain', width=255)
        self.m_listctrl_multi.InsertColumn(2, 'Server', width=255)

        if not self.m_worker:
            self.m_worker = MultiSearchThread(self)
            self.m_worker.start()

    def do_whois_multi_search_result(self, event):

        info_color = wx.BLACK

        if event.data[0] is CONST.DOMAIN_ALIVE:
            status = 'Not Available'
            status_color = self.red
        elif event.data[0] is CONST.DOMAIN_DEAD:
            status = 'Available'
            status_color = self.green
        elif event.data[0] is CONST.DOMAIN_SEARCH_EXCEEDED:
            status = 'Exceeded Limit'
            status_color = self.red
        else:
            status = 'Unknown'
            status_color = self.yellow

        index = self.m_listctrl_multi.InsertStringItem(0, status)
        self.m_listctrl_multi.SetTextColour(info_color)
        self.m_listctrl_multi.SetItemImage(index, status_color)
        self.m_listctrl_multi.SetStringItem(index, 1, str(event.data[1]))
        self.m_listctrl_multi.SetStringItem(index, 2, str(event.data[5]))

    def do_whois_multi_search_error(self, event):

        self.do_cleanup()

    def do_history_search(self, event):
        """
        do_history_search()
        """
        """Used so only one single domain exist in the history list"""
        self.history_select = True

        self.do_whois_search(self)

    def do_display_history_search(self, event):

        if self.history_select is False:
            self.m_listbox_history.Append(event.data[0])

    def clear_history(self, event):

        self.m_listbox_history.Clear()

    def do_list_search(self, event):
        #TODO Implement this
        pass

    def do_whois_map(self, event):

        self.m_combobox_whoisserver.Clear()
        get_domain = self.m_textctrl_domain.GetValue()
        #TODO: Move into the GUIEvent Controller
        whois_map = WhoisClientUtil().map_whois_server(get_domain)

        if whois_map is not None:
            for map_list in whois_map:
                self.m_combobox_whoisserver.Append(map_list)
                self.m_combobox_whoisserver.SetSelection(0)

    def open_file_select(self, event):

        if self.dialog.ShowModal() == wx.ID_OK:
            self.m_textctrl_file.SetValue(self.dialog.GetPath())
            self.l_worker = LoadWordListFile(self)
            self.l_worker.run()

    def show_rightclick_menu_single(self, event):

        self.m_listbox_historyOnContextMenu(event)

    def do_right_click_history_query(self, event):
        """
        do_right_click_history_query()
        """
        """Used so only one single domain exist in the history list"""
        self.history_select = True

        item = self.m_listbox_history.GetSelection()
        selected_item = self.m_listbox_history.GetItems()
        self.m_textctrl_domain.SetValue(selected_item[item])

        self.do_whois_search(self)

    def do_right_click_history_delete(self, event):

        item = self.m_listbox_history.GetSelection()
        self.m_listbox_history.Delete(item)

    def show_rightclick_menu_multi(self, event):

        self.m_listctrl_multiOnContextMenu(event)

    def do_right_click_query(self, event):
        """
        do_right_click_query()
        """
        item = self.m_listctrl_multi.GetFirstSelected()

        if item is not -1:

            """Used so only one single domain exist in the history list"""
            #TODO: When enabling self.history_select = True it screws the below indexing ??
            #self.history_select = True

            selected_item = self.m_listctrl_multi.GetItem(item, 1).GetText()
            self.m_textctrl_domain.SetValue(selected_item)
            self.m_notebooktab.SetSelection(0)
            self.do_whois_search(self)

    def do_right_click_multi_delete(self, event):

        item = self.m_listctrl_multi.GetFirstSelected()
        self.m_listctrl_multi.DeleteItem(item)

    def do_right_click_dlist_delete(self, event):

        item = self.m_list_multi_list.GetSelection()
        self.m_list_multi_list.Delete(item)

    def do_right_click_multi_clearall(self, event):

        self.m_listctrl_multi.ClearAll()

    def open_url_history(self, event):
        """
        open_url_history()
        """

        item = self.m_listbox_history.GetSelection()
        selected_item = self.m_listbox_history.GetItems()
        domain = selected_item[item]

        WhoisClientUtil.copy_to_clipboard(domain)
        self.guievt.open_url_register(domain)

    def open_url_multi(self, event):
        """
        open_url_multi()
        """

        item = self.m_listctrl_multi.GetFirstSelected()
        selected_item = self.m_listctrl_multi.GetItem(item, 1).GetText()

        WhoisClientUtil.copy_to_clipboard(selected_item)
        self.guievt.open_url_register(selected_item)

    def copy_domain_name_mutil(self, event):
        """
        copy_domain_name_mutil()
        """

        item = self.m_listctrl_multi.GetFirstSelected()
        selected_item = self.m_listctrl_multi.GetItem(item, 1).GetText()

        WhoisClientUtil().copy_to_clipboard(selected_item)

    def copy_domain_name_single(self, event):
        """
        copy_domain_name_single()
        """

        item = self.m_listbox_history.GetSelection()
        selected_item = self.m_listbox_history.GetItems()
        domain = selected_item[item]

        WhoisClientUtil().copy_to_clipboard(domain)

    def stop_multi_process(self, event):

        self.m_worker.abort()
        self.do_cleanup()

    def do_add_multi_list(self, event):

        multi_list_domain = self.m_text_multi_list.GetValue()

        if len(multi_list_domain):
            self.m_list_multi_list.Append(self.m_text_multi_list.GetValue())
#
        self.m_text_multi_list.Clear()

    def do_clear_multi_list(self, event):

        self.m_list_multi_list.Clear()

    def do_cleanup(self, *event):
        """
        do_cleanup()
        """
        self.m_button_begin.Enable(True)
        self.m_button_stop_multi.Enable(False)
        self.m_static_mutil_status.SetLabel('Finished')
        self.m_worker = None

    def do_save_results(self, event):

        if self.m_panel_multi_search.IsShown():
            file_type = 'Comma delimited file (*.csv)|*.csv'
        else:
            file_type = 'Text file (*.txt)|*.txt'

        self.save_dialog = wx.FileDialog(None, "Save As", "", "", file_type, style=wx.SAVE)

        if self.save_dialog.ShowModal() == wx.ID_OK:

            self.save_to_filename = self.save_dialog.GetPath()
            #TODO Move this IsShown() method into other areas where it's needed ....etc rightclick event
            if self.m_panel_multi_search.IsShown():
                GUIEvent(self).save_mutli_results(self.save_to_filename)
            else:
                GUIEvent(self).save_single_results(self.save_to_filename)

        else:
            self.save_dialog.Destroy()

    def do_print_results(self, event):
        pass

    def open_about_dialog(self, event):
        """
        open_about_dialog()
        """
        import about_dialog

        about = wx.App(False)
        about_frame = about_dialog.AboutDialog(self)
        about.SetTopWindow(about_frame)
        about_frame.CentreOnParent()
        about_frame.Show()
        about.MainLoop()

    def open_properties(self, event):
        """
        open_properties
        """
        import prop_dialog

        prop = wx.App(False)
        prop_frame = prop_dialog.PropertyDialog(self)
        prop.SetTopWindow(prop_frame)
        prop_frame.CentreOnParent()
        prop_frame.Show()
        prop.MainLoop()

    def show_error_dialog(self, event):
        """
        show_error_dialog()
        """
        import about_dialog

        self.error_event = event

        error = wx.App(False)
        error_frame = about_dialog.ErrorDialog(self)
        error.SetTopWindow(error_frame)
        error_frame.CentreOnParent()
        error_frame.Show()
        error.MainLoop()

    def show_settings_dialog(self, event):

        #self.Disable()
        settings = wx.App(False)
        settings_frame = Settings(self)
        settings.SetTopWindow(settings_frame)
        settings_frame.CenterOnParent()
        settings_frame.Show()
        settings.MainLoop()

    def close_app(self, event):

        self.Destroy()
        sys.exit()

    #TODO Bind an event or remove the below functions
    def set_preveiw_results(self, event):
        pass

    def on_tld_combo_select(self, event):
        pass

    def on_gtld_combo_select(self, event):
        pass

    def set_dead_only(self, event):
        pass

    def set_sleep(self, event):
        pass

    def create_new_tab(self, event):
        pass


class Settings(mframe.SettingsDialog):

    def __init__(self, parent):

        mframe.SettingsDialog.__init__(self, parent)
        self.parent = parent
        self.parent.Disable()
        #self.m_staticText_timeout_value.SetLabel(str(self.m_connection_timeout_silder.GetValue()))
        self.socks5_proxy_pos = 0
        self.socks4_proxy_pos = 1
        self.http_proxy_pos = 2
        self._check_settings()

        logging.basicConfig(level=logging.INFO)
        self.logger = logging.getLogger(__name__)

    def _check_settings(self):

        proxy_enabled = bool(GUIEvent(self).check_bool_settings('proxy_enabled'))

        if proxy_enabled is True:
            self.m_checkBox_proxy_setting.SetValue(True)
            self.m_textCtrl_host.Enable()
            self.m_textCtrl_port.Enable()
            self.m_textCtrl_username.Enable()
            self.m_textCtrl_password.Enable()
            self.m_proxy_choice.Enable()

        try:
            host_proxy = str(GUIEvent(self).check_settings('proxy_host'))
            port_proxy = str(GUIEvent(self).check_settings('proxy_port'))
            username_proxy = str(GUIEvent(self).check_settings('proxy_user'))
            passwd_proxy = str(GUIEvent(self).check_settings('proxy_pass'))
            type_proxy = int(GUIEvent(self).check_settings('proxy_type'))
            connection_timeout = int(GUIEvent(self).check_settings('connection_timeout'))
        except Exception:
            raise exception.GUIException(self.parent, traceback.format_exc())
            self.parent.Enable()

        if host_proxy not in "None": self.m_textCtrl_host.SetValue(host_proxy)
        if port_proxy not in "None": self.m_textCtrl_port.SetValue(port_proxy)
        if username_proxy not in "None": self.m_textCtrl_username.SetValue(username_proxy)
        if passwd_proxy not in "None": self.m_textCtrl_password.SetValue(passwd_proxy)
        self.m_connection_timeout_silder.SetValue(connection_timeout)
        self.m_staticText_timeout_value.SetLabel(str(connection_timeout))

        if type_proxy is CONST.PROXY_TYPE_SOCKS4: self.m_proxy_choice.SetSelection(self.socks4_proxy_pos)
        if type_proxy is CONST.PROXY_TYPE_SOCKS5: self.m_proxy_choice.SetSelection(self.socks5_proxy_pos)
        if type_proxy is CONST.PROXY_TYPE_HTTP: self.m_proxy_choice.SetSelection(self.http_proxy_pos)

    def enable_settings_form(self, event):

        if self.m_checkBox_proxy_setting.GetValue() is True:
            self.m_textCtrl_host.Enable()
            self.m_textCtrl_port.Enable()
            self.m_textCtrl_username.Enable()
            self.m_textCtrl_password.Enable()
            self.m_proxy_choice.Enable()
        else:
            self.m_textCtrl_host.Disable()
            self.m_textCtrl_port.Disable()
            self.m_textCtrl_username.Disable()
            self.m_textCtrl_password.Disable()
            self.m_proxy_choice.Disable()

    def get_timeout_value(self, event):
        self.m_staticText_timeout_value.SetLabel(str(self.m_connection_timeout_silder.GetValue()))

    def apply_settings(self, event):

        GUIEvent(self).write_settings('proxy_enabled', self.m_checkBox_proxy_setting.GetValue())
        GUIEvent(self).write_settings('proxy_host', self.m_textCtrl_host.GetValue())
        GUIEvent(self).write_settings('proxy_port', self.m_textCtrl_port.GetValue())
        GUIEvent(self).write_settings('proxy_user', self.m_textCtrl_username.GetValue())
        GUIEvent(self).write_settings('proxy_pass', self.m_textCtrl_password.GetValue())
        GUIEvent(self).write_settings('connection_timeout', int(self.m_connection_timeout_silder.GetValue()))

        if self.m_proxy_choice.GetSelection() is self.socks4_proxy_pos:
            GUIEvent(self).write_settings('proxy_type', CONST.PROXY_TYPE_SOCKS4)
        if self.m_proxy_choice.GetSelection() is self.socks5_proxy_pos:
            GUIEvent(self).write_settings('proxy_type', CONST.PROXY_TYPE_SOCKS5)
        if self.m_proxy_choice.GetSelection() is self.http_proxy_pos:
            GUIEvent(self).write_settings('proxy_type', CONST.PROXY_TYPE_HTTP)

        self.parent.Enable()
        self.Destroy()

    def close_settings(self, event):

        self.parent.Enable()
        self.Destroy()
