#!/usr/bin/env python

import wx
from threading import *
import logging
import traceback

from mwhois.whosearch import WhoisSearch
import exception

from util import WhoisClientUtil, WhoisSettings


class SingleSearchThread(Thread):
    
    def __init__(self, window_obj):
       
        Thread.__init__(self)
        self._window_obj = window_obj
        self.setDaemon(True)
        self.history_list_counter = 0
        self.history = {}
        self.domain = None

        logging.basicConfig(level=logging.INFO)
        self.logger = logging.getLogger(__name__)
        self.logger.debug('SingleSearchThread constructor: __init__()')
        
    def run(self):
       
        self.logger.debug('called SingleSearchThread().run')

        search = WhoisSearch()

        try:

            proxy_enabled = bool(GUIEvent(self).check_bool_settings('proxy_enabled'))

            if proxy_enabled is True:
                search.connection.proxy = True
                search.connection.proxy_host = str(GUIEvent(self).check_settings('proxy_host'))
                search.connection.proxy_port = int(GUIEvent(self).check_settings('proxy_port'))
                search.connection.proxy_type = int(GUIEvent(self).check_settings('proxy_type'))
            else:
                search.connection.proxy = False
            
            self.logger.debug('trying search thread')
            
            if self._window_obj.history_select is True:

                self.logger.debug('history select enabled.')
                history_items = self._window_obj.m_listbox_history.GetItems()
                search.dname = history_items[self._window_obj.m_listbox_history.GetSelection()]

                #TODO Have history search use stored results. Need to have history data stored in a list type
                # domain_history_list_no = self._window_obj.m_listbox_history.GetSelection()
                # self.logger.debug('history select enabled. using %s' % domain_history_list_no)
                # self._window_obj.history_select = False
                #
                # try:
                #     domain_history = str(self.get_history(domain_history_list_no))
                #     wx.PostEvent(self._window_obj, ResultEvent(self._window_obj.SINGLE_SEARCH_EVT_RESULT_ID,
                #                                                domain_history, 2))
                # except Exception, e:
                #     wx.PostEvent(self._window_obj, ResultEvent(self._window_obj.SINGLE_SEARCH_EVT_ERROR_ID, str(e)))
                
            else:
                search.dname = self._window_obj.m_textctrl_domain.GetValue()
                search.whois_server = str(self._window_obj.m_combobox_whoisserver.GetValue())

            self.logger.debug('doing a whois search via whois servers')

            search.connection.timeout = int(GUIEvent(self).check_settings('connection_timeout'))
            search.whois_search()

            #self.set_history(self.history_list_counter, search.response())
            #self.history_list_counter += 1

            wx.PostEvent(self._window_obj, ResultEvent(self._window_obj.HISTORY_DISPLAY_EVT_ID,
                                                       search.dname))
            wx.PostEvent(self._window_obj, ResultEvent(self._window_obj.SINGLE_SEARCH_EVT_RESULT_ID,
                                                       search.response(), search.whois_info.is_domain_alive()))
        except Exception, e:

            self.logger.error('error %s' % str(e))
            wx.PostEvent(self._window_obj, ResultEvent(self._window_obj.SINGLE_SEARCH_EVT_ERROR_ID, str(e)))
            raise exception.GUIException(self._window_obj, traceback.format_exc())

    def get_history(self, position):
        
        self.logger.debug('called get_history()')
        self.logger.debug('get %s' % self.history)
        return self.history.get(position)

    def set_history(self, domain_history, response):
        
        self.logger.debug('called set_history()')
        self.history.update({domain_history:response})
        self.logger.debug('set %s' % self.history)
        return


