import tkinter as tk
from tkinter import ttk
import re
import time


class App(object):
    def __init__(self):
        self.root = tk.Tk()
        self.root.resizable(False, False)
        self.layout()
        self.root.mainloop()

    def layout(self):
        tabContainer = ttk.Notebook(self.root)
        tabContainer.pack()

        ipTab = ttk.Frame(tabContainer)
        tabContainer.add(ipTab, text=' IP ')
        self._layIpTab(ipTab)

        timeTab = ttk.Frame(tabContainer)
        tabContainer.add(timeTab, text='TIME')
        self._layTimeTab(timeTab)

    def _layIpTab(self, tab):
        self.ip = tk.StringVar();
        self.ip.set('127.0.0.1')
        ttk.Label(tab, text='IPv4:') \
            .grid(row=0, column=0, padx=5, pady=10)
        ttk.Entry(tab, textvariable=self.ip, justify='right', width=25) \
            .grid(row=0, column=1, padx=5, pady=10, columnspan=3)

        self.ipVal = tk.StringVar()
        ttk.Label(tab, text='10进制') \
            .grid(row=1, column=0, padx=5, pady=10)
        ttk.Entry(tab, textvariable=self.ipVal, justify='right', width=25) \
            .grid(row=1, column=1, padx=5, pady=10, columnspan=3)

        self.ipHex = tk.StringVar()
        ttk.Label(tab, text='16进制') \
            .grid(row=2, column=0, padx=5, pady=10)
        ttk.Entry(tab, textvariable=self.ipHex, justify='right', state='disabled', width=25) \
            .grid(row=2, column=1, padx=5, pady=10, columnspan=3)

        ttk.Button(tab, text='Reset', command=self._resetIp) \
            .grid(row=3, column=1, padx=5, pady=10)
        transferBtn = ttk.Button(tab, text='Transfer', command=self._transferIp)
        transferBtn.grid(row=3, column=2, padx=5, pady=10)

    def _layTimeTab(self, tab):
        self.timestamp = tk.StringVar()
        ttk.Label(tab, text='时间戳:').grid(row=0, column=0, padx=5, pady=10)
        ttk.Entry(tab, justify='right', width=25, textvariable=self.timestamp) \
            .grid(row=0, column=1, padx=5, pady=10, columnspan=3)

        self.unit = tk.StringVar();
        self.unit.set('ms')
        ttk.Radiobutton(tab, text='毫秒', variable=self.unit, value='ms') \
            .grid(row=1, column=1, padx=5, pady=10)
        ttk.Radiobutton(tab, text='秒', variable=self.unit, value='s') \
            .grid(row=1, column=2, padx=5, pady=10)

        self.dataTime = tk.StringVar()
        ttk.Label(tab, text='日期:').grid(row=2, column=0, padx=5, pady=10)
        ttk.Entry(tab, justify='right', width=25, textvariable=self.dataTime) \
            .grid(row=2, column=1, padx=5, pady=10, columnspan=3)

        ttk.Button(tab, text='NOW', command=self._now) \
            .grid(row=3, column=1, padx=5, pady=10)
        ttk.Button(tab, text='转换', command=self._ts2date) \
            .grid(row=3, column=2, padx=5, pady=10)

    def _resetIp(self):
        self.ip.set('')
        self.ipVal.set('')
        self.ipHex.set('')

    def _transferIp(self):
        if self.ip.get():
            ip = self.ip.get()
            if not self._validIp(ip):
                self._resetIp()
                self.ip.set('Invalid IP')
                return

            ipVal = self._ip2long(ip)
            self.ipVal.set(ipVal)

            ipHex = self._ip2hex(ip)
            self.ipHex.set(ipHex)

        elif self.ipVal.get():
            ipVal = self.ipVal.get()
            ip = self._long2ip(ipVal)

            if not ip:
                self._resetIp()
                self.ipVal.set('Invalid IP number')
                return

            self.ip.set(ip)
            ipHex = self._ip2hex(ip)
            self.ipHex.set(ipHex)

    def _ip2long(self, ip):
        ipSeg = ip.split('.')
        val = 0
        for i in range(len(ipSeg)):
            val += int(ipSeg[i]) << 8 * (3 - i)
        return val

    def _long2ip(self, ipval):
        try:
            ipVal = int(ipval)
        except ValueError:
            return ''

        if ipVal < 0 or ipVal > 4294967295:
            return ''

        ipSeg = [str((ipVal >> 8 * i) % 256) for i in range(3, -1, -1)]
        ip = '.'.join(ipSeg)
        return ip

    def _ip2hex(self, ip):
        ipSeg = ip.split('.')
        ipSegHex = [str(hex(int(seg)))[2:] for seg in ipSeg]
        ipSegHexPad = ['0' + str(seg) if len(str(seg)) == 1 else str(seg) for seg in ipSegHex]
        return ''.join(ipSegHexPad)

    def _validIp(self, ip):
        isIp = True
        ipPattern = r'^(25[0-5]|2[0-4]\d|[01]?\d{1,2})(\.(25[0-5]|2[0-4]\d|[01]?\d{1,2})){3}$'
        if not re.match(ipPattern, ip):
            isIp = False
        return isIp

    def _ts2date(self):
        ts = self.timestamp.get()
        try:
            ts = float(ts)
            if self.unit.get() == 'ms':
                ts = ts / 1000

            localtime = time.localtime(ts)
            dateTime = time.strftime('%Y-%m-%d %H:%M:%S', localtime)
            self.dataTime.set(dateTime)
        except:
            self.timestamp.set('Invalid timestamp')

    def _now(self):
        ts = time.time()
        self.timestamp.set(ts * 1000)
        self.unit.set('ms')
        self._ts2date()


if __name__ == '__main__':
    app = App()
