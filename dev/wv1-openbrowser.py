#!/usr/bin/python3
import webbrowser
import cgi
import cgitb
cgitb.enable()


url = 'http://www.google.com'  #string that points to site to open
webbrowser.open_new(url) #opens new window, using url string