class MultiSearchThread(Thread):
    
    def __init__(self, window_obj):
       
        Thread.__init__(self)
        self._window_obj = window_obj
        self.setDaemon(True)
        self._want_abort = 0
        
        logging.basicConfig(level=logging.INFO)
        self.logger = logging.getLogger(__name__)
        self.logger.debug('MultiSearchThread constructor: __init__()')
        
    def run(self):
        
        self.logger.debug('called MultiSearchThread().run')
        
        search = WhoisSearch()
        search.wordlist = self._window_obj.m_list_multi_list.GetItems()

        #TODO If multi list box has values use it else get file from file textbox
        #Disabled....
        # if len(self._window_obj.m_list_multi_list.GetItems()):
        #     self.logger.debug('using mutil gui listbox')
        #     search.wordlist = self._window_obj.m_list_multi_list.GetItems()
        # else:
        #     self.logger.debug('using mutil word file textbox')
        #     search.wordlist = self._window_obj.m_textctrl_file.GetValue()

        tld = self._window_obj.m_combo_tld.GetValue()
        cctld = self._window_obj.m_combo_cctld.GetValue()
        gtld = self._window_obj.m_combo_gtld.GetValue()
        
        if tld != '' and cctld != '':search.tld = tld + "." + cctld
        elif tld != '':search.tld = tld
        elif cctld != '':search.tld = cctld
        elif gtld != '':search.tld = gtld
        #else:search.tld = 'com'
            
        if self._window_obj.m_checkbox_dead.GetValue() is True: search.deadonly = True
        
        if not len(self._window_obj.m_textctrl_sleep.GetValue()):
            self._window_obj.m_textctrl_sleep.SetValue('0')

        search.sleep = float(self._window_obj.m_textctrl_sleep.GetValue())

        try:

            proxy_enabled = bool(GUIEvent(self).check_bool_settings('proxy_enabled'))

            if proxy_enabled is True:
                search.connection.proxy = True
                search.connection.proxy_host = str(GUIEvent(self).check_settings('proxy_host'))
                search.connection.proxy_port = int(GUIEvent(self).check_settings('proxy_port'))
                search.connection.proxy_type = int(GUIEvent(self).check_settings('proxy_type'))
            else:
                search.connection.proxy = False

            search.connection.timeout = int(GUIEvent(self).check_settings('connection_timeout'))

            multi = search.whois_multi_search()

            for multi_list in multi:

                status = multi_list[0]
                domain = multi_list[1]
                whois_server = search.whois_server
                creation_date = search.creation_date()
                expiry_date = search.expiry_date()
                update_date = search.update_date()

                if self._want_abort is 0:
                    wx.PostEvent(self._window_obj, ResultEvent(self._window_obj.MULTI_SEARCH_EVT_RESULT_ID, status,
                                                               domain, creation_date, expiry_date, update_date,
                                                               whois_server))
                else:
                    self.logger.debug('aborted MultiSearchThread()')
                    break

        except Exception, e:

            self.logger.debug('error in MultiSearchThread() %s' % e)
            wx.PostEvent(self._window_obj, ResultEvent(self._window_obj.MULTI_SEARCH_EVT_ERROR_ID, e))
            raise exception.GUIException(self._window_obj, traceback.format_exc())

        self.logger.debug('cleanup MultiSearchThread()')
        wx.PostEvent(self._window_obj, ResultEvent(self._window_obj.CLEANUP_EVT_ID, self))

    def abort(self):

        self.logger.debug('abort MultiSearchThread()')
        self._want_abort = 1


class LoadWordListFile(Thread):

    def __init__(self, window_obj):

        Thread.__init__(self)
        self._window_obj = window_obj
        self.setDaemon(True)
        self._want_abort = 0

        logging.basicConfig(level=logging.INFO)
        self.logger = logging.getLogger(__name__)
        self.logger.debug('LoadWordListFile constructor: __init__()')

        self.load_wordlist = self._window_obj.m_textctrl_file.GetValue()

    def run(self):

        self.logger.debug('called LoadWordListFile().run')
        list_it = WhoisClientUtil.list_wordlist(self.load_wordlist)

        try:

            for line_txt in list_it:
                self._window_obj.m_list_multi_list.Append(line_txt)
        except Exception:
            self._window_obj.m_list_multi_list.Clear()
            raise exception.GUIException(self._window_obj, traceback.format_exc())


