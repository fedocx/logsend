#!/usr/bin/env python
#python

import logsend
import readfile
import configure
import judge



configure=configure.Configure()
first=configure.readoption
judge=judge.Judge(filename)

filename='aa.txt'
readfile.readfile(filename)

