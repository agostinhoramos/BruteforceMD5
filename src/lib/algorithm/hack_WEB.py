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

    #STUDING HTML WEBPAGE
    def HTMLformOBJ(self):
        OBJ = {"url":[],"name":[],"method":[]}
        html = urlopen(self.main_url)
        soup = BeautifulSoup(html.read(), features="html.parser")
        try:
            values = soup.find_all('form')
            for value in values:
                v = value.get('action')
                if v:
                    OBJ["url"].append(v)
        except:
            return []
        try:
            values = soup.find_all("input")
            for value in values:
                v = value.get('name')
                if v:
                    OBJ["name"].append(v)
        except:
            return []
        try:
            values = soup.find_all('form')
            for val in values:
                v = val.get('method')
                if v:
                    OBJ["method"].append(v.upper())
        except:
            pass
        return OBJ