class ResultEvent(wx.PyEvent):
    
    def __init__(self, event_id, *args):

        self.event_id = event_id
        wx.PyEvent.__init__(self)
        self.SetEventType(self.event_id)
        self.data = args
        

class GUIEvent():
     
    def __init__(self, win_obj):
         
        self.history = {}
        self._win_obj = win_obj
        self.domain = None

        self.logger = logging.getLogger(__name__)
        self.logger.debug('GUIEvent constructor: __init__()')
        self.settings_path = WhoisSettings.settings_location()
        self.settings = WhoisSettings('Settings', self.settings_path)
         
    def get_history(self, position):
        
        self.logger.debug('called get_history()')
        self.logger.debug('return %s' % self.history)
        return self.history[position]
        
    def set_history(self, domain_history, response):
        
        self.logger.debug('called set_history()')
        self.history.update({domain_history:response})
        self.logger.debug('return %s' % self.history)
        return
    
    def set_tld_list(self):

        self.logger.debug('called set_tld_list()')
        client_util = WhoisClientUtil()
        tld_list = client_util.get_tld()
        cctld = client_util.get_cctld()
        gtld = client_util.get_gtld()
        
        self._win_obj.m_combo_tld.SetItems(tld_list)
        self._win_obj.m_combo_cctld.SetItems(cctld)
        self._win_obj.m_combo_gtld.SetItems(gtld)
        return

    def open_url_register(self, domain):
        """
        open_url_register()
        """
        self.logger.debug('called open_url_register()')
        WhoisClientUtil.open_url(domain)

    def copy_to_clipboard(self, copy_this):
        """
        copy_to_clipboard()
        """
        self.logger.debug('called copy_to_clipboard()')
        WhoisClientUtil().copy_to_clipboard(copy_this)

    def get_domain_properties(self, domain):
        """
        get_domain_properties()
        """
        self.logger.debug('called get_domain_properties()')
        self.domain = domain
        prop = WhoisSearch(dname=self.domain)
        prop.whois_search()
        cdate = prop.creation_date()
        edate = prop.expiry_date()
        udate = prop.update_date()
        email = prop.emails()
        reg = prop.registrant()
        return cdate, edate, udate, email, reg

    def save_mutli_results(self, filename):
        """
        save_multi_results()
        :param filename: string
        """
        self.logger.debug('called save_mutli_results()')

        multi_list_dict = {}

        count = self._win_obj.m_listctrl_multi.GetItemCount()

        for row in range(count):
            item1 = self._win_obj.m_listctrl_multi.GetItem(itemId=row, col=0)
            item2 = self._win_obj.m_listctrl_multi.GetItem(itemId=row, col=1)
            item3 = self._win_obj.m_listctrl_multi.GetItem(itemId=row, col=2)

            multi_list_dict[row] = [item1.GetText(), item2.GetText(), item3.GetText()]

        save = WhoisClientUtil.write_multi_file(multi_list_dict, filename)

        if save is True:
            wx.MessageBox('Saved to File', 'Saved', wx.OK | wx.ICON_INFORMATION)
        else:
            wx.MessageBox('Error saving file', 'Error', wx.OK | wx.ICON_ERROR)

    def save_single_results(self, filename):
        """
        save_single_results()
        :param filename: string
        """
        self.logger.debug('called save_single_results()')

        result_txt = self._win_obj.m_textctrl_results.GetValue()
        save = WhoisClientUtil.write_single_file(result_txt, filename)

        if save is True:
            wx.MessageBox('Saved to File', 'Saved', wx.OK | wx.ICON_INFORMATION)
        else:
            wx.MessageBox('Error saving file', 'Error', wx.OK | wx.ICON_ERROR)

    def check_settings(self, key):

        return self.settings.read_config(key)

    def check_bool_settings(self, key):

        return self.settings.read_config_bool(key)

    def write_settings(self, key, value):

        self.settings.save_to_config(key, value)