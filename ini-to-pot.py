#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 2014 - Ignacio Rodríguez <ignacio@sugarlabs.org>
# This is for the .ini file.
# How to use: script.py file.ini, it will write a file.po

FINAL_TEXT = '''msgid ""
msgstr ""
"Project-Id-Version: \\n"
"POT-Creation-Date: \\n"
"PO-Revision-Date: \\n"
"Last-Translator: \\n"
"Language-Team: \\n"
"MIME-Version: 1.0\\n"
"Content-Type: text/plain; charset=utf-8\\n"
"Content-Transfer-Encoding: 8bit\\n"
"Language: en\\n"
"X-Generator: ini-to-pot script\\n"\n
'''
DATA = 'msgid "{msgid}"\nmsgstr ""\n\n'

import re
import sys
keys_added = []


def convert_ini_to_po(text):
    for match in re.finditer(ur'(\w+)\s*=\s*(.*)', text):
        global FINAL_TEXT
        word_id, translated_text = match.groups()
        if word_id not in keys_added:
            FINAL_TEXT += DATA.format(msgid=translated_text)
            keys_added.append(word_id)
    print "%d words added to result.pot" % len(keys_added)
    open("result.pot", "w").write(FINAL_TEXT)

try:
    text = open(sys.argv[1], "r").read()
    convert_ini_to_po(text)
except IndexError:
    print "You need to specify a ini file\n> python script.py myini.ini"
except IOError:
    print "File '%s' not found" % sys.argv[1]
