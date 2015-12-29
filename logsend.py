#!/usr/bin/env python
#

import logging
import logging.handlers

class Locallog:
    def __init__(self,destip,destport):
#logger.setLevel(logging.INFO)
        self.logger=logging.getLogger("test")
        self.logger.setLevel(logging.DEBUG)
        logging.basicConfig(level=logging.DEBUG,
            format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
            datefmt='%a, %d %b %Y %H:%M:%S',
            filename='myapp.log',
            filemode='w')



        LOG_FILE = 'myapp.log'
        #console = logging.handlers.RotatingFileHandler(LOG_FILE, maxBytes = 100*1024*1024, backupCount = 5)
        remote=logging.handlers.SysLogHandler(address=(destip, destport), facility='auth')

        format = '%(asctime)s %(filename)s[line:%(lineno)d]  %(levelname)s %(message)s'
        formatter = logging.Formatter(format)  

        #console.setFormatter(formatter)
        remote.setFormatter(formatter)


        #logger.addHandler(console)
        self.logger.addHandler(remote)
    def logsend(self,message):
        self.logger.info(message)
        #logger.close()




