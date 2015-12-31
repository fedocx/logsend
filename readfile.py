#!/usr/bin/env python
#
import ConfigParser
import configure

class readfile:
    def __init__():
        firstline=a
        lastline=a
        linenum=0
        configure=configure.Configure()

    def readfile(filename,line):
        try:
            srcfile=open(filename,'r')
            linenum=1
            while 1:
                line=srcfile.readline()
                if linenum>line:
                    logs.logsend(line)
                if not line:
                    break
                linenum=linenum+1
                pass
        finally:
            srcfile.close()


    def setconfigure(filename):
        self.configure.setoptions(filename,self.firstline,self.lastline,self.linenum)

    def getvaluefromconfig(filename)
        self.firstline=configure.getoption("FIRSTLINE",filename)
        self.lastline=configure.getoption("LASTLINE",filename)
        self.linenum=configure.getoption("LINENUM",filename)
        
    def getvaluefromfile(filename)
        try:
            srcfile=open(filename,'r')
            self.linenum=0
            self.firstline=srcfile.readline()
            while 1:
                srcfile.seek(0)
                self.lastline=srcfile.readline()
                if not line:
                    break
                self.linenum=self.linenum+1
                pass
        finally:
            srcfile.close()
