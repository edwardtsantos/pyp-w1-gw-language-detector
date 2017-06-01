# -*- coding: utf-8 -*-
import re
"""This is the entry point of the program."""

def detect_language(text, languages):
    prev_count = 0
    most_language_words = ""

    for l in languages:
        common_words = l['common_words']
        regex = re.compile(r'\b(%s)\b'%'|'.join(common_words),flags=re.IGNORECASE)
        if ( len(re.findall(regex,text)) > prev_count ):
            most_language_words = l['name']
            prev_count = len(re.findall(regex,text))

    return most_language_words
