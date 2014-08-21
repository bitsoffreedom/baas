#!/usr/bin/env python3

import sys
import os.path
import email
import time

LOGFILE = "${HOME}/baas.log"
msg = email.message_from_file(sys.stdin)
headersFrom     = msg.get('From')
headersSubject  = msg.get('Subject')
headersDate     = msg.get('Date')
headersReceived = msg.get_all('Received')
#deliveryDate    = time.strftime("%a, %d %b %Y %H:%M:%S +0000",
#               time.gmtime(msg.get_date()))

log = open(os.path.expandvars(LOGFILE),'a')
log.write("\nfrom:     %s\n subject:  %s\n date:     %s\n\n" \
          % (headersFrom, headersSubject, headersDate))
for r in headersReceived:
    log.write("  %s\n" % r)
log.close()
