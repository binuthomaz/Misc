#!/usr/bin/python

import re
import sys

def port_args(proc_text):
    args = []
    while re.search("\$%d" % (len(args) + 1), proc_text) :
        args.append('VARCHAR')

    return re.sub("\(\s*varargs\s*\)", "(%s)" % ', '.join(args), proc_text, flags=re.IGNORECASE)


proc_text = open(sys.argv[1], 'r').read()

ported_proc_text_step1 = port_args(proc_text)

print ported_proc_text_step1
