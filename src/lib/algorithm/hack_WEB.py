from urllib.request import urlopen
from ..algorithm.app import App
from bs4 import BeautifulSoup
import sys
import re

class hack_WEB(App):
    def __init__(self, obj):
        self.obj = obj
        self.sql_sep = ', ' #by default
        self.main_url = self.obj['url_website']
        self.TOKEN = self.obj['app_token']

