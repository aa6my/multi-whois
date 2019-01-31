# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jun  6 2014)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class MyFrame
###########################################################################

class MyFrame ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Multi Whois", pos = wx.Point( -1,-1 ), size = wx.Size( 1024,768 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.Size( 1024,768 ), wx.Size( -1,-1 ) )
		
		self.m_menubar_top = wx.MenuBar( 0 )
		self.m_menu_file = wx.Menu()
		self.m_menuItem_save = wx.MenuItem( self.m_menu_file, wx.ID_ANY, u"Save", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu_file.AppendItem( self.m_menuItem_save )
		
		self.m_menuItem_settings = wx.MenuItem( self.m_menu_file, wx.ID_ANY, u"Settings", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu_file.AppendItem( self.m_menuItem_settings )
		
		self.m_menuItem_close = wx.MenuItem( self.m_menu_file, wx.ID_ANY, u"Close", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu_file.AppendItem( self.m_menuItem_close )
		
		self.m_menubar_top.Append( self.m_menu_file, u"File" ) 
		
		self.m_menu_help = wx.Menu()
		self.m_menuItem_about = wx.MenuItem( self.m_menu_help, wx.ID_ANY, u"About", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu_help.AppendItem( self.m_menuItem_about )
		
		self.m_menubar_top.Append( self.m_menu_help, u"Help" ) 
		
		self.SetMenuBar( self.m_menubar_top )
		
		bSizerMainWindow = wx.BoxSizer( wx.VERTICAL )
		
		self.m_notebooktab = wx.Notebook( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_panel_single_search = wx.Panel( self.m_notebooktab, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer3 = wx.BoxSizer( wx.VERTICAL )
		
		gSizerSearchArea = wx.GridSizer( 0, 3, 0, 0 )
		
		bSizer4 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticTextDomainLabel = wx.StaticText( self.m_panel_single_search, wx.ID_ANY, u"Domain", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticTextDomainLabel.Wrap( -1 )
		bSizer4.Add( self.m_staticTextDomainLabel, 0, wx.ALL, 5 )
		
		self.m_textctrl_domain = wx.TextCtrl( self.m_panel_single_search, wx.ID_ANY, wx.EmptyString, wx.Point( -1,-1 ), wx.Size( 255,-1 ), wx.TE_PROCESS_ENTER )
		self.m_textctrl_domain.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 90, False, wx.EmptyString ) )
		self.m_textctrl_domain.SetToolTipString( u"Enter domain to search" )
		
		bSizer4.Add( self.m_textctrl_domain, 0, wx.ALL, 5 )
		
		
		gSizerSearchArea.Add( bSizer4, 0, 0, 5 )
		
		bSizer7 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticTextWhoisServerLabel = wx.StaticText( self.m_panel_single_search, wx.ID_ANY, u"Choose Whois Server", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticTextWhoisServerLabel.Wrap( -1 )
		bSizer7.Add( self.m_staticTextWhoisServerLabel, 0, wx.ALL, 5 )
		
		m_combobox_whoisserverChoices = []
		self.m_combobox_whoisserver = wx.ComboBox( self.m_panel_single_search, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 255,-1 ), m_combobox_whoisserverChoices, wx.CB_READONLY )
		self.m_combobox_whoisserver.SetSelection( 0 )
		self.m_combobox_whoisserver.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 90, False, wx.EmptyString ) )
		self.m_combobox_whoisserver.SetToolTipString( u"Select whois server after entering domain " )
		
		bSizer7.Add( self.m_combobox_whoisserver, 0, wx.ALL|wx.EXPAND, 5 )
		
		
		gSizerSearchArea.Add( bSizer7, 0, 0, 5 )
		
		bSizer8 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticTextSearchHidden = wx.StaticText( self.m_panel_single_search, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticTextSearchHidden.Wrap( -1 )
		bSizer8.Add( self.m_staticTextSearchHidden, 0, wx.ALL, 5 )
		
		self.m_button_single_search = wx.Button( self.m_panel_single_search, wx.ID_ANY, u"Search", wx.DefaultPosition, wx.Size( -1,-1 ), 0 )
		self.m_button_single_search.SetToolTipString( u"Begin search query" )
		
		bSizer8.Add( self.m_button_single_search, 0, wx.ALIGN_RIGHT, 5 )
		
		
		gSizerSearchArea.Add( bSizer8, 0, 0, 5 )
		
		
		bSizer3.Add( gSizerSearchArea, 0, wx.EXPAND, 5 )
		
		gSizerResultsArea = wx.GridSizer( 0, 2, 0, 0 )
		
		bSizer9 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer9.SetMinSize( wx.Size( 600,-1 ) ) 
		self.m_staticText6 = wx.StaticText( self.m_panel_single_search, wx.ID_ANY, u"Results", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText6.Wrap( -1 )
		bSizer9.Add( self.m_staticText6, 0, wx.ALL, 5 )
		
		self.m_textctrl_results = wx.TextCtrl( self.m_panel_single_search, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( -1,-1 ), wx.TE_MULTILINE|wx.TE_READONLY|wx.TE_WORDWRAP )
		bSizer9.Add( self.m_textctrl_results, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		gSizerResultsArea.Add( bSizer9, 1, wx.EXPAND, 5 )
		
		bSizer11 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer181 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText7 = wx.StaticText( self.m_panel_single_search, wx.ID_ANY, u"History", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText7.Wrap( -1 )
		bSizer181.Add( self.m_staticText7, 0, wx.ALL, 5 )
		
		self.m_staticText13 = wx.StaticText( self.m_panel_single_search, wx.ID_ANY, u"(Clear)", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText13.Wrap( -1 )
		self.m_staticText13.Hide()
		
		bSizer181.Add( self.m_staticText13, 0, wx.ALL, 5 )
		
		self.m_button_clear_history = wx.Button( self.m_panel_single_search, wx.ID_ANY, u"(Clear History)", wx.DefaultPosition, wx.DefaultSize, 0|wx.NO_BORDER )
		self.m_button_clear_history.SetToolTipString( u"Clear history list" )
		
		bSizer181.Add( self.m_button_clear_history, 0, 0, 5 )
		
		
		bSizer11.Add( bSizer181, 0, wx.EXPAND, 5 )
		
		m_listbox_historyChoices = []
		self.m_listbox_history = wx.ListBox( self.m_panel_single_search, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_listbox_historyChoices, wx.LB_NEEDED_SB|wx.LB_SINGLE )
		self.m_listbox_history.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 90, False, wx.EmptyString ) )
		
		self.m_rightclick_menu_single = wx.Menu()
		self.m_menuItem13 = wx.MenuItem( self.m_rightclick_menu_single, wx.ID_ANY, u"Perform Query", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_rightclick_menu_single.AppendItem( self.m_menuItem13 )
		
		self.m_menuItem111 = wx.MenuItem( self.m_rightclick_menu_single, wx.ID_ANY, u"Register Domain", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_rightclick_menu_single.AppendItem( self.m_menuItem111 )
		
		self.m_menuItem15 = wx.MenuItem( self.m_rightclick_menu_single, wx.ID_ANY, u"Copy", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_rightclick_menu_single.AppendItem( self.m_menuItem15 )
		
		self.m_menuItem52 = wx.MenuItem( self.m_rightclick_menu_single, wx.ID_ANY, u"Delete", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_rightclick_menu_single.AppendItem( self.m_menuItem52 )
		
		self.m_listbox_history.Bind( wx.EVT_RIGHT_DOWN, self.m_listbox_historyOnContextMenu ) 
		
		bSizer11.Add( self.m_listbox_history, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		gSizerResultsArea.Add( bSizer11, 1, wx.EXPAND, 5 )
		
		
		bSizer3.Add( gSizerResultsArea, 1, wx.EXPAND, 5 )
		
		gSizerBottomButtons = wx.GridSizer( 0, 2, 1, 1 )
		
		bSizer18 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_button_print1 = wx.Button( self.m_panel_single_search, wx.ID_ANY, u"Print", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_button_print1.Hide()
		
		bSizer18.Add( self.m_button_print1, 0, wx.ALL, 5 )
		
		self.m_button_quit1 = wx.Button( self.m_panel_single_search, wx.ID_ANY, u"Quit", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_button_quit1.SetToolTipString( u"Quit application" )
		
		bSizer18.Add( self.m_button_quit1, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )
		
		self.m_button_save1 = wx.Button( self.m_panel_single_search, wx.ID_ANY, u"Save", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer18.Add( self.m_button_save1, 0, wx.ALL, 5 )
		
		
		gSizerBottomButtons.Add( bSizer18, 0, 0, 5 )
		
		bSizer21 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_static_is_alive = wx.StaticText( self.m_panel_single_search, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 110,-1 ), wx.ALIGN_RIGHT )
		self.m_static_is_alive.Wrap( -1 )
		bSizer21.Add( self.m_static_is_alive, 0, wx.ALIGN_RIGHT|wx.ALL|wx.FIXED_MINSIZE, 5 )
		
		
		gSizerBottomButtons.Add( bSizer21, 1, wx.EXPAND|wx.ALIGN_RIGHT, 5 )
		
		
		bSizer3.Add( gSizerBottomButtons, 0, wx.EXPAND, 5 )
		
		
		self.m_panel_single_search.SetSizer( bSizer3 )
		self.m_panel_single_search.Layout()
		bSizer3.Fit( self.m_panel_single_search )
		self.m_notebooktab.AddPage( self.m_panel_single_search, u"Single Search", True )
		self.m_panel_multi_search = wx.Panel( self.m_notebooktab, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer19 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer24 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText71 = wx.StaticText( self.m_panel_multi_search, wx.ID_ANY, u"Wordlist", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText71.Wrap( -1 )
		bSizer24.Add( self.m_staticText71, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_textctrl_file = wx.TextCtrl( self.m_panel_multi_search, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 255,-1 ), 0 )
		bSizer24.Add( self.m_textctrl_file, 0, wx.ALL, 5 )
		
		self.m_button_open = wx.Button( self.m_panel_multi_search, wx.ID_ANY, u"Open", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer24.Add( self.m_button_open, 0, wx.ALL, 5 )
		
		self.m_staticText11 = wx.StaticText( self.m_panel_multi_search, wx.ID_ANY, u"TLD:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText11.Wrap( -1 )
		bSizer24.Add( self.m_staticText11, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		m_combo_tldChoices = []
		self.m_combo_tld = wx.ComboBox( self.m_panel_multi_search, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 80,-1 ), m_combo_tldChoices, wx.CB_DROPDOWN|wx.CB_READONLY )
		bSizer24.Add( self.m_combo_tld, 0, wx.ALL, 5 )
		
		self.m_staticText12 = wx.StaticText( self.m_panel_multi_search, wx.ID_ANY, u"and/or ccTLD:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText12.Wrap( -1 )
		bSizer24.Add( self.m_staticText12, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		m_combo_cctldChoices = []
		self.m_combo_cctld = wx.ComboBox( self.m_panel_multi_search, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 80,-1 ), m_combo_cctldChoices, wx.CB_DROPDOWN|wx.CB_READONLY )
		bSizer24.Add( self.m_combo_cctld, 0, wx.ALL, 5 )
		
		self.m_staticText131 = wx.StaticText( self.m_panel_multi_search, wx.ID_ANY, u"or gTLD:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText131.Wrap( -1 )
		bSizer24.Add( self.m_staticText131, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		m_combo_gtldChoices = []
		self.m_combo_gtld = wx.ComboBox( self.m_panel_multi_search, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 150,-1 ), m_combo_gtldChoices, wx.CB_DROPDOWN|wx.CB_READONLY )
		bSizer24.Add( self.m_combo_gtld, 0, wx.ALL, 5 )
		
		
		bSizer19.Add( bSizer24, 0, wx.ALL|wx.EXPAND, 5 )
		
		bSizer25 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText9 = wx.StaticText( self.m_panel_multi_search, wx.ID_ANY, u"Options", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText9.Wrap( -1 )
		bSizer25.Add( self.m_staticText9, 0, wx.ALL, 5 )
		
		
		bSizer19.Add( bSizer25, 0, wx.ALL|wx.EXPAND, 5 )
		
		bSizer26 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_checkbox_dead = wx.CheckBox( self.m_panel_multi_search, wx.ID_ANY, u"Dead Only", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_checkbox_dead.SetToolTipString( u"Show only domains that are available" )
		
		bSizer26.Add( self.m_checkbox_dead, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_staticline1 = wx.StaticLine( self.m_panel_multi_search, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL|wx.LI_VERTICAL )
		self.m_staticline1.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNTEXT ) )
		self.m_staticline1.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNTEXT ) )
		
		bSizer26.Add( self.m_staticline1, 0, wx.EXPAND |wx.ALL, 5 )
		
		self.m_staticText10 = wx.StaticText( self.m_panel_multi_search, wx.ID_ANY, u"Sleep", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText10.Wrap( -1 )
		bSizer26.Add( self.m_staticText10, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_textctrl_sleep = wx.TextCtrl( self.m_panel_multi_search, wx.ID_ANY, u"0", wx.DefaultPosition, wx.Size( 40,-1 ), 0 )
		self.m_textctrl_sleep.SetToolTipString( u"Number of seconds to sleep between whois queries" )
		
		bSizer26.Add( self.m_textctrl_sleep, 0, wx.ALL, 5 )
		
		self.m_staticline2 = wx.StaticLine( self.m_panel_multi_search, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL|wx.LI_VERTICAL )
		bSizer26.Add( self.m_staticline2, 0, wx.EXPAND |wx.ALL, 5 )
		
		self.m_button_begin = wx.Button( self.m_panel_multi_search, wx.ID_ANY, u"Begin", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_button_begin.SetToolTipString( u"Start searching" )
		
		bSizer26.Add( self.m_button_begin, 0, wx.ALL, 5 )
		
		self.m_button_stop_multi = wx.Button( self.m_panel_multi_search, wx.ID_ANY, u"Stop", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_button_stop_multi.Enable( False )
		
		bSizer26.Add( self.m_button_stop_multi, 0, wx.ALL, 5 )
		
		
		bSizer19.Add( bSizer26, 0, wx.ALL|wx.EXPAND, 5 )
		
		bSizer27 = wx.BoxSizer( wx.HORIZONTAL )
		
		bSizer192 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer192.SetMinSize( wx.Size( 700,-1 ) ) 
		self.m_listctrl_multi = wx.ListCtrl( self.m_panel_multi_search, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,-1 ), wx.LC_REPORT|wx.SUNKEN_BORDER )
		self.m_rightclick_menu_multi = wx.Menu()
		self.m_menuItem1 = wx.MenuItem( self.m_rightclick_menu_multi, wx.ID_ANY, u"Perform Query", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_rightclick_menu_multi.AppendItem( self.m_menuItem1 )
		
		self.m_menuItem11 = wx.MenuItem( self.m_rightclick_menu_multi, wx.ID_ANY, u"Register Domain", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_rightclick_menu_multi.AppendItem( self.m_menuItem11 )
		
		self.m_menuItem16 = wx.MenuItem( self.m_rightclick_menu_multi, wx.ID_ANY, u"Copy", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_rightclick_menu_multi.AppendItem( self.m_menuItem16 )
		
		self.m_menuItem12 = wx.MenuItem( self.m_rightclick_menu_multi, wx.ID_ANY, u"Delete", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_rightclick_menu_multi.AppendItem( self.m_menuItem12 )
		
		self.m_menuItem_clear = wx.MenuItem( self.m_rightclick_menu_multi, wx.ID_ANY, u"Clear All", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_rightclick_menu_multi.AppendItem( self.m_menuItem_clear )
		
		self.m_menuItem121 = wx.MenuItem( self.m_rightclick_menu_multi, wx.ID_ANY, u"Properties", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_rightclick_menu_multi.AppendItem( self.m_menuItem121 )
		
		self.m_listctrl_multi.Bind( wx.EVT_RIGHT_DOWN, self.m_listctrl_multiOnContextMenu ) 
		
		bSizer192.Add( self.m_listctrl_multi, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		bSizer27.Add( bSizer192, 0, wx.EXPAND, 5 )
		
		bSizer20 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText15 = wx.StaticText( self.m_panel_multi_search, wx.ID_ANY, u"Domain List", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText15.Wrap( -1 )
		bSizer20.Add( self.m_staticText15, 0, wx.ALL, 5 )
		
		m_list_multi_listChoices = []
		self.m_list_multi_list = wx.ListBox( self.m_panel_multi_search, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_list_multi_listChoices, 0 )
		self.m_menu5 = wx.Menu()
		self.m_menu_dlist__delete = wx.MenuItem( self.m_menu5, wx.ID_ANY, u"Delete", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu5.AppendItem( self.m_menu_dlist__delete )
		
		self.m_list_multi_list.Bind( wx.EVT_RIGHT_DOWN, self.m_list_multi_listOnContextMenu ) 
		
		bSizer20.Add( self.m_list_multi_list, 1, wx.ALL|wx.ALIGN_RIGHT|wx.EXPAND, 5 )
		
		bSizer22 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_text_multi_list = wx.TextCtrl( self.m_panel_multi_search, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_PROCESS_ENTER )
		bSizer22.Add( self.m_text_multi_list, 0, wx.ALL|wx.EXPAND, 5 )
		
		
		bSizer20.Add( bSizer22, 0, wx.EXPAND, 5 )
		
		bSizer211 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_button12 = wx.Button( self.m_panel_multi_search, wx.ID_ANY, u"Add", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer211.Add( self.m_button12, 0, wx.ALL, 5 )
		
		self.m_button14 = wx.Button( self.m_panel_multi_search, wx.ID_ANY, u"Clear All", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer211.Add( self.m_button14, 0, wx.ALL, 5 )
		
		
		bSizer20.Add( bSizer211, 0, wx.EXPAND, 5 )
		
		
		bSizer27.Add( bSizer20, 1, wx.EXPAND, 5 )
		
		
		bSizer19.Add( bSizer27, 1, wx.ALL|wx.EXPAND, 5 )
		
		bSizer182 = wx.BoxSizer( wx.HORIZONTAL )
		
		bSizer28 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_button_print2 = wx.Button( self.m_panel_multi_search, wx.ID_ANY, u"Print", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_button_print2.Hide()
		
		bSizer28.Add( self.m_button_print2, 0, wx.ALL, 5 )
		
		self.m_button_quit2 = wx.Button( self.m_panel_multi_search, wx.ID_ANY, u"Quit", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer28.Add( self.m_button_quit2, 0, wx.ALL, 5 )
		
		self.m_button_save2 = wx.Button( self.m_panel_multi_search, wx.ID_ANY, u"Save", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer28.Add( self.m_button_save2, 0, wx.ALL, 5 )
		
		
		bSizer182.Add( bSizer28, 0, wx.ALIGN_BOTTOM|wx.EXPAND, 5 )
		
		bSizer191 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_static_mutil_status = wx.StaticText( self.m_panel_multi_search, wx.ID_ANY, u"Status", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_LEFT )
		self.m_static_mutil_status.Wrap( -1 )
		self.m_static_mutil_status.Hide()
		
		bSizer191.Add( self.m_static_mutil_status, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )
		
		
		bSizer182.Add( bSizer191, 1, wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		bSizer19.Add( bSizer182, 0, wx.EXPAND, 5 )
		
		
		self.m_panel_multi_search.SetSizer( bSizer19 )
		self.m_panel_multi_search.Layout()
		bSizer19.Fit( self.m_panel_multi_search )
		self.m_notebooktab.AddPage( self.m_panel_multi_search, u"Multi Search", False )
		
		bSizerMainWindow.Add( self.m_notebooktab, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		self.SetSizer( bSizerMainWindow )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.Bind( wx.EVT_CLOSE, self.close_app )
		self.Bind( wx.EVT_MENU, self.do_save_results, id = self.m_menuItem_save.GetId() )
		self.Bind( wx.EVT_MENU, self.show_settings_dialog, id = self.m_menuItem_settings.GetId() )
		self.Bind( wx.EVT_MENU, self.close_app, id = self.m_menuItem_close.GetId() )
		self.Bind( wx.EVT_MENU, self.open_about_dialog, id = self.m_menuItem_about.GetId() )
		self.m_textctrl_domain.Bind( wx.EVT_TEXT, self.do_whois_map )
		self.m_textctrl_domain.Bind( wx.EVT_TEXT_ENTER, self.do_whois_search )
		self.m_button_single_search.Bind( wx.EVT_BUTTON, self.do_whois_search )
		self.m_button_clear_history.Bind( wx.EVT_BUTTON, self.clear_history )
		self.m_listbox_history.Bind( wx.EVT_LISTBOX_DCLICK, self.do_history_search )
		self.m_listbox_history.Bind( wx.EVT_RIGHT_DOWN, self.show_rightclick_menu )
		self.Bind( wx.EVT_MENU, self.do_right_click_history_query, id = self.m_menuItem13.GetId() )
		self.Bind( wx.EVT_MENU, self.open_url_history, id = self.m_menuItem111.GetId() )
		self.Bind( wx.EVT_MENU, self.copy_domain_name_single, id = self.m_menuItem15.GetId() )
		self.Bind( wx.EVT_MENU, self.do_right_click_history_delete, id = self.m_menuItem52.GetId() )
		self.m_button_print1.Bind( wx.EVT_BUTTON, self.do_print_results )
		self.m_button_quit1.Bind( wx.EVT_BUTTON, self.close_app )
		self.m_button_save1.Bind( wx.EVT_BUTTON, self.do_save_results )
		self.m_button_open.Bind( wx.EVT_BUTTON, self.open_file_select )
		self.m_checkbox_dead.Bind( wx.EVT_CHECKBOX, self.set_dead_only )
		self.m_button_begin.Bind( wx.EVT_BUTTON, self.do_multi_search )
		self.m_button_stop_multi.Bind( wx.EVT_BUTTON, self.stop_multi_process )
		self.m_listctrl_multi.Bind( wx.EVT_LEFT_DCLICK, self.do_list_search )
		self.m_listctrl_multi.Bind( wx.EVT_RIGHT_DOWN, self.show_rightclick_menu )
		self.Bind( wx.EVT_MENU, self.do_right_click_query, id = self.m_menuItem1.GetId() )
		self.Bind( wx.EVT_MENU, self.open_url_multi, id = self.m_menuItem11.GetId() )
		self.Bind( wx.EVT_MENU, self.copy_domain_name_mutil, id = self.m_menuItem16.GetId() )
		self.Bind( wx.EVT_MENU, self.do_right_click_multi_delete, id = self.m_menuItem12.GetId() )
		self.Bind( wx.EVT_MENU, self.do_right_click_multi_clearall, id = self.m_menuItem_clear.GetId() )
		self.Bind( wx.EVT_MENU, self.open_properties, id = self.m_menuItem121.GetId() )
		self.Bind( wx.EVT_MENU, self.do_right_click_dlist_delete, id = self.m_menu_dlist__delete.GetId() )
		self.m_text_multi_list.Bind( wx.EVT_TEXT_ENTER, self.do_add_multi_list )
		self.m_button12.Bind( wx.EVT_BUTTON, self.do_add_multi_list )
		self.m_button14.Bind( wx.EVT_BUTTON, self.do_clear_multi_list )
		self.m_button_print2.Bind( wx.EVT_BUTTON, self.do_print_results )
		self.m_button_quit2.Bind( wx.EVT_BUTTON, self.close_app )
		self.m_button_save2.Bind( wx.EVT_BUTTON, self.do_save_results )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def close_app( self, event ):
		event.Skip()
	
	def do_save_results( self, event ):
		event.Skip()
	
	def show_settings_dialog( self, event ):
		event.Skip()
	
	
	def open_about_dialog( self, event ):
		event.Skip()
	
	def do_whois_map( self, event ):
		event.Skip()
	
	def do_whois_search( self, event ):
		event.Skip()
	
	
	def clear_history( self, event ):
		event.Skip()
	
	def do_history_search( self, event ):
		event.Skip()
	
	def show_rightclick_menu( self, event ):
		event.Skip()
	
	def do_right_click_history_query( self, event ):
		event.Skip()
	
	def open_url_history( self, event ):
		event.Skip()
	
	def copy_domain_name_single( self, event ):
		event.Skip()
	
	def do_right_click_history_delete( self, event ):
		event.Skip()
	
	def do_print_results( self, event ):
		event.Skip()
	
	
	
	def open_file_select( self, event ):
		event.Skip()
	
	def set_dead_only( self, event ):
		event.Skip()
	
	def do_multi_search( self, event ):
		event.Skip()
	
	def stop_multi_process( self, event ):
		event.Skip()
	
	def do_list_search( self, event ):
		event.Skip()
	
	
	def do_right_click_query( self, event ):
		event.Skip()
	
	def open_url_multi( self, event ):
		event.Skip()
	
	def copy_domain_name_mutil( self, event ):
		event.Skip()
	
	def do_right_click_multi_delete( self, event ):
		event.Skip()
	
	def do_right_click_multi_clearall( self, event ):
		event.Skip()
	
	def open_properties( self, event ):
		event.Skip()
	
	def do_right_click_dlist_delete( self, event ):
		event.Skip()
	
	def do_add_multi_list( self, event ):
		event.Skip()
	
	
	def do_clear_multi_list( self, event ):
		event.Skip()
	
	
	
	
	def m_listbox_historyOnContextMenu( self, event ):
		self.m_listbox_history.PopupMenu( self.m_rightclick_menu_single, event.GetPosition() )
		
	def m_listctrl_multiOnContextMenu( self, event ):
		self.m_listctrl_multi.PopupMenu( self.m_rightclick_menu_multi, event.GetPosition() )
		
	def m_list_multi_listOnContextMenu( self, event ):
		self.m_list_multi_list.PopupMenu( self.m_menu5, event.GetPosition() )
		

###########################################################################
## Class PropertyDialog
###########################################################################

class PropertyDialog ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Domain Properties", pos = wx.DefaultPosition, size = wx.Size( -1,-1 ), style = wx.CLOSE_BOX|wx.DEFAULT_DIALOG_STYLE|wx.STAY_ON_TOP )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		gSizer4 = wx.GridSizer( 0, 2, 0, 0 )
		
		self.m_staticText28 = wx.StaticText( self, wx.ID_ANY, u"Domain Name:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText28.Wrap( -1 )
		gSizer4.Add( self.m_staticText28, 0, wx.ALL, 5 )
		
		self.m_staticTxt_domain_prop = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 255,-1 ), 0 )
		self.m_staticTxt_domain_prop.Wrap( -1 )
		gSizer4.Add( self.m_staticTxt_domain_prop, 0, wx.ALL, 5 )
		
		self.m_staticText16 = wx.StaticText( self, wx.ID_ANY, u"Creation Date:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText16.Wrap( -1 )
		gSizer4.Add( self.m_staticText16, 0, wx.ALL, 5 )
		
		self.m_staticTxt_cdate_prop = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticTxt_cdate_prop.Wrap( -1 )
		gSizer4.Add( self.m_staticTxt_cdate_prop, 0, wx.ALL, 5 )
		
		self.m_staticText18 = wx.StaticText( self, wx.ID_ANY, u"Expiry Date:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText18.Wrap( -1 )
		gSizer4.Add( self.m_staticText18, 0, wx.ALL, 5 )
		
		self.m_staticTxt_edate_prop = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticTxt_edate_prop.Wrap( -1 )
		gSizer4.Add( self.m_staticTxt_edate_prop, 0, wx.ALL, 5 )
		
		self.m_staticText20 = wx.StaticText( self, wx.ID_ANY, u"Update Date:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText20.Wrap( -1 )
		gSizer4.Add( self.m_staticText20, 0, wx.ALL, 5 )
		
		self.m_staticTxt_udate_prop = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticTxt_udate_prop.Wrap( -1 )
		gSizer4.Add( self.m_staticTxt_udate_prop, 0, wx.ALL, 5 )
		
		self.m_staticText24 = wx.StaticText( self, wx.ID_ANY, u"Registrant:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText24.Wrap( -1 )
		self.m_staticText24.Hide()
		
		gSizer4.Add( self.m_staticText24, 0, wx.ALL, 5 )
		
		self.m_staticTxt_reg_prop = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticTxt_reg_prop.Wrap( -1 )
		gSizer4.Add( self.m_staticTxt_reg_prop, 0, wx.ALL, 5 )
		
		self.m_staticText22 = wx.StaticText( self, wx.ID_ANY, u"Email:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText22.Wrap( -1 )
		self.m_staticText22.Hide()
		
		gSizer4.Add( self.m_staticText22, 0, wx.ALL, 5 )
		
		self.m_staticTxt_email_prop = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticTxt_email_prop.Wrap( -1 )
		gSizer4.Add( self.m_staticTxt_email_prop, 0, wx.ALL, 5 )
		
		self.m_button14 = wx.Button( self, wx.ID_ANY, u"Close", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer4.Add( self.m_button14, 0, wx.ALL, 5 )
		
		
		self.SetSizer( gSizer4 )
		self.Layout()
		gSizer4.Fit( self )
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.m_button14.Bind( wx.EVT_BUTTON, self.close_prop_box )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def close_prop_box( self, event ):
		event.Skip()
	

###########################################################################
## Class SettingsDialog
###########################################################################

class SettingsDialog ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.DefaultSize, style = wx.DEFAULT_DIALOG_STYLE )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer23 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer24 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText28 = wx.StaticText( self, wx.ID_ANY, u"Proxy Settings", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText28.Wrap( -1 )
		bSizer24.Add( self.m_staticText28, 0, wx.ALL, 5 )
		
		
		bSizer24.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.m_staticline3 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer24.Add( self.m_staticline3, 0, wx.EXPAND |wx.ALL, 5 )
		
		
		bSizer23.Add( bSizer24, 0, wx.EXPAND, 5 )
		
		bSizer26 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText33 = wx.StaticText( self, wx.ID_ANY, u"Enable Proxy", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText33.Wrap( -1 )
		bSizer26.Add( self.m_staticText33, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_checkBox_proxy_setting = wx.CheckBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_RIGHT )
		bSizer26.Add( self.m_checkBox_proxy_setting, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_staticText34 = wx.StaticText( self, wx.ID_ANY, u"Proxy Type", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText34.Wrap( -1 )
		bSizer26.Add( self.m_staticText34, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		m_proxy_choiceChoices = [ u"SOCKS5", u"SOCKS4", u"HTTP" ]
		self.m_proxy_choice = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_proxy_choiceChoices, 0 )
		self.m_proxy_choice.SetSelection( 0 )
		self.m_proxy_choice.Enable( False )
		
		bSizer26.Add( self.m_proxy_choice, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		bSizer23.Add( bSizer26, 0, wx.EXPAND, 5 )
		
		gSizer5 = wx.GridSizer( 2, 4, 0, 0 )
		
		self.m_staticText_host = wx.StaticText( self, wx.ID_ANY, u"Host", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText_host.Wrap( -1 )
		gSizer5.Add( self.m_staticText_host, 0, wx.ALL, 5 )
		
		self.m_textCtrl_host = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( -1,-1 ), 0 )
		self.m_textCtrl_host.Enable( False )
		
		gSizer5.Add( self.m_textCtrl_host, 0, wx.ALL, 5 )
		
		self.m_staticText_port = wx.StaticText( self, wx.ID_ANY, u"Port", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText_port.Wrap( -1 )
		gSizer5.Add( self.m_staticText_port, 0, wx.ALL, 5 )
		
		self.m_textCtrl_port = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( -1,-1 ), 0 )
		self.m_textCtrl_port.Enable( False )
		
		gSizer5.Add( self.m_textCtrl_port, 0, wx.ALL, 5 )
		
		self.m_staticText_username = wx.StaticText( self, wx.ID_ANY, u"Username", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText_username.Wrap( -1 )
		gSizer5.Add( self.m_staticText_username, 0, wx.ALL, 5 )
		
		self.m_textCtrl_username = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_textCtrl_username.Enable( False )
		
		gSizer5.Add( self.m_textCtrl_username, 0, wx.ALL, 5 )
		
		self.m_staticText_password = wx.StaticText( self, wx.ID_ANY, u"Password", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText_password.Wrap( -1 )
		gSizer5.Add( self.m_staticText_password, 0, wx.ALL, 5 )
		
		self.m_textCtrl_password = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_PASSWORD )
		self.m_textCtrl_password.Enable( False )
		
		gSizer5.Add( self.m_textCtrl_password, 0, wx.ALL, 5 )
		
		
		bSizer23.Add( gSizer5, 0, wx.EXPAND, 5 )
		
		bSizer27 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText35 = wx.StaticText( self, wx.ID_ANY, u"Connection Timeout", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText35.Wrap( -1 )
		bSizer27.Add( self.m_staticText35, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_connection_timeout_silder = wx.Slider( self, wx.ID_ANY, 10, 1, 60, wx.DefaultPosition, wx.Size( 120,-1 ), wx.SL_HORIZONTAL )
		bSizer27.Add( self.m_connection_timeout_silder, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_staticText_timeout_value = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText_timeout_value.Wrap( -1 )
		bSizer27.Add( self.m_staticText_timeout_value, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		bSizer23.Add( bSizer27, 1, wx.EXPAND, 5 )
		
		bSizer25 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_button_setting_ok = wx.Button( self, wx.ID_ANY, u"OK", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer25.Add( self.m_button_setting_ok, 0, wx.ALL|wx.ALIGN_BOTTOM, 5 )
		
		self.m_button1_settings_close = wx.Button( self, wx.ID_ANY, u"Close", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer25.Add( self.m_button1_settings_close, 0, wx.ALL|wx.ALIGN_BOTTOM, 5 )
		
		
		bSizer23.Add( bSizer25, 1, wx.EXPAND, 5 )
		
		
		self.SetSizer( bSizer23 )
		self.Layout()
		bSizer23.Fit( self )
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.m_checkBox_proxy_setting.Bind( wx.EVT_CHECKBOX, self.enable_settings_form )
		self.m_connection_timeout_silder.Bind( wx.EVT_SCROLL, self.get_timeout_value )
		self.m_button_setting_ok.Bind( wx.EVT_BUTTON, self.apply_settings )
		self.m_button1_settings_close.Bind( wx.EVT_BUTTON, self.close_settings )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def enable_settings_form( self, event ):
		event.Skip()
	
	def get_timeout_value( self, event ):
		event.Skip()
	
	def apply_settings( self, event ):
		event.Skip()
	
	def close_settings( self, event ):
		event.Skip()
	

