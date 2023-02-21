import urllib.request, urllib.parse, urllib.error

"""This is the simplest version of a web browser that I could find written
in python, in just 3 lines of code (not including the import information) you 
can read all the data from yahoo's UK web page. This shows the power of Python"""

class BrowserData:

    def len_browser_open(self):
        open_browser = self.browser_open()
        print(len(open_browser), 'is the length, and the type is', type(open_browser))
        return len(open_browser)


    def browser_open(self):
        fhand = urllib.request.urlopen('http://uk.yahoo.com/')
        for line in fhand:
            stringer = line.decode().strip()
            return stringer
