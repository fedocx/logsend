#!/usr/bin/env python
#

import ConfigParser

class Configure:
    def __init__():
        configurefile="logdata.conf"
        filename="FILENAME"
        firstline="FIRSTLINE"
        lastline="LASTLINE"
        linenum="LINENUM"
        config = ConfigParser.ConfigParser()
        self.config.read(self.configurefile)
        self.config.add_section(self.firstline)
        self.config.add_section(self.lastline)
        self.config.add_section(self.linenum
        self.config.add_section(self.filename)
    def setoption(optionname,filename,value):
        self.config.set(optionname,filename,value)
        f=open(configurefile,"a+")
        self.config.write(f)
        f.close()
    def setoptions(filename,firstlinevalue,lastlinevalue,linenumvalue):
        setoption(filename,firstline,firstlinevalue)
        setoption(filename,lastline,lastlinevalue)
        setoption(filename,linenum,linenumvalue)
    def getoption(optionname,filename)
        self.config.read(self.configurefile)
        access = config.get(optionname,filename)
        return access
    def getsections(optionname)
        self.config.read(self.configurefile)
        access = config.options(optionname)
        return access

aa=Configure()
aa.getoption("LASTLINE")
