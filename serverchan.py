import tkinter as tk
from tkinter import ttk
import time
import requests
import configparser


class MainWindows(tk.Tk):

    _url = ''

    def __init__(self):

        super().__init__()
        self.init_gui()
        self.resizable(0, 0)

    def init_gui(self):

        self.title('ServerChan')
        self.geometry('600x365')
        self.lbltitle = tk.Label(self, text='Title')
        # self.lbltitle.pack()
        self.lbltitle.place(x=20, y=2)
        self.txttitle = tk.Text(self, width=80, height=3)
        # self.txttitle.pack()
        self.txttitle.place(x=20, y=20)
        self.lbltext = tk.Label(self, text='Text')
        # self.lbltext.pack()
        self.lbltext.place(x=20, y=65)
        self.txttext = tk.Text(self, width=80, height=10)
        # self.txttext.pack()
        self.txttext.place(x=20, y=90)
        self.lblresult = tk.Label(self, text='Result')
        # self.lblresult.pack()
        self.lblresult.place(x=20, y=230)
        self.txtresult = tk.Text(self, width=80, height=3)
        # self.txtresult.pack()
        self.txtresult.place(x=20, y=250)
        self.btn = tk.Button(self, width=20, height=3, text='SEND')
        # self.btn.pack()
        self.btn.place(x=220, y=300)
        self.btn.config(command=self.send_fun)

    def send_fun(self):

        rtn = self.req_url()
        self.txtresult.insert('0.0', rtn)

    def req_url(self):

        self.config_url(self.txttitle.get('0.0', tk.END), self.txttext.get('0.0', tk.END))
        header = {

            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36',

            'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',

            'Host':'sc.ftqq.com',

            'Connection':'keep-alive',

            'Accept-Encoding': 'gzip, deflate, br',

            'Accept-Language': 'en-US,en;q=0.9',

            'Sec-Fetch-Dest': 'document',

            'Sec-Fetch-Mode': 'navigate',

            'Sec-Fetch-Site': 'none',

            'Sec-Fetch-User': '?1',

            'Upgrade-Insecure-Requests': '1'

            }
        res = requests.get(url=self._url, headers=header)
        return res

    def read_ini(self, inikey, inivaluse):
        config = configparser.ConfigParser()
        config.read("./config.ini", encoding="utf-8")
        convaluse = config.get(inikey, inivaluse)
        return convaluse

    def config_url(self, text, desp):

        self._url = 'https://sc.ftqq.com/'+self.read_ini('info', 'key') + '.send?text='+text+'&&desp='+desp


if __name__ == '__main__':

    app = MainWindows()

    app.mainloop()
