#!/usr/bin/env python3
#-*- encoding:utf-8 -*-

# func: F*ck it, the repo overwrite my script.
#       trans the inappropriate form into stand forms!
#       (主题)（(第n课)）.pdf     ===>        (第n课)：(主题).pdf


import os
import re
from os import path

def transform():
    # start with current path
    for item in os.listdir():
        if path.isdir(item):
            os.chdir(item)
            transform()
            os.chdir('..')

        if item.find('.') != -1:
            subfix  = item[item.find('.')+1:]
            if subfix != 'pdf':
                continue
            pattern1= '(.*)：(.*)\.pdf'
            pattern2= '(.*)（(.*)）\.pdf'
            if re.match(pattern1, item) != None:
                pass
            elif re.match(pattern2, item) != None:
                # transform it!
                temp = re.match(pattern2, item)
                newname = temp.group(2)+'：'+temp.group(1)+".pdf"
                os.rename(item, newname)
            else:
                # some forms we don't support
                continue

if __name__ == "__main__":
    print("Now we start !")
    transform()
    print("We've finished it, check it!")
