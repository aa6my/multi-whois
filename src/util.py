#!/usr/bin/env python

from mwhois.whomap import WhoisServerMap
import mwhois.const as CONST
import ConfigParser
import exception
import traceback
import os
import platform

class WhoisClientUtil():

    def __init__(self):
        """
        WhoisClientUtil()
        """

    @staticmethod
    def map_whois_server(domain):
        
        tld = domain.split('.')
        server = WhoisServerMap().all_server_map
    
        for keys, values in server.items():
            if keys == tld[-1]:
                return values[0], values[1]
            else:
                continue
#
    @staticmethod
    def get_tld():
        
        get_tld = WhoisServerMap().all_server_map
        tld = ['', 'co']
        
        for keys, values in get_tld.items():
            if values[4] is CONST.TLD_STANDARD:
                tld.append(keys)
        tld.sort()
        return tld

    @staticmethod
    def get_cctld():
        
        get_cctld = WhoisServerMap().all_server_map
        cctld = ['']
        
        for keys, values in get_cctld.items():
            if values[4] is CONST.CCTLD_STANDARD:
                cctld.append(keys)
        
        cctld.sort()
        return cctld

    @staticmethod
    def get_gtld():
        
        get_gtld = WhoisServerMap().all_server_map
        gtld = ['']
        
        for keys, values in get_gtld.items():
            if values[4] is CONST.GTLD_STANDARD or values[4] is CONST.GTLD_DONUTS\
                    or values[4] is CONST.GTLD_UNIREG or values[4] is CONST.GTLD_UNITED\
                    or values[4] is CONST.GTLD_RIGHTSIDE:
                gtld.append(keys)
        gtld.sort()
        return gtld

    @staticmethod
    def open_url(domain):
        """
        open_url()
        """

        try:
            name_aff_id = 7811
            url = 'https://www.name.com/domain/search'
            import webbrowser
            """Go Daddy """
            #webbrowser.open_new_tab('http://x.co/42JkU')
            """Name.com"""
            #webbrowser.open_new_tab('https://www.name.com/domain/search/?aff_id=%d&domain=%s' % (name_aff_id, domain))
            """ Name.com 2 """
            webbrowser.open_new_tab('%s?utm_campaign=affiliate&utm_source=%s&utm_medium=&utm_content=&domain=%s'
                                    % (url, name_aff_id, domain))

        except:
            pass
            #TODO Either fix below exception or remove this and it's inheritance
            #raise exception.GUIException(controller.GUIEvent(self)._win_obj, traceback.format_exc())
            #raise exception.GUIException(e)

    @staticmethod
    def copy_to_clipboard(copy_this):
        """
        copy_to_clipboard()
        """
        import wx

        clipdata = wx.TextDataObject()
        clipdata.SetText(copy_this)
        wx.TheClipboard.Open()
        wx.TheClipboard.SetData(clipdata)
        wx.TheClipboard.Close()

    @staticmethod
    def list_wordlist(wordlist):
        """
        list_wordlist()
        """
        with open(wordlist) as f:
            lines = f.read().splitlines()
        return lines

    @staticmethod
    def write_multi_file(result_list, filename):
        """
        write_multi_file()
        :param result_list: dict
        :param filename: string
        """
        try:
            import csv
            with open(filename, 'wb') as csvfile:
                mwriter = csv.writer(csvfile, delimiter=',', quotechar=',', quoting=csv.QUOTE_MINIMAL)
                mwriter.writerow(['Status', 'Domain Name', 'Whois Server'])
                for key, values in result_list.iteritems():
                    mwriter.writerow(values)
            return True
        except:
            return False

    @staticmethod
    def write_single_file(result_txt, filename):
        """
        write_single_file()
        :param result_txt: string
        :param filename: string
        """
        try:
            single_save = open(filename, 'w')
            single_save.write(result_txt)
            single_save.close()
            return True
        except:
            return False


class WhoisSettings:

    def __init__(self, section, location):

        self.section = section
        self.location = location

    @staticmethod
    def settings_location():

        linux_os = 'linux'
        windows_os = 'windows'
        home_path = None
        os_type = platform.system()

        if os_type.lower() == linux_os:
            home_path = os.path.expanduser('~')
        elif os_type.lower() is windows_os:
            home_path = os.path.expanduser('~')
        else:
            home_path = os.path.expanduser('~')
            print 'Unknown OS'

        file_path = home_path + '/.mwhois_settings.cfg'

        if not os.path.isfile(file_path):
            try:
                open(file_path, 'a').close()
                WhoisSettings.write_config_file(file_path)
            except Exception:
                raise exception.GeneralException(traceback.format_exc())
        else:
            pass

        return file_path

    def read_config(self, key):

        #print 'read_settings()'
        try:
            config = ConfigParser.ConfigParser()
            config.read(self.location)
            value = config.get(self.section, key)
        except Exception:
            raise exception.GeneralException(traceback.format_exc())

        return value

    def read_config_bool(self, key):

        #print 'read_bool_settings()'
        try:
            config = ConfigParser.ConfigParser()
            config.read(self.location)
            bool_value = config.getboolean(self.section, key)
        except Exception:
            raise exception.GeneralException(traceback.format_exc())

        return bool_value

    def save_to_config(self, key, value):

        #print 'write_settings()'
        try:
            config = ConfigParser.ConfigParser()
            config.read(self.location)

            if self.section not in config.sections():
                config.add_section(self.section)

            config.set(self.section, key, value)
            with open(self.location, 'wb') as cf:
                config.write(cf)
        except Exception:
            raise exception.GeneralException(traceback.format_exc())

    @staticmethod
    def write_config_file(location):

        cfgfile = open(location, 'w')
        config = ConfigParser.ConfigParser()
        config.add_section('Settings')
        config.set('Settings', 'proxy_enabled', False)
        config.set('Settings', 'proxy_host')
        config.set('Settings', 'proxy_port')
        config.set('Settings', 'proxy_user')
        config.set('Settings', 'proxy_pass')
        config.set('Settings', 'proxy_type', 2)
        config.set('Settings', 'connection_timeout', 10)
        config.write(cfgfile)
        cfgfile.close()